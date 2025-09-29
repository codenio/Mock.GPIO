#!/bin/bash
# Copyright (c) 2025 codenio ( Aananth K )
# SPDX-License-Identifier: GPL-3.0-only
rm -rf build/
rm -rf dist/

python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*