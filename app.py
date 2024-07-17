from flask import Flask, render_template, request, jsonify

import json
import threading
from datetime import datetime

from n_db_get_data import getDataFromDB
from n_filter import filterFunc

from n_clear_upload import clearUpload
from n_add_to_upload import addToUpload
from n_create_file_paths import *

from tg_bot_mailing import sendMessageWithFiles, sendMessageWithoutFiles

app = Flask(__name__)


@app.route('/')
def index():
    originUserData = getDataFromDB('/root')
    return render_template('n_app.html', dataUsers = originUserData)




@app.route('/filter_data', methods=['POST'])
def getFilterData():
    originUserData = getDataFromDB('/root')
    if request.json['filterType'] == 0:
        requestData = {
            'personType': request.json['personType'],
            'personAgeFrom': request.json['personAgeFrom'],
            'personAgeTo': request.json['personAgeTo'],
            'languages': request.json['languages']
        }
        filteredUserData = filterFunc(originUserData, requestData)
        return render_template('n_table.html', dataUsers = filteredUserData)
    else:
        return render_template('n_table.html', dataUsers = originUserData)




@app.route('/send_message', methods=['POST'])
def sendMessage():
    addToUpload(request.files.getlist('files'))
    sendMessageToUsers(request.form.get('message'), 
                       request.files.getlist('files'),
                       json.loads(request.form.get('ids')))
    return jsonify('_success: /send_message. Сообщение отправлено!')




@app.route('/delay_message', methods = ['POST'])
def delayMessage():
    addToUpload(request.files.getlist('files'))
    delayMessageTimer(request.form.get('date'), 
                      request.form.get('time'),
                      request.form.get('message'), 
                      request.files.getlist('files'),
                      json.loads(request.form.get('ids')))
    return jsonify('_success: /delay_message. Сообщение отложено!')




def sendMessageToUsers(messageText, files, pickedUsers):
    if len(pickedUsers) == 0:
        return '_warning: /send_message. Список пользователей пуст!'
    #Передаем только имена файлов которые нужно отправить из всех
    filePaths = createFilePaths([file.filename for file in files])
    if len(filePaths) > 0:
        sendMessageWithFiles(pickedUsers, messageText, filePaths)
        clearFiles(filePaths)
    else:
        sendMessageWithoutFiles(pickedUsers, messageText)
    #После отправки можно реализовать метод для удаление текущих files ибо они больше не нудны




def delayMessageTimer(date, time, messageText, files, pickedUsers):
    fullDateStr = f'{date} {time}'
    fullDate = datetime.strptime(fullDateStr, '%d.%m.%Y %H:%M')
    currentDate = datetime.now()
    delaySec = (fullDate - currentDate).total_seconds()
    #Поставить таймер
    print(f'{messageText}, {files}, {date}, {time}')
    timer = threading.Timer(delaySec, sendMessageToUsers, args=[messageText, files, pickedUsers])
    timer.start()


if __name__ == "__main__":
    app.run()