Automatic Desktop Cleaner

- Track desktop, if new file is added then move
- move files
- run in the background
- System for file organization
	- Folders for each file tyoe category (e.g Images, Video, Audio, Text etc.)
	- Within folders we need to organise by date,
		create subfolders with date as name something like
		- 2019
			September
				9th
- need to find all file types to check what file has been added	


1. python3 -m venv venv, to install the virtual env
2. Activate env : "source venv/bin/activate"
3. Requirements:
	- Have/create 2 folders: oldDesktop(folder to track files) and newDesktop(new destination)
	- Install watchdog, pip install watchdog
	- Set folder path correctly
4. Have in the new destination, the main folders declared in extension type section(Media...Images...Videos...Programming...etc) if not the script will be fail
3. pyhton cleandesk.py
4. When start the script, just move something in folder_to_track to see the changes
6. To run on background, is necessary open Automator.app and create an Application, click on Library, and then on Utilities and run shell script and type the command to use the script and save it anywhere.