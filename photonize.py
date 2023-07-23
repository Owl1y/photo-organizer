import os
import datetime

current_cwd = os.getcwd()
file_list = os.listdir(current_cwd)

file_ext = ["jpg", "jpeg", "JPG", "png", "PNG", "NEF", "THM", "AVI", "mp4", "MOD"]
cut_filelist = [n for n in file_list if n[-3:] in file_ext]

for source in cut_filelist:
    
    os_time = os.path.getmtime(source)
    modification_time = datetime.datetime.fromtimestamp(os_time)
    iso_time = modification_time.date().isoformat()
    
    dir_with_time = current_cwd + "/" + iso_time
    dir_exist = os.path.exists(dir_with_time) 

    if not dir_exist:
        os.mkdir(dir_with_time)

    os.rename(current_cwd + "/" + source, dir_with_time + "/" + source)
        
