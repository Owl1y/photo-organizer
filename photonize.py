import os
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import time
import datetime

def get_date(video_path):
    try:
        exif_dict = piexif.load(video_path)
        if 'Exif' in exif_dict:
            exif_data = exif_dict['Exif']
            creation_date_tag = piexif.ExifIFD.DateTimeOriginal

            if creation_date_tag in exif_data:
                creation_date = exif_data[creation_date_tag].decode('utf-8')
                return creation_date

    except (KeyError, ValueError):
        pass

    return None

current_cwd = os.getcwd()
file_list = os.listdir(current_cwd)

file_ext = ["jpg", "jpeg", "JPG", "png", "PNG", "NEF", "THM", "AVI", "mp4", "MOD"]
cut_filelist = [n for n in file_list if n[-3:] in file_ext]

# print(cut_filelist)

for source in cut_filelist:
    # current_source = TinyTag.get(source)
    # print(source, get_date(source))
    os_time = os.path.getmtime(source)
    modification_time = datetime.datetime.fromtimestamp(os_time)
    iso_time = modification_time.date().isoformat()
    # print(time.ctime(os_time))
    
    print(source, get_date(source), iso_time)
    # print(datetime.datetime.fromtimestamp(os_time))


