from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'newDesktop':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" + year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/franciscozambrano/Desktop/newDesktop/Other/Uncategorized",
#Audio
    '.aif' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.cda' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.mid' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.midi' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.mp3' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.mpa' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.ogg' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.wav' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.wma' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.wpl' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
    '.m3u' : "/Users/franciscozambrano/Desktop/newDesktop/Media/Audio",
#Text
    '.txt' : "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
    '.doc' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Microsoft/Word",
    '.docx' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Microsoft/Word",
    '.odt ' : "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
    '.pdf': "/Users/franciscozambrano/Desktop/newDesktop/Text/PDF",
    '.rtf': "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
    '.tex': "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
    '.wks ': "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
    '.wps': "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
    '.wpd': "/Users/franciscozambrano/Desktop/newDesktop/Text/TextFiles",
#Video
    '.3g2': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.3gp': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.avi': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.flv': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.h264': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.m4v': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.mkv': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.mov': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.mp4': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.mpg': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.mpeg': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.rm': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.swf': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.vob': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
    '.wmv': "/Users/franciscozambrano/Desktop/newDesktop/Media/Video",
#Images
    '.ai': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.bmp': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.gif': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.ico': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.jpg': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.jpeg': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.png': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.ps': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.psd': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.svg': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.tif': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.tiff': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
    '.CR2': "/Users/franciscozambrano/Desktop/newDesktop/Media/Images",
#Internet
    '.asp': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.aspx': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.cer': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.cfm': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.cgi': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.pl': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.css': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.htm': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.js': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.jsp': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.part': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.php': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.rss': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
    '.xhtml': "/Users/franciscozambrano/Desktop/newDesktop/Other/Internet",
#Compressed
    '.7z': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.arj': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.deb': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.pkg': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.rar': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.rpm': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.tar.gz': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.z': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
    '.zip': "/Users/franciscozambrano/Desktop/newDesktop/Other/Compressed",
#Disc
    '.bin': "/Users/franciscozambrano/Desktop/newDesktop/Other/Disc",
    '.dmg': "/Users/franciscozambrano/Desktop/newDesktop/Other/Disc",
    '.iso': "/Users/franciscozambrano/Desktop/newDesktop/Other/Disc",
    '.toast': "/Users/franciscozambrano/Desktop/newDesktop/Other/Disc",
    '.vcd': "/Users/franciscozambrano/Desktop/newDesktop/Other/Disc",
#Data
    '.csv': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.dat': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.db': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.dbf': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.log': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.mdb': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.sav': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.sql': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.tar': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.xml': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
    '.json': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Database",
#Executables
    '.apk': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
    '.bat': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
    '.com': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
    '.exe': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
    '.gadget': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
    '.jar': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
    '.wsf': "/Users/franciscozambrano/Desktop/newDesktop/Other/Executables",
#Fonts
    '.fnt': "/Users/franciscozambrano/Desktop/newDesktop/Other/Fonts",
    '.fon': "/Users/franciscozambrano/Desktop/newDesktop/Other/Fonts",
    '.otf': "/Users/franciscozambrano/Desktop/newDesktop/Other/Fonts",
    '.ttf': "/Users/franciscozambrano/Desktop/newDesktop/Other/Fonts",
#Presentations
    '.key': "/Users/franciscozambrano/Desktop/newDesktop/Text/Presentations",
    '.odp': "/Users/franciscozambrano/Desktop/newDesktop/Text/Presentations",
    '.pps': "/Users/franciscozambrano/Desktop/newDesktop/Text/Presentations",
    '.ppt': "/Users/franciscozambrano/Desktop/newDesktop/Text/Presentations",
    '.pptx': "/Users/franciscozambrano/Desktop/newDesktop/Text/Presentations",
#Programming
    '.c': "/Users/franciscozambrano/Desktop/newDesktop/Programming/C&C++",
    '.class': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Java",
    '.dart': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Dart",
    '.py': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Python",
    '.sh': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Shell",
    '.swift': "/Users/franciscozambrano/Desktop/newDesktop/Programming/Swift",
    '.html': "/Users/franciscozambrano/Desktop/newDesktop/Programming/html",
    '.h': "/Users/franciscozambrano/Desktop/newDesktop/Programming/html",
#Spreadsheets
    '.ods' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlr' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xls' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Microsoft/Excel",
    '.xlsx' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.cab' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.cfg' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.cpl' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.cur' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.dll' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.dmp' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.drv' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.icns' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.ico' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.ini' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.lnk' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.msi' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.sys' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
    '.tmp' : "/Users/franciscozambrano/Desktop/newDesktop/Text/Other/System",
}

folder_to_track = '/Users/franciscozambrano/Desktop/oldDesktop'
folder_destination = '/Users/franciscozambrano/Desktop/newDesktop'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()