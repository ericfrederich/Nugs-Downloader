#!/usr/bin/env python3

from pathlib import Path
import json
from getpass import getpass
import sys
import shutil


config_file_path = Path("config.json")
config_backup_path = Path("config.bak.json")

if len(sys.argv[1:]) == 1 and sys.argv[1].startswith("Bearer "):
    token = sys.argv[1]
elif len(sys.argv[1:]) == 2 and sys.argv[1] == "Bearer" and len(sys.argv[2]) > 100:
    token = " ".join(sys.argv[1:])
else:
    token = getpass("Paste your token here (wont' be echo'd): ")

print(f"Copying {config_file_path} to {config_backup_path}")
shutil.copy2(config_file_path, config_backup_path)

with config_file_path.open("rt") as fin:
    data = json.load(fin)

data["token"] = token

with config_file_path.open("wt") as fout:
    print(json.dumps(data, sort_keys=True, indent=4), file=fout)
