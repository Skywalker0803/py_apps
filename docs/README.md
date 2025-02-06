<div align="center">

# PY Apps

</div>

> Trying to make useful softwares within reach

<!-- TODO: Replace with your project details. -->

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white&style=for-the-badge)](https://python.org "Go to Python website")

- [Installation](installation.md)
- [Usage](usage.md)
- [Development](development.md)
- [CI pipeline](ci-pipeline.md)
- [Deploy](deploy.md)

## Project Structure

```
py_apps/
    ├ apps/
    │   ├ browser/
    │   │   ├ lnk/
    │   │   ├ __init__.py
    │   │   ├ common.py
    │   │   ├ epiphany.py
    │   │   ├ falkon.py
    │   │   ├ firefox.py
    │   │   ├ midori.py
    │   │   └ vivaldi.py
    │   └ devtools/
    │       ├ vscode.py
    │       └ vscode.py
    ├ errors/
    │   ├ __init__.py
    │   ├ common.py
    │   ├ cmd_not_found.py
    │   ├ distro_x_only.py
    │   ├ unknown_pkg_manager.py
    │   └ unsupported_arch.py
    ├ pages/
    │   ├ __init__.py
    │   ├ browser.py
    │   ├ devtools.py
    │   └ main.py
    ├ ui/
    │   ├ __init__.py
    │   ├ dialog.py
    │   ├ dialog.tcss
    │   ├ notice.py
    │   ├ notice.tcss
    │   ├ selection.py
    │   └ selection.tcss
    ├ utils/
    │   ├ __init__.py
    │   ├ common.py
    │   ├ app_manage.py
    │   ├ cmd.py
    │   ├ network.py
    │   ├ sys.py
    │   └ utils.py
    ├ __init__.py
    └ main.py
```

## Special Thanks

> Appreciate all the people / project that had helped me in the passing time

- Python3
- [Textual TUI Library](https://textual.textualize.io/)
- [Project template](https://github.com/MichaelCurrin/py-project-template) by [@MichaelCurrin](https://github.com/MichaelCurrin)
- Inspired by [TMOE](https://github.com/2moe/tmoe) (or [Gitee unarchived Chinese version](https://gitee.com/mo2/linux)) part "tools"

I give my most sincere thank to all those above, thank for them making me myself now

Last, may all the beauty be blessed
