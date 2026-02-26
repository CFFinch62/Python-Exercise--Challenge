#!/usr/bin/env python3
"""
build.py — Cross-platform build script for Python Exercises for Beginners.

Usage:
    python build.py           # Release build (spec file)
    python build.py --clean   # Delete dist/ and build/ before building

Supported platforms: Linux, macOS, Windows
Requires: pip install pyinstaller
"""

import subprocess
import sys
import os
import shutil
import argparse

# ── Config ────────────────────────────────────────────────────────────────────
APP_NAME   = "PythonExercises"
SPEC_FILE  = "python_exercises.spec"

PLATFORM   = sys.platform          # 'linux', 'darwin', 'win32'
IS_WINDOWS = PLATFORM == "win32"
IS_MAC     = PLATFORM == "darwin"
IS_LINUX   = PLATFORM == "linux"

# Where PyInstaller writes its output
DIST_DIR   = os.path.join(os.path.dirname(__file__), "dist")
BUILD_DIR  = os.path.join(os.path.dirname(__file__), "build")

# ── Helpers ───────────────────────────────────────────────────────────────────

def run(cmd: list[str]) -> None:
    """Run a command, printing it first, and exit on failure."""
    print(f"\n▶ {' '.join(cmd)}\n")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"\n❌  Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)


def check_prerequisites() -> None:
    """Verify Python version and PyInstaller availability."""
    if sys.version_info < (3, 8):
        print("❌  Python 3.8+ is required.")
        sys.exit(1)

    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("❌  PyInstaller is not installed.")
        print("    Run:  pip install pyinstaller")
        sys.exit(1)

    try:
        import customtkinter  # noqa: F401
    except ImportError:
        print("❌  customtkinter is not installed.")
        print("    Run:  pip install customtkinter")
        sys.exit(1)

    print(f"✅  Python {sys.version.split()[0]}  |  Platform: {PLATFORM}")


def clean() -> None:
    """Remove dist/ and build/ directories."""
    for folder in (DIST_DIR, BUILD_DIR):
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"🗑   Removed {folder}")


def build() -> None:
    """Run PyInstaller using the spec file."""
    if not os.path.exists(SPEC_FILE):
        print(f"❌  Spec file not found: {SPEC_FILE}")
        sys.exit(1)

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--clean",           # remove previous PyInstaller temp files
        "--noconfirm",       # overwrite dist without asking
        SPEC_FILE,
    ]
    run(cmd)


def report() -> None:
    """Print the location and size of the generated artefact."""
    if IS_WINDOWS:
        exe_path = os.path.join(DIST_DIR, APP_NAME + ".exe")
    elif IS_MAC:
        exe_path = os.path.join(DIST_DIR, "Python Exercises for Beginners.app")
    else:  # Linux
        exe_path = os.path.join(DIST_DIR, APP_NAME)

    if os.path.exists(exe_path):
        if os.path.isdir(exe_path):   # macOS .app bundle
            size_mb = sum(
                os.path.getsize(os.path.join(root, f))
                for root, _, files in os.walk(exe_path)
                for f in files
            ) / (1024 * 1024)
        else:
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)

        print(f"\n✅  Build complete!")
        print(f"    Output : {exe_path}")
        print(f"    Size   : {size_mb:.1f} MB")

        if IS_LINUX:
            print(f"\n    Run with:  chmod +x \"{exe_path}\" && \"{exe_path}\"")
        elif IS_WINDOWS:
            print(f"\n    Run with:  \"{exe_path}\"")
        elif IS_MAC:
            print(f"\n    Run with:  open \"{exe_path}\"")
    else:
        print(f"\n⚠️   Expected output not found at: {exe_path}")
        print("    Check the dist/ folder manually.")


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build Python Exercises for Beginners with PyInstaller."
    )
    parser.add_argument(
        "--clean", action="store_true",
        help="Delete dist/ and build/ directories before building."
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  Python Exercises for Beginners — Build Script")
    print("=" * 60)

    check_prerequisites()

    if args.clean:
        clean()

    build()
    report()


if __name__ == "__main__":
    main()
