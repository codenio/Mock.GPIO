# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning where possible.

## [0.2.0] - 2025-09-29
### Changed
- Minimalized `Makefile` to essential targets.
- `pyproject.toml`: set `dependencies = []` and removed dynamic dependency loading.
  This avoids PyPy 3.11 failures from `nh3`/PyO3 in CI.
- Added `tox.ini` and `make tox` for local matrix testing with pyenv.

## [0.1.10] - 2025-09-29
### Added
- Standard Makefile with targets for install, test, publish, clean, help, etc.
- LICENSE (GPL-3.0) file.
- pyproject.toml for modern build config.
- MANIFEST.in for packaging.
- requirements-dev.txt for development dependencies.
- CHANGELOG.md.


