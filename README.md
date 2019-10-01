# Desktop Cleaner

Track every type of files in a specific directory and keep them organized into another folder in such a easy way.

## Setup
This project requires `Python3`, `PIP`.  
You'll also need to ensure your SSH keys are stored in Github for the machine you're creating projects from.

## How it works
This script is simply based on:  
- Track a specific directory(e.g: desktop), if new file is added then move
- move files
- run in the background
- System for file organization
	- Folders for each file type category (e.g Images, Video, Audio, Text etc.)
	- Within folders we need to organise by date, create subfolders with date as name something like
		- 2019
			September
				9th
- need to find all file types to check what file has been added

## Installation
1. Clone this project
2. Navigate ti this project directory
3. **Optional**: `python3 -m venv venv`, to install the virtual env
4. **Optional**: To activate env : `source venv/bin/activate`, and to deactivate it simply type `deactivate`
5. Requirements:
	- Have/create 2 folders: oldDesktop(folder to track files) and newDesktop(new destination) or new ones created by yourself but remember to changed that on file script
	- Install watchdog, `pip install watchdog`
	- Set folder path correctly
6. Have in the new destination, the main folders declared in the extension type section(i.e: Media, Images, Videos, Programming, etc) if not the script will be fail


## Usage
To run the script `python cleandesk.py`.  
When the script starts, just move something in the folder to track to see the changes.  
Only for MacOS system: if you want to run it in background, it's necessary open Automator.app and create an Application, click on Library, and then on Utilities and run shell script and type the command to use the script and save it anywhere.