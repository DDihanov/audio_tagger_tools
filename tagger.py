import os
import sys
import re
import mutagen
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
import mutagen.id3

for root, dirs, files in os.walk('E:/music/test/'):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if file.endswith('.JPG') or file.endswith('.jpg') or file.endswith('.m3u') or file.lower() == ".ds_store":
            continue
        print(len(path) * '---', file)
        path = os.path.join(root, file)
        flac_file = mutagen.flac.Open(path)
        flac_file['title'] = file.replace(".flac", "")
        flac_file.save()
        print(path)
