# coding: utf-8
import sys
from pathlib import Path

AUTHOR = "K2cr2O1"
TEAM = "天机阁(Fairy-Oracle-Sanctuary)"
VERSION = "1.0.0"
YEAR = "2026"
UPDATE_TIME = "2026-1-10"

RELEASE_URL = "https://github.com/Fairy-Oracle-Sanctuary/NEO-Bot-Framework/releases"
GITHUB_URL = "https://github.com/Fairy-Oracle-Sanctuary/NEO-Bot-Framework"

CONFIG_FOLDER = Path("AppData").absolute()

CONFIG_FILE = CONFIG_FOLDER / "config.json"
DB_PATH = CONFIG_FOLDER / "database.db"

COVER_FOLDER = CONFIG_FOLDER / "Cover"
COVER_FOLDER.mkdir(exist_ok=True, parents=True)

PIC_SUFFIX = ".jpg"

if sys.platform == "win32":
    EXE_SUFFIX = ".exe"
else:
    EXE_SUFFIX = ""
