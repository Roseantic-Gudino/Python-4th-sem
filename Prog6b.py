import os
import sys
import pathlib
import zipfile

dirName= input("Enter Directory name that you want to backup: ")

if not os.path.isdir(dirName):
    print("Directory ", dirName, " doesnt exists")
    sys.exit(0)

curDirectory=pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", mode="w") as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path) #, arcname=file_path.relative_to(curDirectory))
        
if os.path.isfile("myZip.zip"):
    print("Archive ", "myZip.zip", " created succesfully")
else:
    print("Error in creating zip archive")
