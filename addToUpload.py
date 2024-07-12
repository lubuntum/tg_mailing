import sys
import threading
import sys
from werkzeug.utils import secure_filename
from config import UPLOAD_FILES_DIRECTORY_PATH
fileLock = threading.Lock()
def addToUpload(files):
    for file in files:
        #filename = secure_filename(file.filename)
        fileLock.acquire()
        try:
            savePath = str(UPLOAD_FILES_DIRECTORY_PATH + '/' + file.filename).encode()
            with open(savePath, 'wb') as f:
                file.save(f)
        finally:
            fileLock.release()