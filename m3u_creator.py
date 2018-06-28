import os
import sys
import glob
import io
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

unsuccesful = []

def create_m3u(dir=".", playlist_name="."):
    try:
        print("Processing directory '%s'..." % dir)

        playlist = ''
        mp3s = []
        glob_pattern = "*.[mM][pP]3"

        os.chdir(dir)

        for file in glob.glob(glob_pattern):
            if playlist == '':
                playlist = playlist_name + '.m3u'


            to_check = EasyID3(file)

            if 'tracknumber' in to_check:
                meta_info = {
                    'filename': file,
                    'length': int(MP3(file).info.length),
                    'tracknumber': EasyID3(file)['tracknumber'][0].split('/')[0],
                }
            else:
                meta_info = {
                    'filename': file,
                    'length': int(MP3(file).info.length),
                }

            mp3s.append(meta_info)

        if len(mp3s) > 0:
            print("Writing playlist '%s'..." % playlist)

            # write the playlist
            of = io.open(playlist, 'w', encoding="utf-8")
            of.write("#EXTM3U\n")

            # # sorted by track number
            # for mp3 in sorted(mp3s, key=lambda mp3: int(mp3['tracknumber'])):
            #     of.write("#EXTINF:%s,%s\n" % (mp3['length'], mp3['filename']))
            #     of.write(mp3['filename'] + "\n")

            for mp3 in mp3s:
                of.write("#EXTINF:%s,%s\n" % (mp3['length'], mp3['filename']))
                of.write(mp3['filename'] + "\n")
            of.close()
        else:
            print("No mp3 files found in '%s'." % dir)

    except:
        unsuccesful.append(to_check + os.linesep)
        print("ERROR occured when processing directory '%s'. Ignoring." % dir)
        print("Text: ", sys.exc_info()[0])


def main(argv=None):
    if argv is None:
        argv = sys.argv

    directory = ""

    directory = input()

    for root, dirs, files in os.walk(directory):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for dir in dirs:
            dirPath = os.path.join(root + os.sep + dir)
            isEmpty = True
            for file in os.listdir(dirPath):
                if file.endswith(".mp3"):
                    isEmpty = False
                    break
            if not isEmpty:
                create_m3u(os.path.join(root + os.sep + dir), dir)


    print('Could not create playlist for:' + os.sep)
    for song in unsuccesful:
        print(song)
    return 0


# if name == "main":
sys.exit(main())
