# NOTE: this script must be in RenPy SDK dir (next to renpy.py)
# Pylint is off because _don't ask me_ how I made it work. Pylint would have no clue as well.
# pylint: skip-file

# We'll need this to stub renpy.game.args
from argparse import Namespace

# Entrypoint to Ren'Py
import renpy
renpy.import_all()

from pathlib import Path
mas_dir = Path("../mas/Monika After Story")
mas_rpy_glob = mas_dir.glob("**/*.rpy")
src_dir = Path("../pysrc")
src_dir.mkdir(parents=True, exist_ok=True)


def parse_rpy(fn):
    lines = renpy.parser.list_logical_lines(fn, None, 1, add_lines=True)
    nested = renpy.parser.group_logical_lines(lines)

    renpy.game.args = Namespace(compile_python=False)
    renpy.game.script = renpy.script.Script()

    l = renpy.lexer.Lexer(nested)
    rv = renpy.parser.parse_block(l)
    return rv

def stream_python_src(rv):
    for init in filter(lambda it: isinstance(it, renpy.ast.Init), rv):
        for python in filter(lambda it: isinstance(it, renpy.ast.Python), init.block):
            yield init.priority, python.store, init.filename, python.linenumber, python.code.source

def extract_init_python(fn):
    def write_python(fn):
        script_name = Path(fn).name

    rv = parse_rpy(str(rpy_path.absolute()))
    init_stores = {}

    for block in stream_python_src(rv):
        priority, store, filename, line, source = block
        if store not in init_stores:
            init_stores[store] = []

        blocks = init_stores[store]
        blocks.append(block)

    return init_stores

def merge_init_blocks(all_dict, stores_dict):
    for store, blocks in stores_dict.items():
        if store not in all_dict:
            all_dict[store] = blocks
        all_dict[store].extend(blocks)

def sort_init_blocks(all_dict):
    for blocks in all_dict.values():
        blocks.sort(key=lambda it: it[0])

def dump_init_blocks(all_dict):
    for store, blocks in all_dict.items():
        store_name = store.split(".")[1] if store != "store" else "store"
        with open(Path(src_dir, f"{store_name}.py"), "w") as f:
            for block in blocks:
                rel_path = Path(block[2]).relative_to(mas_dir)
                f.write(f"# *** Extracted from [{rel_path}] ***\n"
                        f"# init {block[0]} python in {store_name}:\n")
                f.write(block[4])
                f.write("\n\n")


all_init_stores = {}
print("Extracting Python from 'init python' blocks...")

for rpy_path in mas_rpy_glob:
    print(f"  - Processing {rpy_path}...")
    init_stores = extract_init_python(rpy_path)
    merge_init_blocks(all_init_stores, init_stores)

print()
print("Sorting 'init python' blocks and dumping...")

sort_init_blocks(all_init_stores)
dump_init_blocks(all_init_stores)
print(f"Done, extracted sources written to {src_dir}.")
