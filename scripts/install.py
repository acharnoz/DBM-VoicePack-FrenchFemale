import shutil
from pathlib import Path

addonversion = "0.3.6"
DBMVoiceVersion = "18"

Interface = "110107"
InterfaceMists = "50500"
InterfaceCata = "40402"
InterfaceWrath = "30404"
InterfaceTBC = "20504"
InterfaceClassic = "11507"

DIPPKG_PATH = Path("G:\Dev\DBM-VoicePack\zip-files")
ADDON_path = Path("G:\Dev\DBM-VoicePack")
wow_addon_path=Path("G:\\World of Warcraft\\_retail_\\Interface\\AddOns")

def replace_keys(key_to_var, filepath: Path):
    # Opening our text file in read only
    # mode using the open() function
    with open(filepath, 'r') as file:
        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = file.read()

        # Searching and replacing the text
        # using the replace() function
        for key, val in key_to_var.items():
            data = data.replace(key, val)

    # Opening our text file in write only
    # mode to write the replaced content
    with open(filepath, 'w') as file:

        # Writing the replaced data in our
        # text file
        file.write(data)

    # Printing Text replaced
    print("Text replaced")

def install_addon(addon_name:str, version:str):

    key_to_var = {}
    key_to_var["INTERFACE_KEY"] = Interface
    key_to_var["INTERFACECLASSIC_KEY"] = InterfaceClassic
    key_to_var["INTERFACETBC_KEY"] = InterfaceTBC
    key_to_var["INTERFACEWARTH_KEY"] = InterfaceWrath
    key_to_var["INTERFACECATA_KEY"] = InterfaceCata
    key_to_var["INTERFACEMISTS_KEY"] = InterfaceMists
    key_to_var["VERSION_KEY"] = version
    key_to_var["DBM_VOICE_KEY"] = DBMVoiceVersion

    src = ADDON_path / addon_name
    dest = wow_addon_path / addon_name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

    files = []
    files.append(addon_name+".toc")
    for file in files:
        toc_file = Path(dest / file)
        replace_keys(key_to_var, toc_file)

install_addon("DBM-VPEnglishFemale", addonversion)
install_addon("DBM-VPFrenchFemale", addonversion)
install_addon("DBM-VPEnglishMale", addonversion)
install_addon("DBM-VPFrenchMale", addonversion)