import threading
from datetime import datetime

from flask import Flask, render_template, request, jsonify
from db_get_data import getDataFromDB
from data_filter import filtering
from tg_bot_mailing import sendMessageWithFiles, sendMessageWithoutFiles

from clearUpload import clearUpload
from addToUpload import addToUpload
from createFilePaths import createFilePaths

app = Flask(__name__)

originUserData = getDataFromDB('/root')
recipientsList = []

#Aboba
#1234

#---------
#Выполняется при загрузке и перезагрузке страницы!
#Очищается список получателей RecipientsList
#Очищается папка с файлами которые были загружены при прошлой отпраке рассылки
#Загружается основной шаблон (app.html)
#---------
@app.route('/')
def index():
    recipientsList.clear()
    clearUpload()
    return render_template('app.html', data=originUserData)


#---------
#Выполняется при применении фильтрации или сбросе фильтрации (Нажатие на кнопку "Применить фильтрацию" и "Сбросить фильтрацию")
#На клиенте выполняется AJAX запрос и сервер получает все настройки фильтрации (Тип, Диапазон возрастов, Языки)
#Далее в контейнер с таблицей загружается новый шаблон (datatable.html) и туда подгружаются фильтрованые данные
#Также при выполнении фильтрации, очищается список получателей RecipientsList
#---------
@app.route('/filter_and_refresh_data', methods=['POST'])
def getFilterData():
    recipientsList.clear()
    return render_template('datatable.html', data=filtering(originUserData, request.json['checkboxInput'], request.json['selectInput'], request.json['fromTextInput'], request.json['toTextInput']))


#---------
#Выполняется при нажатии на чекбокс в шапке таблицы
#На клиенте выполняется AJAX запрос и сервер получает ID ВСЕХ пользователей текущей таблицы с колонки ID
#Полученые данные сохраняются в список RecipientsList который в дальнешем используется для отправки сообщений
#Если пользователь убирает галочку с чекбокса то и соответственно и удалаюятся ID пользователей из RecipientsList по вышеописаному примеру
#---------
@app.route('/get_all_data', methods=['POST'])
def getAllDataFromPage():
    idList = request.json['idList']
    checked = int(request.json['checked'])

    if checked != 0:
        for i in idList:
            recipientsList.append(int(i['id']))
    elif checked != 1:
        recipientsList.clear()
    print(f'From all {recipientsList}')
    return jsonify('_suc: /get_all_data', recipientsList)


#---------
#Выполняется при нажатии на любой чекбокс в строке с элементом таблицы
#На клиенте выполняется AJAX запрос и сервер получает ID пользователя с колонки ID
#Полученые данные сохраняются в список RecipientsList который в дальнешем используется для отправки сообщений
#Если пользователь убирает галочку с чекбокса то и соответственно и удалаюятся ID пользователей из RecipientsList по вышеописаному примеру
#---------
@app.route('/get_data', methods=['POST'])
def getDataFromPage():
    id = int(request.json['id'])
    checked = int(request.json['checked'])

    if id != '' and checked != 0:
        recipientsList.append(id)
    elif id != '' and checked != 1:
        recipientsList.remove(id)
    print(recipientsList)
    return jsonify('_suc: /get_data', recipientsList)



#---------
#Выполняется при отправке сообщения (Нажатие на кнопку "Отправить сообщение")
#На клиенте выполняется AJAX запрос и сервер получает текст рассылки и все файлы которые загрузил пользователь
#Файлы сохраняются в папке UPLOAD_FILES и находятся там до новой отправки рассылки, потом они удаляются
#---------
@app.route('/send_message', methods=['POST'])
def sendMessage():
    addToUpload(request.files.getlist('files'))

    sendMessageToUsers(request.form.get('messageText'), request.files.getlist('files'), recipientsList)
    return jsonify('_suc: /send_message. Сообщение отправлено!', recipientsList)

def sendMessageToUsers(messageText, files, pickedUsers):#Только данные

    if len(pickedUsers) == 0:
        return '_war: /send_message. Список пользователей пуст!'
    #Передаем только имена файлов которые нужно отправить из всех
    filePaths = createFilePaths([file.filename for file in files])

    if len(filePaths) > 0:
        sendMessageWithFiles(pickedUsers, messageText, filePaths)
    else:
        sendMessageWithoutFiles(pickedUsers, messageText)
    #После отправки можно реализовать метод для удаление текущих files ибо они больше не нудны
@app.route('/delay_message', methods = ['POST'])
def delayMessage():
    addToUpload(request.files.getlist('files'))
    delayMessageTimer(request.form.get('date'), request.form.get('time'),
                      request.form.get('messageText'), request.files.getlist('files'), pickedUsers=recipientsList)
    return jsonify('_suc: /delay_message. Отложено!', recipientsList)

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