from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_bcrypt import Bcrypt

import json
import threading
from datetime import datetime

from config import SECRET_KEY

from auth.auth_user import authUser
from n_db_get_data import getDataFromDB
from n_filter import filterFunc
from n_add_to_upload import addToUpload
from n_create_file_paths import *
from tg_bot_mailing import sendMessageWithFiles, sendMessageWithoutFiles

app = Flask(__name__)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect('/login')
    username = session['username']
    originUserData = getDataFromDB('/root')
    return render_template('n_app.html', dataUsers = originUserData, username = username)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if authUser(username, password):
        return redirect('/')
    return render_template('login.html', errorActive='active')


@app.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/login')


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
    #print(f'{messageText}, {files}, {date}, {time}')
    timer = threading.Timer(delaySec, sendMessageToUsers, args=[messageText, files, pickedUsers])
    timer.start()


if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    app.run()