import os
from PIL import Image
from PIL.ExifTags import TAGS

def get_date(img_source):
    try:
        exif_data = img_source._getexif()
        
        # Iterate over all Exif tags
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag)
            if tag_name == 'DateTimeOriginal':
                return value
                
    except (AttributeError, KeyError, IndexError):
        # Handle cases where the image has no Exif data or no DateTimeOriginal tag
        pass
    
    return None




current_cwd = os.getcwd()
file_list = os.listdir(current_cwd)

file_ext = ["jpg", "jpeg", "JPG", "png", "PNG", "NEF", "THM", "AVI", "mp4"]
cut_filelist = [n for n in file_list if n[-3:] in file_ext]

print(cut_filelist)

for image in cut_filelist:
    current_image = Image.open(image)
    print(get_date(current_image))
