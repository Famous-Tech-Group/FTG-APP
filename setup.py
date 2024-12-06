# setup.py
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {
    "packages": ["os", "sys", "PyQt5", "sqlalchemy", "black", "requests", "pyperclip", "difflib", "git"],
    "excludes": [],
    "include_files": ["logo.png"]  # Add any additional files you need
}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Famous-Tech-Group",
    version="0.1",
    description="Famous-Tech Collaboration Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="logo.ico")]
)