# -*- mode: python ; coding: utf-8 -*-

<<<<<<< HEAD
data_files = [
    ('py_apps/ui/*.tcss', 'py_apps/ui'),
    ('py_apps/apps/browser/lnk/*', 'py_apps/apps/browser/lnk'),
]
=======
>>>>>>> c8b487e (fix firefox install bug)

a = Analysis(
    ['py_apps/main.py'],
    pathex=[],
    binaries=[],
<<<<<<< HEAD
    datas=data_files,
=======
    datas=[('py_apps/ui/*.tcss', 'py_apps/ui')],
>>>>>>> c8b487e (fix firefox install bug)
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
