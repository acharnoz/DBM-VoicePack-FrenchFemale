import shutil
from pathlib import Path

Interface = "100007"
InterfaceWrath = "30401"
InterfaceClassic = "11403"
DIPPKG_PATH = Path("G:\Dev\DBM-VoicePack\zip-files")
ADDON_path = Path("G:\Dev\DBM-VoicePack")

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

def package_addon(addon_name:str, version:str):

    key_to_var = {}
    key_to_var["INTERFACE_KEY"] = Interface
    key_to_var["INTERFACECLASSIC_KEY"] = InterfaceWrath
    key_to_var["INTERFACEWARTH_KEY"] = InterfaceClassic
    key_to_var["VERSION_KEY"] = version

    src = ADDON_path / addon_name
    dest = DIPPKG_PATH / addon_name / addon_name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

    files = []
    files.append(addon_name+".toc")
    files.append(addon_name+"_Vanilla.toc")
    files.append(addon_name+"_Wrath.toc")
    for file in files:
        toc_file = Path(dest / file)
        replace_keys(key_to_var, toc_file)

    zippath = Path( DIPPKG_PATH / (addon_name + "_multi" + "_v" + version) )
    shutil.make_archive(zippath, 'zip', DIPPKG_PATH / addon_name )
    shutil.rmtree(DIPPKG_PATH / addon_name)

package_addon("DBM-VPEnglishFemale", "0.1.1")
package_addon("DBM-VPFrenchFemale", "0.2.8")
package_addon("DBM-VPEnglishMale", "0.1.1")
package_addon("DBM-VPFrenchMale", "0.1.1")