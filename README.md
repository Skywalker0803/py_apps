# Py3-TMOE 📦
> Trying to revive the old TMOE project!

<!-- Shields generated with https://michaelcurrin.github.io/badge-generator/ -->

[![Python CI](https://github.com/MichaelCurrin/py-project-template/actions/workflows/main.yml/badge.svg)](https://github.com/MichaelCurrin/py-project-template/actions/workflows/main.yml)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/py-project-template?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/py-project-template/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white&style=for-the-badge)](https://python.org "Go to Python website")

## For developers
[![code style - black](https://img.shields.io/badge/code_style-black-blue&style=for-the-badge)](https://black.readthedocs.io/)
[![dev dependency - flake8](https://img.shields.io/badge/code_format-flake8-blue&style=for-the-badge)](https://pypi.org/project/flake8)
[![dev dependency - pylint](https://img.shields.io/badge/code_linting-pylint-blue&style=for-the-badge)](https://pypi.org/project/pylint)
[![dev dependency - mypy](https://img.shields.io/badge/type_test-mypy-blue&style=for-the-badge)](https://pypi.org/project/mypy)
[![dev dependency - pytest](https://img.shields.io/badge/test-pytest-blue&style=for-the-badge)](https://pypi.org/project/pytest)

**Note**: this project uses black & isort for code formatting, `make` for automatic tasks.

DO NOT USE default code formatting feature of your IDE, make sure to run `make fmt` before committing to the project

### Make usage

- `make`: this uses `make install` by default
- `make install`: install the dependencies & dev dependencies with `pip3`
- `make upgrade`: upgrade the project's current dependencies with `pip3`
- `make fmt`: try for format your code with `black` & `isort`
- `make fmt-check`: check the formatting issues in the project
- `make lint`: start linting your code with `pylint` & `flake8`
- `make fix`: run both `make fmt` & `make lint` together
- `make test`: start the tests with `pytest`
- `make run`: run the main project in `src/` as a module

For other usages, please check in the project's [Makefile](/Makefile) for more information


## License

Released under [MIT](/LICENSE) by [@Skywalker0803](https://github.com/Skywalker0803).

A copy of the original license must be included if a significant portion of this template or project is used. You could rename it to `LICENSE-source` and then include your own `LICENSE` file with your name.
