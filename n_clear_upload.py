import os
from config import UPLOAD_FILES_DIRECTORY_PATH

def clearUpload():
    fileList = os.listdir(UPLOAD_FILES_DIRECTORY_PATH)
    for i in fileList:
        file = os.path.join(UPLOAD_FILES_DIRECTORY_PATH, i)
        os.remove(file)