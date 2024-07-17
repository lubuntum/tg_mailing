import os
from config import UPLOAD_FILES_DIRECTORY_PATH

def createFilePaths(files):
    #--->
    #--->
    #--->
    filePaths = [file for file in files if os.path.isfile(os.path.join(UPLOAD_FILES_DIRECTORY_PATH, file))]
    filePaths = [os.path.join(UPLOAD_FILES_DIRECTORY_PATH, file) for file in filePaths]
    return filePaths


#--->#fileList = os.listdir(UPLOAD_FILES_DIRECTORY_PATH) #Скорее всего тут просто добавить переданный агрумент files
#--->#print(f'From OS -> {fileList}')
#--->#print(f'From actual files -> {files}')