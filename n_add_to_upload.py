import threading
import time

from config import UPLOAD_FILES_DIRECTORY_PATH

fileLock = threading.Lock()

def addToUpload(files):
    for file in files:
        #--->
        fileLock.acquire()
        try:
            file.filename = f'{file.filename}_{int(time.time()*1000)}'
            savePath = str(UPLOAD_FILES_DIRECTORY_PATH + '/' + file.filename).encode()
            with open(savePath, 'wb') as f:
                file.save(f)
        finally:
            fileLock.release()


#import sys
#from werkzeug.utils import secure_filename
#--->#filename = secure_filename(file.filename)