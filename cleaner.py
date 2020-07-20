from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
#import json
#import shutil
#import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Foldername where you want these files to go':
                try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'
                    file_exists = os.path.isfile(extensions_folders[extension] + '/' + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]
                        new_name = new_name.split('/')[4]
                        file_exists = os.path.isfile(extensions_folders[extension] + '/' + new_name)

                    src = folder_to_track + '/' + filename

                    ''' Following few lines make Year and Month folder in each file '''
                    '''

                    year = datetime.datetime.year
                    month = datetime.datetime.month

                    folder_destination_path = extensions_folders[extension]

                    year_exists = False
                    month_exists = False

                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == str(year):
                            folder_destination_path = extensions_folders[extension] + '/' + str(year)
                            year_exists = True
                            if folder_month in os.listdir(extensions_folders[extension]):
                                if folder_month == str(month):
                                    folder_destination_path = extensions_folders[extension] + '/' + str(year) + str(month)
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + '/' + str(year))
                        folder_destination_path = extensions_folders[extension] + '/' + str(year)
                    if not month_exists:
                        os.mkdir(extensions_folders[extension] + '/' + str(year) + str(month))
                        folder_destination_path = extensions_folders[extension] + '/' + str(year) + str(month) '''                   

                    new_name = extensions_folders[extension] + '/' + new_name
                    os.rename(src, new_name)

                except Exception:
                    print(filename)

extensions_folders = {
        # No name
        'noname':  '/Users/UserName/Downloads/FolderName/Other/Uncategorized',
        # audio
        '.aif':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.cda':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.mid':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.midi':   '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.mp3':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.mpa':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.ogg':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.wav':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.wma':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.wpl':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        '.m3u':    '/Users/UserName/Downloads/FolderName/Media/Audio',
        # text
        '.txt':    '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        '.doc':    '/Users/UserName/Downloads/FolderName/Text/Word',
        '.docx':   '/Users/UserName/Downloads/FolderName/Text/Word',
        '.pages':  '/Users/UserName/Downloads/FolderName/Text/Word',
        '.odt ':   '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        '.pdf':    '/Users/UserName/Downloads/FolderName/Text/PDF',
        '.rtf':    '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        '.tex':    '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        '.wks ':   '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        '.wps':    '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        '.wpd':    '/Users/UserName/Downloads/FolderName/Text/Text_Files',
        # video
        '.3g2':    '/Users/UserName/Downloads/sharvil/Media/Video',
        '.3gp':    '/Users/UserName/Downloads/sharvil/Media/Video',
        '.avi':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.flv':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.h264':   '/Users/UserName/Downloads/FolderName/Media/Video',
        '.m4v':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.mkv':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.mov':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.mp4':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.mpg':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.mpeg':   '/Users/UserName/Downloads/FolderName/Media/Video',
        '.rm':     '/Users/UserName/Downloads/FolderName/Media/Video',
        '.swf':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.vob':    '/Users/UserName/Downloads/FolderName/Media/Video',
        '.wmv':    '/Users/UserName/Downloads/FolderName/Media/Video',
        # images
        '.ai':     '/Users/UserName/Downloads/FolderName/Media/Images',
        '.bmp':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.gif':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.jpg':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.jpeg':   '/Users/UserName/Downloads/FolderName/Media/Images',
        '.png':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.ps':     '/Users/UserName/Downloads/FolderName/Media/Images',
        '.psd':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.svg':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.tif':    '/Users/UserName/Downloads/FolderName/Media/Images',
        '.tiff':   '/Users/UserName/Downloads/FolderName/Media/Images',
        '.cr2':    '/Users/UserName/Downloads/FolderName/Media/Images',
        # internet
        '.asp':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.aspx':   '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.cer':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.cfm':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.cgi':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.pl':     '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.css':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.htm':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.js':     '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.jsp':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.part':   '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.php':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.rss':    '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.xhtml':  '/Users/UserName/Downloads/FolderName/Other/Internet',
        '.html':   '/Users/UserName/Downloads/FolderName/Other/Internet',
        # compressed
        '.7z':     '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.arj':    '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.deb':    '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.pkg':    '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.rar':    '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.rpm':    '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.tar.gz': '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.z':      '/Users/UserName/Downloads/FolderName/Other/Compressed',
        '.zip':    '/Users/UserName/Downloads/FolderName/Other/Compressed',
        # disc
        '.bin':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.dmg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.iso':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.toast':  '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.vcd':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        # data
        '.csv':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.dat':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.db':     '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.dbf':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.log':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.mdb':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.sav':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.sql':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.tar':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.xml':    '/Users/UserName/Downloads/FolderName/Programming/Database',
        '.json':   '/Users/UserName/Downloads/FolderName/Programming/Database',
        # executables
        '.apk':    '/Users/UserName/Downloads/FolderName/Other/Executables',
        '.bat':    '/Users/UserName/Downloads/FolderName/Other/Executables',
        '.com':    '/Users/UserName/Downloads/FolderName/Other/Executables',
        '.exe':    '/Users/UserName/Downloads/FolderName/Other/Executables',
        '.gadget': '/Users/UserName/Downloads/FolderName/Other/Executables',
        '.jar':    '/Users/UserName/Downloads/FolderName/Other/Executables',
        '.wsf':    '/Users/UserName/Downloads/FolderName/Other/Executables',
        # fonts
        '.fnt':    '/Users/UserName/Downloads/FolderName/Other/Fonts',
        '.fon':    '/Users/UserName/Downloads/FolderName/Other/Fonts',
        '.otf':    '/Users/UserName/Downloads/FolderName/Other/Fonts',
        '.ttf':    '/Users/UserName/Downloads/FolderName/Other/Fonts',
        # presentations
        '.key':    '/Users/UserName/Downloads/FolderName/Text/Presentations',
        '.odp':    '/Users/UserName/Downloads/FolderName/Text/Presentations',
        '.pps':    '/Users/UserName/Downloads/FolderName/Text/Presentations',
        '.ppt':    '/Users/UserName/Downloads/FolderName/Text/Presentations',
        '.pptx':   '/Users/UserName/Downloads/FolderName/Text/Presentations',
        # programming
        '.c':      '/Users/UserName/Downloads/FolderName/Programming/C&C++',
        '.class':  '/Users/UserName/Downloads/FolderName/Programming/Java',
        '.java':   '/Users/UserName/Downloads/FolderName/Programming/Java',
        '.py':     '/Users/UserName/Downloads/FolderName/Programming/Python',
        '.sh':     '/Users/UserName/Downloads/FolderName/Programming/Shell',
        '.h':      '/Users/UserName/Downloads/FolderName/Programming/C&C++',
        # spreadsheets
        '.ods':    '/Users/UserName/Downloads/FolderName/Text/Excel',
        '.xlr':    '/Users/UserName/Downloads/FolderName/Text/Excel',
        '.xls':    '/Users/UserName/Downloads/FolderName/Text/Excel',
        '.xlsx':   '/Users/UserName/Downloads/FolderName/Text/Excel',
        '.numbers':'/Users/UserName/Downloads/FolderName/Text/Excel',
        # system
        '.bak':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.cab':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.cfg':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.cpl':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.cur':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.dll':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.dmp':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.drv':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.icns':   '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.ico':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.ini':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.lnk':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.msi':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.sys':    '/Users/UserName/Downloads/FolderName/Text/Other/System',
        '.tmp':    '/Users/UserName/Downloads/FolderName/Text/Other/System'
        }


folder_to_track = '/Users/UserName/Downloads'
folder_destination = '/Users/UserName/Downloads/FolderName'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
