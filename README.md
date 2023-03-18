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

* generate-new-dico script
* translate dummy texts, check version of VPVEM
* Remove in dbm dictioannary "di.ogg": "DUMMY", "didi.ogg": "DUMMY"
* cd .\WOW-VoicePack-Generator\


* python scripts\cmd-oggfiles-update-voicepack.py -c .\my-audio-configs\aws-french-optimal-config.json .\dbm-dictionaries\dbm-vp-fr.json ..\DBM-VoicePack-FrenchFemale\DBM-VPFrenchFemale\dictionary.json -o .\test\ -e AWS
* copy generated file from test to ..\DBM-VoicePack-FrenchFemale\DBM-VPFrenchFemale\dictionary.json