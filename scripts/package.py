import shutil
from pathlib import Path


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

key_to_var = {}
key_to_var["DBMEA_VERSION_KEY"] = "0.3.1"

src1 = Path("G:\\Dev\\DBMEventAnnouncement\\DBMEA")
src2 = Path("G:\\Dev\\DBMEventAnnouncement\\DBMEA-FR-Voicepacks")
src3 = Path("G:\\Dev\\DBMEventAnnouncement\\DBMEA-EN-Voicepacks")
wow_addon_pkg = Path("G:\\Dev\\DBMEventAnnouncement\\package\\DBMEA")

addons = [src1]

for child in src2.iterdir():
    addons.append(child)

for child in src3.iterdir():
    addons.append(child)

for p in addons:
    addon_name = p.name
    dest = wow_addon_pkg / addon_name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(p, dest)

output_DBMEA_toc = Path(wow_addon_pkg / "DBMEA" / "DBMEA.toc")
replace_keys(key_to_var, output_DBMEA_toc)

output_filename = Path(wow_addon_pkg.parent / (wow_addon_pkg.name + "_v" + key_to_var["DBMEA_VERSION_KEY"]) )
shutil.make_archive(output_filename, 'zip', wow_addon_pkg)
