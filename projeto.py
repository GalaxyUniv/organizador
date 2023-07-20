import os
import shutil

fromdir = "C:/Users/Eliana/Downloads/"
todir = "C:/Users/Eliana/Documents/"

listoffiles =os.listdir(fromdir)
print(listoffiles)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    print(name)
    print(extension)
    if extension in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = fromdir + filename
        path2 = todir + "Downloads"
        path3 = todir + "Downloads/" + filename
        if os.path.exists(path2):
            print("movendo", filename)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movendo", filename)
            shutil.move(path1,path3)
