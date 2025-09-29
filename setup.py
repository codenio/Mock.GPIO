from pathlib import Path
from distutils.util import convert_path

from setuptools import setup, find_packages

# Copyright (c) 2025 codenio ( Aananth K )
# SPDX-License-Identifier: GPL-3.0-only

readme = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

pkg_ns = {}

ver_path = convert_path("Mock/__init__.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), pkg_ns)

setup(
    name="Mock.GPIO",
    version=pkg_ns["__version__"],
    description="Mock Library for RPi.GPIO",
    url="https://github.com/codenio/Mock.GPIO",
    author="Aananth K",
    author_email="aananthraj1995@gmail.com",
    license="GPL-3.0",
    packages=find_packages(exclude=[]),
    install_requires=[],
    zip_safe=False,
    long_description_content_type="text/markdown",
    long_description=readme,
)
