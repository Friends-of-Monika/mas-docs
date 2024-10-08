"""
This script parses Python AST of .py modules in 'pysrc' directory in an attempt
to extract MAS documentation from functions etc.
"""

from typing import Tuple, List, Dict, Any

from pathlib import Path
from textwrap import dedent
import json
import ast
import re

ClassStruct = Tuple[str, List[ast.expr], str | None, List[ast.FunctionDef], int]
FuncStruct = Tuple[str, ast.arguments, str | None, int]
DocDict = Dict[str, Any]


# Python 2 syntax incompatibilities (quick) fixes

def remove_ur_ru_prefix(src: str) -> str:
    """Removes ur/ru string literal prefix from py2 source code."""
    pattern = r'\b([uU][rR]|[rR][uU])(["\'])'
    modified_code = re.sub(pattern, r'r\2', src)
    return modified_code

def convert_octal_literals(src: str) -> str:
    """Converts literals like 0755 from py2 source code to 0oXXX."""
    pattern = r'(?<![-\d.])\b0([0-7]+)\b(?!\.\d)'
    modified_code = re.sub(pattern, r'0o\1', src)
    return modified_code


# dedent(...) fix

def fix_dedent(docstring: str) -> str:
    """If string does not start with an empty line, copies indent from second
       line and inserts it before first to properly apply dedent(...)."""
    lines = docstring.splitlines()
    if len(lines) >= 2 and lines[0].strip() and lines[1].startswith((' ', '\t')):
        indent = lines[1][:len(lines[1]) - len(lines[1].lstrip())]
        lines[0] = indent + lines[0]
        lines.insert(0, '')
    return '\n'.join(lines)


# AST node decomposition

def decompose_func(node: ast.FunctionDef) -> FuncStruct:
    """Decomposes function definition to name, args, and docstring."""
    f_deco = node.decorator_list
    f_name = node.name
    f_args = node.args

    docstring: str | None = None
    if isinstance(node.body[0], ast.Expr):
        if isinstance(node.body[0].value, ast.Constant):
            docstring = node.body[0].value.value

    return f_name, f_args, docstring, node.lineno, f_deco

def decompose_class(node: ast.ClassDef) -> ClassStruct:
    """Decomposes class definition to name, bases, docstring and methods."""
    c_deco = node.decorator_list
    c_name = node.name
    c_bases = node.bases

    docstring: str | None = None
    if isinstance(node.body[0], ast.Expr):
        if isinstance(node.body[0].value, ast.Constant):
            docstring = node.body[0].value.value

    methods = [decompose_func(child) for child in node.body
               if isinstance(child, ast.FunctionDef)]
    return c_name, c_bases, docstring, methods, c_deco


# Data exporting (e.g. converting to renderable parameters)

def export_class_doc(struct: ClassStruct) -> Dict[str, Any]:
    """Serializes class structure to dictionary suitable for rendering."""

    data: Dict[str, Any] = {}
    data["type"] = "class"
    data["class_decorators"] = [ast.unparse(node) for node in struct[4]]
    data["identifier"] = struct[0]
    data["class_bases"] = [ast.unparse(node) for node in struct[1]]

    if struct[2] is not None:
        data["docstring"] = dedent(fix_dedent(struct[2])).strip()

    data["class_functions"] = [export_func_doc(fn) for fn in struct[3]]

    return data

def export_func_doc(struct: FuncStruct) -> Dict[str, Any]:
    """Serializes function structure to dictionary suitable for rendering."""

    data: Dict[str, Any] = {}
    data["type"] = "function"
    data["function_decorators"] = [ast.unparse(node) for node in struct[4]]
    data["identifier"] = struct[0]

    if struct[2] is not None:
        data["docstring"] = dedent(fix_dedent(struct[2])).strip()

    data["function_args"] = {
        "args": [arg.arg for arg in struct[1].args],
        "defaults": [ast.unparse(_def) for _def in struct[1].defaults],
        "pos_only_args": [arg.arg for arg in struct[1].posonlyargs],
        "kw_only_args": [arg.arg for arg in struct[1].kwonlyargs],
        "kw_defaults": [ast.unparse(_def) for _def in struct[1].kw_defaults],
        "kw_arg": struct[1].kwarg.arg if struct[1].kwarg is not None else None,
        "var_arg": struct[1].vararg.arg if struct[1].vararg is not None else None
    }

    return data


# Python parsing

def extract_docs(path: Path) -> List[DocDict]:
    """Parses Python code at given path and returns dictionary of documented
       members (identifier -> doc dict)."""

    with open(path, "r", encoding="utf-8") as f: # pylint: disable=redefined-outer-name
        src_text = f.read()

    # Apply py2-to-3 fixes
    src_text = remove_ur_ru_prefix(src_text)
    src_text = convert_octal_literals(src_text)

    src_ast = ast.parse(src_text, filename=path)
    doc_dicts: List[DocDict] = []

    for node in src_ast.body:
        doc_dict: DocDict | None = None

        if isinstance(node, ast.FunctionDef):
            st = decompose_func(node)
            doc_dict = export_func_doc(st)
        elif isinstance(node, ast.ClassDef):
            st = decompose_class(node)
            doc_dict = export_class_doc(st)

        if doc_dict is not None:
            doc_dicts.append(doc_dict)

    return doc_dicts


pysrc_dir = Path(Path(__file__).parent, "pysrc")
doc_dir = Path(Path(__file__).parent, "doc/json")
doc_dir.mkdir(parents=True, exist_ok=True)

print("Parsing Python files...")
for py_path in pysrc_dir.glob("*.py"):
    print(f"  - Processing {py_path.relative_to(Path(__file__).parent)}...")
    docs = extract_docs(py_path)

    script_name = ".".join(py_path.name.split(".")[:-1]) # pylint: disable=invalid-name
    doc_path = Path(doc_dir, f"{script_name}.json")
    with open(doc_path, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2)
