import os
import shutil

from_dir = "C:/Users/viswa/OneDrive/Desktop/Image_files"
to_dir = "C:/Users/viswa/OneDrive/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files_name in list_of_files:
    name,extention = os.path.splitext(files_name)
    print(name)
    print(extention)

    if extention == "":
        continue
    if extention in [".txt", ".doc",".docx",".pdf"]:
        path1 = from_dir + '/' + files_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + files_name
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)    


