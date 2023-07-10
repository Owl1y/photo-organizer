import os
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
import time
import datetime

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
    
    # print(source, get_date(source), iso_time)
    print(source, iso_time)
    # print(datetime.datetime.fromtimestamp(os_time))


