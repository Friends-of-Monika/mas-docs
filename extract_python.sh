#!/bin/sh

if [ ! -d renpy ]; then
    echo "Cannot locate 'renpy' directory, run ./extract_py.sh before running this script." >&2
    exit 1
fi

if [ ! -d mas ]; then
    echo "Cannot locate 'mas' directory, clone MAS git repo before running this script." >&2
    exit 1
fi

cd renpy || exit 1
ln -f ../extract_python.py extract_python.py
./lib/py3-linux-x86_64/python ./extract_python.py
