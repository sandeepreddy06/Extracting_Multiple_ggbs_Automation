import os
import shutil
from itertools import chain
from zipfile import ZipFile
import zipfile
import string

ROOT_FOLDER = "D:/AssetExtraction/"

def find_E_files(path):
    x = os.listdir(path)
    print(x)
    for files in x:
        if files.endswith(".ggb"):
            print(files)
            with ZipFile(path+files, 'r') as zipObj:
                zipObj.extractall(path+"E_"+files+"\\")
    print("---------------x Extraction Process Completed x----------------")

find_E_files(ROOT_FOLDER)

y=[]
def extract_files(path):
    os.mkdir(path+"New/", mode=0o777,dir_fd=None)
    f=os.listdir(path)
    for fil in f:
        if fil.startswith("E"):
            y=[fil]
            for x in y:
                os.mkdir(path+"New/"+x+"/", mode=0o777,dir_fd=None)
                MAIN=path+"New/"+x+"/"
                DIRS=path+fil
                print(DIRS)
                for root, subdirs, files in os.walk(DIRS):
                    for file in files:
                        print(file)
                        paths = os.path.join(root, file)
                        print(paths)
                        shutil.copy(paths, MAIN)
            
    print("---------------x Extraction Completed x----------------")

extract_files(ROOT_FOLDER)