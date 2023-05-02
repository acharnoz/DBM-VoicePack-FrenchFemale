import shutil
from pathlib import Path
import os


#define a function & pass dst. directory and src. directories
def merge_directories(new_directory_name, *directories_to_merge):
    if not os.path.exists(new_directory_name):
        os.makedirs(new_directory_name) #create a dst. directory if not exist

    for directory in directories_to_merge: 
        for item in os.listdir(directory):  #iterate sub-directory from source folders
            #join path of folder and sub-folder
            s = os.path.join(directory, item)
            d = os.path.join(new_directory_name, item)
            if os.path.isdir(s):
                if item in os.listdir(new_directory_name):
                    files = os.listdir(s)
                    for file in files:  #iterate file from sub-folder
                        j = os.path.join(s, file)
                        k = os.path.join(d, file)
                        shutil.copy2(j,k)  #paste file in already existed sub-directory
                else:
                    shutil.copytree(s, d)  #create a sub-directory in dst directory then paste file
            else:
                shutil.copy2(s, d)  #paste file in already existed sub-directory

VPVEM_path = Path("G:\World of Warcraft\_retail_\Interface\AddOns\DBM-VPVEM")
VPVEM_JSON_path = Path("G:\World of Warcraft\_retail_\Interface\AddOns\DBM-VPVEM\DBM-VPVEM-REF.json")
VPGEN_path = Path("G:\Dev\WOW-VoicePack-Generator")
ADDON_path = Path("G:\Dev\DBM-VoicePack")
TMPDIR_path = Path("G:\Dev\WOW-VoicePack-Generator\\tmp-dbm-output")
SOUNDSDIR_path = Path("G:\Dev\WOW-VoicePack-Generator\dbm-dictionaries\sounds")

cmdoggfilesupdatevoicepack = VPGEN_path / "scripts" / "cmd-oggfiles-update-voicepack.py"
cmdoggfilescreatevoicepack = VPGEN_path / "scripts" / "cmd-oggfiles-create-voicepack.py"


params = []

EN_VP_JSON_PATH = VPGEN_path / "dbm-dictionaries" / "dbm-vp-en.json"
FR_VP_JSON_PATH = VPGEN_path / "dbm-dictionaries" / "dbm-vp-fr.json"

cfgFemaleFR = VPGEN_path / "my-audio-configs" / "aws-fr-female-cfg.json"
addonFemaleFR = ADDON_path / "DBM-VPFrenchFemale"
params.append([cfgFemaleFR,addonFemaleFR,FR_VP_JSON_PATH])

cfgMaleFR = VPGEN_path / "my-audio-configs" / "aws-fr-male-cfg.json"
addonMaleFR = ADDON_path / "DBM-VPFrenchMale"
params.append([cfgMaleFR,addonMaleFR,FR_VP_JSON_PATH])

cfgFemaleEN = VPGEN_path / "my-audio-configs" / "aws-en-female-cfg.json"
addonFemaleEN = ADDON_path / "DBM-VPEnglishFemale"
params.append([cfgFemaleEN,addonFemaleEN,EN_VP_JSON_PATH])

cfgMaleEN = VPGEN_path / "my-audio-configs" / "aws-en-male-cfg.json"
addonMaleEN = ADDON_path / "DBM-VPEnglishMale"
params.append([cfgMaleEN,addonMaleEN,EN_VP_JSON_PATH])


#Update pkg
for param in params:

    CFG = param[0]
    ADDON = param[1]
    VP_JSON_PATH = param[2]
    ADDON_JSON = ADDON / "dictionary.json"

    cmd = f"python \"{cmdoggfilesupdatevoicepack}\" -c {CFG} {VP_JSON_PATH} {ADDON_JSON} -o {TMPDIR_path} -e AWS"
    print(cmd)
    os.system(cmd)
    merge_directories(TMPDIR_path, SOUNDSDIR_path)
    merge_directories(ADDON, TMPDIR_path)
    shutil.rmtree(TMPDIR_path)
    os.mkdir(TMPDIR_path) 

# Generate all files
# for param in params:

#     CFG = param[0]
#     ADDON = param[1]
#     VP_JSON_PATH = param[2]

#     cmd = f"python \"{cmdoggfilescreatevoicepack}\" -e AWS -c {CFG} -o {TMPDIR_path} {VP_JSON_PATH}"
#     print(cmd)
#     os.system(cmd)
#     merge_directories(TMPDIR_path, SOUNDSDIR_path)
#     merge_directories(ADDON, TMPDIR_path)
#     shutil.rmtree(TMPDIR_path)
#     os.mkdir(TMPDIR_path) 
 