from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'sharvil':
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
        'noname':  '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Uncategorized',
        # audio
        '.aif':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.cda':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.mid':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.midi':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.mp3':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.mpa':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.ogg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.wav':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.wma':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.wpl':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        '.m3u':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Audio',
        # text
        '.txt':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        '.doc':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Word',
        '.docx':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Word',
        '.pages':  '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Word',
        '.odt ':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        '.pdf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/PDF',
        '.rtf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        '.tex':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        '.wks ':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        '.wps':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        '.wpd':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Text_Files',
        # video
        '.3g2':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.3gp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.avi':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.flv':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.h264':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.m4v':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.mkv':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.mov':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.mp4':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.mpg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.mpeg':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.rm':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.swf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.vob':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        '.wmv':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Video',
        # images
        '.ai':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.bmp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.gif':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.jpg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.jpeg':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.png':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.ps':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.psd':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.svg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.tif':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.tiff':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        '.cr2':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Media/Images',
        # internet
        '.asp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.aspx':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.cer':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.cfm':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.cgi':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.pl':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.css':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.htm':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.js':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.jsp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.part':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.php':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.rss':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.xhtml':  '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        '.html':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Internet',
        # compressed
        '.7z':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.arj':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.deb':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.pkg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.rar':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.rpm':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.tar.gz': '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.z':      '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        '.zip':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Compressed',
        # disc
        '.bin':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.dmg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.iso':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.toast':  '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        '.vcd':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Disc',
        # data
        '.csv':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.dat':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.db':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.dbf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.log':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.mdb':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.sav':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.sql':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.tar':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.xml':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        '.json':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Database',
        # executables
        '.apk':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        '.bat':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        '.com':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        '.exe':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        '.gadget': '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        '.jar':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        '.wsf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Executables',
        # fonts
        '.fnt':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Fonts',
        '.fon':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Fonts',
        '.otf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Fonts',
        '.ttf':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Other/Fonts',
        # presentations
        '.key':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Presentations',
        '.odp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Presentations',
        '.pps':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Presentations',
        '.ppt':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Presentations',
        '.pptx':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Presentations',
        # programming
        '.c':      '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/C&C++',
        '.class':  '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Java',
        '.java':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Java',
        '.py':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Python',
        '.sh':     '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/Shell',
        '.h':      '/Users/sharvilarjunwadkar/Downloads/sharvil/Programming/C&C++',
        # spreadsheets
        '.ods':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Excel',
        '.xlr':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Excel',
        '.xls':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Excel',
        '.xlsx':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Excel',
        '.numbers':'/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Excel',
        # system
        '.bak':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.cab':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.cfg':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.cpl':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.cur':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.dll':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.dmp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.drv':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.icns':   '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.ico':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.ini':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.lnk':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.msi':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.sys':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System',
        '.tmp':    '/Users/sharvilarjunwadkar/Downloads/sharvil/Text/Other/System'
        }


folder_to_track = '/Users/sharvilarjunwadkar/Downloads'
folder_destination = '/Users/sharvilarjunwadkar/Downloads/sharvil'
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
