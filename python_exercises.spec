# -*- mode: python ; coding: utf-8 -*-
# ============================================================
#  python_exercises.spec  —  PyInstaller build specification
#  Python Exercises for Beginners
# ============================================================

import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# ── Gather customtkinter assets (themes, images) ─────────────────────────────
ctk_datas = collect_data_files('customtkinter')

# ── Analysis ─────────────────────────────────────────────────────────────────
a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # Bundle the data modules alongside main
        ('exercises_data.py', '.'),
        ('solutions_data.py', '.'),
        # Bundle images folder
        ('images', 'images'),
        # customtkinter requires its theme/image data at runtime
        *ctk_datas,
    ],
    hiddenimports=[
        'customtkinter',
        'tkinter',
        'tkinter.messagebox',
        '_tkinter',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Trim unused heavy packages to keep exe size reasonable
        'matplotlib', 'numpy', 'pandas', 'PIL', 'PyQt5', 'PyQt6',
        'scipy', 'sklearn', 'tensorflow', 'torch',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# ── Executable ───────────────────────────────────────────────────────────────
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PythonExercises',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    # Hide the console window on Windows and macOS (it's a GUI app).
    # On Linux we keep it False so terminal launch still works cleanly.
    console=(sys.platform == 'linux'),
    disable_windowed_traceback=False,
    argv_emulation=False,      # macOS only
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='images/PythonExercisesIcon.png',
)

# ── macOS .app bundle ─────────────────────────────────────────────────────────
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='Python Exercises for Beginners.app',
        icon='images/PythonExercisesIcon.png',
        bundle_identifier='com.pythonexercises.beginners',
        info_plist={
            'NSHighResolutionCapable': True,
            'CFBundleShortVersionString': '1.0.0',
        },
    )
