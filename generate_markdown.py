"""
This script loads .json docs from 'doc/json' directory and generates Markdown
pages for documented functions and saves them to 'doc/pages'
"""

from typing import List, Tuple, Dict, Any, IO
from collections import OrderedDict
from io import StringIO

from pathlib import Path
import json
import ast
import re


def parse_mas_docstring(docstring: str) -> Dict[str, Any]: # pylint: disable=too-many-branches,too-many-locals,too-many-statements
    """Parses MAS-specific docstrings (to the best of its ability) and returns
       contained parameters, descriptions, assumes, throws etc. in a dictionary."""

    lines = docstring.strip().splitlines()
    data = {
        "description": "",
        "inputs": OrderedDict(),
        "returns": "",
        "assumes": "",
        "raises": [],
        "notes": []
    }

    # Regex patterns for sections
    section_header_pattern = re.compile(r'^(?P<indent>\s*)(?P<section>IN|INPUTS?|PARAMS?|OUT|ASSUMES?|RETURNS?|RAISES?|NOTES?):?(?:\s+(?P<content>.+))?$') # pylint: disable=line-too-long
    # Adjusted to match 'param_name - description' or 'param_name:'
    param_pattern = re.compile(r'^(?P<indent>\s*)(?P<name>\w+)\s*(?:-\s*(?P<desc>.+)|:\s*)$')
    # Matches '- ExceptionType - description'
    raises_pattern = re.compile(r'^\s*-\s*(?P<type>\w+)(?:\s*-\s*|\s+)(?P<desc>.+)$')

    current_section = "description"
    last_param = None
    last_raise_index = -1
    section_content = ""
    section_indent = 0  # Indentation level of the current section header
    param_indent = None  # Indentation level of the current parameter

    for line in lines:
        line = line.rstrip()

        # Attempt to match a section header
        section_match = section_header_pattern.match(line)
        if section_match:
            indent = len(section_match.group('indent'))
            if indent <= section_indent:
                # Store content from the previous section
                if current_section == "description":
                    data["description"] += section_content.strip() + " "
                elif current_section in ("assume", "assumes"):
                    data["assumes"] += section_content.strip() + " "
                elif current_section in ("out", "return", "returns"):
                    data["returns"] += section_content.strip() + " "
                elif current_section in ("note", "notes"):
                    data["notes"].append(section_content.strip())
                elif current_section in ("raise", "raises"):
                    pass  # Raises are handled separately

                # Start the new section
                section_content = ""
                current_section = section_match.group('section').lower()
                content = section_match.group('content')
                section_indent = indent  # Update current section indentation

                # Include content on the same line as the section header
                if content:
                    section_content += content.strip() + " "

                last_param = None
                last_raise_index = -1
                param_indent = None
                continue

        # Process lines based on the current section
        if current_section in ("in", "param", "params"):
            # Try matching a parameter line
            param_match = param_pattern.match(line)
            if param_match:
                param_name = param_match.group('name')
                param_desc = param_match.group('desc')
                param_indent = len(param_match.group('indent'))
                if param_desc is not None:
                    param_desc = param_desc.strip()
                    data["inputs"][param_name] = param_desc
                    last_param = param_name
                else:
                    data["inputs"][param_name] = ''
                    last_param = param_name
                continue
            elif last_param:
                # Check if line is indented more than param_indent
                line_indent = len(line) - len(line.lstrip())
                if line_indent > param_indent:
                    data["inputs"][last_param] += ' ' + line.strip()
                else:
                    # Line is not indented, could be a new section or invalid format
                    # Reset last_param and param_indent
                    last_param = None
                    param_indent = None
                    # Re-process the line as it might be a section header or other content
                    # Continue to next iteration to avoid double processing
                    section_match = section_header_pattern.match(line)
                    if section_match:
                        # Decrement the loop counter to reprocess this line
                        continue
            else:
                pass

        elif current_section in ("raise", "raises"):
            # Try matching an exception line
            raise_match = raises_pattern.match(line)
            if raise_match:
                exception_type = raise_match.group('type')
                exception_desc = raise_match.group('desc').strip()
                data["raises"].append({
                    "type": exception_type,
                    "description": exception_desc
                })
                last_raise_index = len(data["raises"]) - 1
            elif last_raise_index != -1:
                # Append to the last exception's description
                data["raises"][last_raise_index]["description"] += " " + line.strip()
            else:
                pass

        else:
            # Accumulate content for other sections
            section_content += line.strip() + " "

    # Store any remaining content from the last section
    if current_section == "description":
        data["description"] += section_content.strip() + " "
    elif current_section in ("out", "return", "returns"):
        data["returns"] += section_content.strip() + " "
    elif current_section in ("assume", "assumes"):
        data["assumes"] += section_content.strip() + " "
    elif current_section in ("note", "notes"):
        data["notes"].append(section_content.strip())

    # Strip excess whitespace
    data = {
        key: value.strip() if isinstance(value, str) else value
        for key, value in data.items()
    }

    return data


def is_deprecated(data: Dict[str, Any]) -> Tuple[bool, bool, str | None, str | None]:
    """Checks if given function/class is deprecated, if it raises, and optionally
       if returns use_instead."""

    doc_type = data["type"]
    decorators = data[f"{doc_type}_decorators"]

    deprecated = get_deprecated_decorator(decorators)
    if deprecated is None:
        return False, False, None

    kw_params: Dict[str, Any] = {}
    for keyword in deprecated.keywords:
        if isinstance(keyword.value, ast.Constant):
            kw_params[keyword.arg] = keyword.value.value

    should_raise = kw_params.get("should_raise", False)
    use_instead = kw_params.get("use_instead", None)
    use_instead_msg_fmt = kw_params.get("use_instead_msg_fmt",
                                        "Instead, consider using `{use_instead}`.")

    if use_instead_msg_fmt is not None:
        use_instead = use_instead_msg_fmt.format(use_instead=use_instead)

    return True, should_raise, use_instead


def is_internal_func(data: Dict[str, Any]) -> bool:
    """Checks if function is internal (prefixed by _ or __)."""
    return data["identifier"].startswith("_")

def is_mangled_name(data: Dict[str, Any]) -> bool:
    """Checks if function name is mangled (prefixed by _m1_XXX__)."""
    return bool(re.match(r"^_m1_\w+__\w+$", data["identifier"]))


def get_deprecated_decorator(unparsed_list: List[str]) -> ast.Call | None:
    """Tries to get AST of @store.mas_utils.deprecated decorator."""

    for expr_ast in map(ast.parse, unparsed_list):
        call_or_attr = expr_ast.body[0].value
        if isinstance(call_or_attr, ast.Call):
            if isinstance(call_or_attr.func, ast.Attribute):
                attr_name = call_or_attr.func.attr
                if attr_name == "deprecated":
                    return expr_ast.body[0].value

    return None


def generate_doc_markdown(json_path: Path, out_path: Path) -> None: # pylint: disable=redefined-outer-name
    """Generates .md page for given JSON doc path."""

    def write_md(doc_json: List[Dict[str, Any]], f: IO) -> None:
        classes = list(filter(lambda it: it["type"] == "class", doc_json))
        all_funcs = list(filter(lambda it: it["type"] == "function", doc_json))
        pub_funcs = list(filter(lambda it: not is_internal_func(it), all_funcs))
        int_funcs = list(filter(is_internal_func, all_funcs))

        for class_doc in classes:
            pass

        f.write("## Functions\n\n")
        for func_doc in pub_funcs:
            f.write(generate_func_markdown(func_doc))

        f.write("### Internal functions\n\n"
                "> [!CAUTION]\n"
                "> These functions are *internal* and are not recommended for use.\n\n")

        for func_doc in int_funcs:
            f.write(generate_func_markdown(func_doc, header_depth=4))

    with json_path.open("r") as f:
        doc_json = json.load(f)

    with out_path.open("w") as f:
        write_md(doc_json, f)


def generate_func_markdown(data: Dict[str, Any], header_depth: int = 3) -> str: # pylint: disable=too-many-locals
    """Generates Markdown section for given function doc data.
       Optional header_depth parameter defines Markdown header depth for
       function section."""

    def merge_args(args: List[str], defs: List[str]) -> List[Tuple[str, str | None]]:
        non_def_len = len(args) - len(defs)
        defs = [*(None for _ in range(non_def_len)), *defs]
        return list(zip(args, defs))

    def join_args(args: List[Tuple[str, str | None]]) -> str:
        return ", ".join(f"{name}={_def}" if _def is not None else name
                         for name, _def in args)

    name = data["identifier"]
    deco = data["function_decorators"]
    args = data["function_args"]["args"]
    defaults = data["function_args"]["defaults"]
    args_with_defs = merge_args(args, defaults)

    docstring = data.get("docstring", "")
    doc_data = parse_mas_docstring(docstring)
    doc_desc = doc_data["description"]
    doc_inputs = doc_data["inputs"]
    doc_outputs = doc_data["returns"]

    md = StringIO()
    md.write(f"{"#" * header_depth} def {name}({join_args(args_with_defs)})\n\n")

    is_depr, depr_raises, depr_use_instead = is_deprecated(data)
    if is_depr:
        if depr_raises:
            md.write("> [!CAUTION]\n"
                     "> This function is flagged as **deprecated** and **will raise an error.**")
        else:
            md.write("> [!WARNING]\n"
                     "> This function is flagged as **deprecated** and **is not recommended "
                     "for use.**")
        if depr_use_instead is not None:
            md.write(f"<br>\n> {depr_use_instead}")
        md.write("\n\n")

    if doc_desc:
        md.write(f"{doc_desc}\n\n")

    if deco:
        md.write("**Decorators:**\n")
        for expr in deco:
            md.write(f"- `@{expr}`\n")
        md.write("\n\n")

    if doc_inputs:
        md.write("**Parameters:**\n")
        for arg, description in doc_inputs.items():
            md.write(f"- `{arg}` &mdash; {description}\n")
        md.write("\n\n")

    if doc_outputs:
        md.write("**Returns:**<br>\n")
        md.write(doc_outputs)
        md.write("\n\n")

    return md.getvalue()


doc_dir = Path(Path(__file__).parent, "doc")
doc_json_dir = Path(doc_dir, "json")

doc_pages_dir = Path(doc_dir, "pages")
doc_pages_dir.mkdir(parents=True, exist_ok=True)
print("Generating Markdown docs...")

for json_path in doc_json_dir.glob("*.json"):
    print(f"  - Processing {json_path.relative_to(doc_json_dir)}...")
    md_doc_name = ".".join([*json_path.name.split(".")[:-1], "md"]) # pylint: disable=invalid-name
    md_path = Path(doc_pages_dir, md_doc_name)
    generate_doc_markdown(json_path, md_path)
