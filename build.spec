# -*- mode: python ; coding: utf-8 -*-

add_datas = [
    ('key2cursor/*.json', 'key2cursor'),
    ('key2cursor/tui/*.tcss', 'key2cursor/tui'),
    ('key2cursor/lib/*', 'key2cursor/lib'),
    ('key2cursor/tui/*', 'key2cursor/tui'),
    ('image/*', 'image'),
    ('image/*.ico', 'image'),
]

block_cipher = None

a = Analysis(
    ['key2cursor\\__main__.py'],
    pathex=[],
    binaries=[],
    datas=add_datas,
    hiddenimports=['plyer.platforms.win.notification'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='key2mouse_noconsole',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="image/key2mouse_icon.ico",
)
