import os
import sys
import re
import mutagen
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3

for root, dirs, files in os.walk('E:/music/test2/'):
    path = root.split(os.sep)
    toDelete = re.split((" |, |,"), os.path.basename(root)[12:])
    print(toDelete)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if file.endswith('.JPG') or file.endswith('.jpg') or file.endswith('.m3u'):
            continue
        print(len(path) * '---', file)
        for splitter in toDelete:
            if file.__contains__(splitter):
                audio = EasyID3(os.path.join(root, file))
                audio['title'] = file.replace(".flac", "")
                audio.save()
                print(path)
