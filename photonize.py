import os
from PIL import Image
from PIL.ExifTags import TAGS

current_cwd = os.getcwd()
print(current_cwd)
file_list = os.listdir(current_cwd)
print(file_list)

file_ext = ["jpg", "jpeg", "JPG", "png", "PNG", "NEF", "THM", "AVI", "mp4"]

cut_filelist = [n for n in file_list if n[-3:] in file_ext]

print(cut_filelist)

