# DBM-VoicePack
This is voice packs for DBM (Deadly Boss Mods) created by Milho and Daydream (Dalaran EU Realm). It provides voices for most important events tracked by DBM. Make sure you have previously installed an updated version of DBM before installing this addon.

**Remarks:**
* This plugin is in beta version and translations are still being adjusted, do not hesitate to give us feedback !
* We used artificial intelligence to transform the French text into voice, it does not replace a human voice but it allows faster development and updates in the first place.

**Settings:**
1. Type in the console /dbm. This opens the Deadly Boss Mods options window.
1. Select the Options tab.
1. In the list that appears below, select the Voice Alerts option in General Options.
1. In the box on the right, select "French XXXX by Milho" in the combo with the heading Voice package for voice alerts.
 
If there are any suggestions/problems, please contact me.
 
**How update audio files for DBM (reminder)**
* check toc format https://warcraft.wiki.gg/wiki/TOC_format
* https://github.com/DeadlyBossMods/DBM-Voicepack-VEM/tree/master/DBM-VPVEM
* generate-new-dico script (ctl F5 ici)
* Then in G:\Dev\WOW-VoicePack-Generator\dbm-dictionaries
* translate dummy texts, check version of VPVEM (update DMB Voice version un package and install script)
* Remove in dbm dictioannary "di.ogg": "DUMMY", "didi.ogg": "DUMMY"
* After update, rename new-dbm-vp-en.json/new-dbm-vp-fr.json in dbm-vp-en.json / dbm-vp-fr.json
* (in the powershell console) cd G:\Dev\WOW-VoicePack-Generator\
* launch poetry shell
* cd G:\Dev\DBM-VoicePack\scripts
* python .\update-voicepacks.py
* lancer ensuite package.py script (sous visual) (ctl F5 ici)

** How push to Curse
* edit the push_script.ps1 file to change the addon version (or wow version client)
* cd  G:\Dev\DBM-VoicePack\zip-files
* .\push_script.ps1 (execute)