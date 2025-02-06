# Installation

_TODO: Remove any unnecessary sections._


## Project requirements

_TODO: Update for appropriate minimum Python version and any other OS or project-level packages covered later. Optionally add more links._



| Name                                     | Description        |
|------------------------------------------|--------------------|
| [Python](https://www.python.org/) >= 3.8 | This project is developed under python 3.10 |
| `python3-pip`  | Just for ubuntu, for others, search yourself |
| `poetry` | Yet another pip, also able to manage venvs |


## Install hooks

```sh
$ make hooks    # Setup git pre-push hooks
```


## Install system dependencies

_TODO: Include any instructions or commands to install a package or application, other than Python. Example below using external reference and explicit instructions._

Install Python on your machine - see this Gist on [How to install Python 3](https://gist.github.com/MichaelCurrin/57caae30bd7b0991098e9804a9494c23).

### Ubuntu/Debian

_To be completed by you._

### macOS

_To be completed by you._

### Windows

_To be completed by you._


## Install project dependencies

It is usually best-practice in _Python_ projects to install into a sandboxed _virtual environment_, This will be locked to a specific Python version and contain only the _Python_ libraries that you install into it, so that your _Python_ projects do not get affected.

I use `poetry` by default, and [`poetry.toml`](/poetry.toml) is configured to open venv under /path/to/project/.venv/ directory

### Install with Pip

Create and activate a virtual environment:

```sh
$ python3 -m venv .venv
```

- Linux/macOS
    ```sh
    $ source .venv/bin/activate
    ```
- Windows
    ```powershell
    > .venv\Scripts\activate
    ```

> Note: If you need more info, follow this guide to [Set up a Python 3 Virtual Environment](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).

Install Python packages into the project's virtual environment:

```sh
$ make install
```

### Install with Poetry

Required - install Poetry on your system globally. See [Gist](https://gist.github.com/MichaelCurrin/8d6c377cc46ce2ef6f94e52b4a21787d).

Then Python packages into a virtual environment managed by Poetry:

```sh
$ poetry install
```

Upgrade packages when needed:

```sh
$ poetry update
```

---

You may continue to the [Usage](usage.md) doc.
