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


# AST node decomposition

def decompose_func(node: ast.FunctionDef) -> FuncStruct:
    """Decomposes function definition to name, args, and docstring."""
    f_name = node.name
    f_args = node.args

    docstring: str | None = None
    if isinstance(node.body[0], ast.Expr):
        if isinstance(node.body[0].value, ast.Constant):
            docstring = node.body[0].value.value

    return f_name, f_args, docstring, node.lineno

def decompose_class(node: ast.ClassDef) -> ClassStruct:
    """Decomposes class definition to name, bases, docstring and methods."""
    c_name = node.name
    c_bases = node.bases

    docstring: str | None = None
    if isinstance(node.body[0], ast.Expr):
        if isinstance(node.body[0].value, ast.Constant):
            docstring = node.body[0].value.value

    methods = [decompose_func(child) for child in node.body
               if isinstance(child, ast.FunctionDef)]
    return c_name, c_bases, docstring, methods, node.lineno

def unwind_attr(node: ast.Attribute) -> str:
    """Unwinds attribute chain and returns it in dot notation."""
    chain: List[str] = []
    current = node

    while not isinstance(current, ast.Name):
        chain.append(current.attr)
        current = current.value

    chain.append(current.id)
    return ".".join(chain[::-1])


# Data exporting (e.g. converting to renderable parameters)

def export_class_bases(base_nodes: List[ast.Name | ast.Attribute]) -> List[str]:
    """Serializes class bases to list of strings."""
    base_str: List[str] = []
    for node in base_nodes:
        if isinstance(node, ast.Name):
            base_str.append(node.id)
        elif isinstance(node, ast.Attribute):
            base_str.append(unwind_attr(node))
        else:
            raise ValueError(f"unexpected class base node {node!r}")
    return base_str

def export_class_doc(struct: ClassStruct) -> Dict[str, Any]:
    """Serializes class structure to dictionary suitable for rendering."""

    data: Dict[str, Any] = {}
    data["type"] = "class"
    data["identifier"] = struct[0]
    data["class_bases"] = export_class_bases(struct[1])
    data["line"] = struct[4]

    if struct[2] is not None:
        data["docstring"] = dedent(struct[2]).strip()
    data["class_functions"] = [export_func_doc(fn) for fn in struct[3]]

    return data

def export_func_doc(struct: FuncStruct) -> Dict[str, Any]:
    """Serializes function structure to dictionary suitable for rendering."""

    data: Dict[str, Any] = {}
    data["type"] = "function"
    data["identifier"] = struct[0]
    data["line"] = struct[3]

    data["function_args"] = {
        "args": [arg.arg for arg in struct[1].args],
        "pos_only_args": [arg.arg for arg in struct[1].posonlyargs],
        "defaults": [ast.unparse(_def) for _def in struct[1].defaults],
        "kw_defaults": [ast.unparse(_def) for _def in struct[1].kw_defaults],
        "kw_only_args": [arg.arg for arg in struct[1].kwonlyargs],
        "kw_arg": struct[1].kwarg.arg if struct[1].kwarg is not None else None,
        "var_arg": struct[1].vararg.arg if struct[1].vararg is not None else None
    }

    if struct[2] is not None:
        data["docstring"] = dedent(struct[2]).strip()

    return data


# Python parsing

def extract_docs(path: str) -> Dict[str, DocDict]:
    """Parses Python code at given path and returns dictionary of documented
       members (identifier -> doc dict)."""

    with open(path, "r", encoding="utf-8") as f: # pylint: disable=redefined-outer-name
        src_text = f.read()

    # Apply py2-to-3 fixes
    src_text = remove_ur_ru_prefix(src_text)
    src_text = convert_octal_literals(src_text)

    src_ast = ast.parse(src_text, filename=path)
    doc_dicts: Dict[str, DocDict] = {}

    for node in src_ast.body:
        if isinstance(node, ast.FunctionDef):
            st = decompose_func(node)
            doc = export_func_doc(st)
            doc_dicts[st[0]] = doc
        elif isinstance(node, ast.ClassDef):
            st = decompose_class(node)
            doc = export_class_doc
            doc_dicts[st[0]] = doc(st)

    return doc_dicts


pysrc_dir = Path(Path(__file__).parent, "pysrc")
doc_dir = Path(Path(__file__).parent, "doc/json")
doc_dir.mkdir(parents=True, exist_ok=True)

print("Parsing Python files...")
for py_path in pysrc_dir.glob("*.py"):
    print(f"  - Processing {py_path}...")
    docs = extract_docs(py_path)

    script_name = ".".join(py_path.name.split(".")[:-1]) # pylint: disable=invalid-name
    doc_path = Path(doc_dir, f"{script_name}.json")
    with open(doc_path, "w", encoding="utf-8") as f:
        json.dump(docs, f, indent=2)
