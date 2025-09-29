#!/bin/bash
# Copyright (c) 2025 codenio ( Aananth K )
# SPDX-License-Identifier: GPL-3.0-only
rm -rf build/
rm -rf dist/

python setup.py install

python3 setup.py install