# MAS Docs

An experimental attempt to extract Python code from `init x python in ...` blocks
in `.rpy` scripts of [Monika After Story](https://github.com/Monika-After-Story/MonikaModDev).

## Installing RenPy SDK

Run `./install_renpy.sh` script, it will download and extract RenPy SDK. It uses
RenPy 8+ (nightly build), but it seems to work just fine.

After it completes you'll have `renpy` directory. Do not rename it.

## Installing MAS

Run the following command in your terminal:
```shell
git clone https://github.com/Monika-After-Story/MonikaModDev mas
```

Make sure your target directory is `mas`. Don't change that name.

## Extracting Python

Run `./extract_python.sh` script (*do not* run `extract_python.py`, mind the `.py`);
it will only start if first hardlinked inside `renpy` directory, where RenPy SDK is.

After it completes, you'll have `pysrc` directory with `init python` scripts compiled
into `<store name>.py` Python files.

## Generating docs

Run `./extract_docs.py` script when you've done all previous steps.

After it completes, new/updated doc `.json` files will be placed in `doc/json` directory.
