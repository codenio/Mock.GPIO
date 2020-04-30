#!/bin/bash
rm -rf build/
rm -rf dist/

python setup.py install

python3 setup.py install