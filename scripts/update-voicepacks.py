import shutil
from pathlib import Path
import os

VPVEM_path = Path("G:\World of Warcraft\_retail_\Interface\AddOns\DBM-VPVEM")
VPVEM_JSON_path = Path("G:\World of Warcraft\_retail_\Interface\AddOns\DBM-VPVEM\DBM-VPVEM-REF.json")
VPGEN_path = Path("G:\Dev\WOW-VoicePack-Generator")
ADDON_path = Path("G:\Dev\DBM-VoicePack")
TMPDIR_path = Path("G:\Dev\WOW-VoicePack-Generator\\tmp-dbm-output")

cmdoggfilesupdatevoicepack = VPGEN_path / "scripts" / "cmd-oggfiles-update-voicepack.py"

EN_VP_JSON_PATH = VPGEN_path / "dbm-dictionaries" / "dbm-vp-en.json"
FR_VP_JSON_PATH = VPGEN_path / "dbm-dictionaries" / "dbm-vp-fr.json"

cfgFemaleFR = VPGEN_path / "my-audio-configs" / "aws-fr-female-cfg.json"
addonFemaleFR = ADDON_path / "DBM-VPFrenchFemale" / "dictionary.json"

cfgMaleFR = VPGEN_path / "my-audio-configs" / "aws-fr-male-cfg.json"
addonMaleFR = ADDON_path / "DBM-VPFrenchMale" / "dictionary.json"

cfgFemaleEN = VPGEN_path / "my-audio-configs" / "aws-en-female-cfg.json"
addonFemaleEN = ADDON_path / "DBM-VPEnglishFemale" / "dictionary.json"

cfgMaleEN = VPGEN_path / "my-audio-configs" / "aws-en-male-cfg.json"
addonMaleEN = ADDON_path / "DBM-VPEnglishMale" / "dictionary.json"

CFG = cfgFemaleFR
ADDON = addonFemaleFR
VP_JSON_PATH = FR_VP_JSON_PATH

cmd = f"python \"{cmdoggfilesupdatevoicepack}\" -c {CFG} {VP_JSON_PATH} {ADDON} -o {TMPDIR_path} -e AWS"
print(cmd)
os.system(cmd)
#* copy generated file from test to ..\DBM-VoicePack-FrenchFemale\DBM-VPFrenchFemale\dictionary.json