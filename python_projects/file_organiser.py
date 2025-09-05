import os 
import shutil
extension_map = {
    "PDFs":['.pdf'],
    "Images":['.png','.jpeg','.jpg'],
    "TextFiles":['.txt'],
}

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder,extensions in extension_map:
        if ext in extensions:
            return folder
        return "others"
def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path,file)
        if os.path.isfile(full_path):
            get_destination_folder(file) 