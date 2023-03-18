import shutil
from pathlib import Path
import os

VPVEM_path = Path("G:\World of Warcraft\_retail_\Interface\AddOns\DBM-VPVEM")
VPVEM_JSON_path = Path("G:\World of Warcraft\_retail_\Interface\AddOns\DBM-VPVEM\DBM-VPVEM-REF.json")
VPGEN_path = Path("G:\Dev\WOW-VoicePack-Generator")

cmddicocreate = VPGEN_path / "scripts" / "cmd-dico-create.py"
cmddicocompare = VPGEN_path / "scripts" / "cmd-dico-compare.py"
cmddicomerge = VPGEN_path / "scripts" / "cmd-dico-merge.py"


for LANG in ['fr','en']:
    
    VP_JSON_PATH = VPGEN_path / "dbm-dictionaries" / f"dbm-vp-{LANG}.json"
    VP_NEW_JSON_PATH = VPGEN_path / "dbm-dictionaries" / f"new-dbm-vp-{LANG}.json"

    cmd = f"python \"{cmddicocreate}\" -l {LANG} -n DBM-VPVEM-REF -o \"{VPVEM_JSON_path}\" \"{VPVEM_path}\""
    os.system(cmd)
    cmd = f"python \"{cmddicocompare}\" \"{VPVEM_JSON_path}\" \"{VP_JSON_PATH}\""
    os.system(cmd)
    cmd = f"python \"{cmddicomerge}\" \"{VP_JSON_PATH}\" \"{VPVEM_JSON_path}\" -o \"{VP_NEW_JSON_PATH}\""
    os.system(cmd)
