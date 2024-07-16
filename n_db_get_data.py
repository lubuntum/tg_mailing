import firebase_admin
from firebase_admin import db, credentials
from config import SERVICE_ACCOUNT_KEY_PATH, DATABASE_URL, DATABASE_ROOT

credentials = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(credentials, {'databaseURL': DATABASE_URL})

def getDataFromDB(path):
    reference = db.reference(path)
    users = reference.get()
    #OLD \/ \/ \/
    # for i in usersDataRaw:
    #     usersDataFormat.append([usersDataRaw[i]['userId'],
    #                             str((usersDataRaw[i]['name'] if 'Не указан' not in (usersDataRaw[i]['name']) else '') + '\n' + (usersDataRaw[i]['surName'] if 'Не указан' not in (usersDataRaw[i]['surName']) else '')),
    #                             usersDataRaw[i]['phone'],
    #                             usersDataRaw[i]['personType'],
    #                             list(map(int, usersDataRaw[i]['age'].split('-'))),
    #                             usersDataRaw[i]['language'] if 'Не указано' not in (usersDataRaw[i]['language']) else 'Не указано',
    #                             usersDataRaw[i]['knowledge'] if 'Не указано' not in (usersDataRaw[i]['knowledge']) else 'Не указано',
    #                             usersDataRaw[i]['trainingPurpose'] if 'Не указано' not in (usersDataRaw[i]['trainingPurpose']) else 'Не указано',
    #                             str(usersDataRaw[i]['surveyDate'] + '\n' + usersDataRaw[i]['surveyTime'])])
    return users

getDataFromDB(DATABASE_ROOT)