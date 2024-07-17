import re

def filterFunc(users, filter):

    #Сортировка по типу
    pTypeDict = {'adult': 'Для себя', 'child': 'Для ребенка', 'empty': ''}
    if pTypeDict[filter['personType']] != '':
        users = {key: value for key, value in users.items() if value['pType'] == pTypeDict[filter['personType']]}
    else: pass

    #Сортировка по возрасту
    if int(filter['personAgeFrom']) < int(filter['personAgeTo']):
        users = {key: value for key, value in users.items()
                 if (len(re.findall(r'\b\d+\b', value['pAge'])) == 2 and
                     (int(re.findall(r'\b\d+\b', value['pAge'])[0]) <= int(filter['personAgeFrom']) and
                      int(re.findall(r'\b\d+\b', value['pAge'])[1]) >= int(filter['personAgeFrom']) or
                      int(re.findall(r'\b\d+\b', value['pAge'])[0]) <= int(filter['personAgeTo']) and
                      int(re.findall(r'\b\d+\b', value['pAge'])[1]) >= int(filter['personAgeTo'])) or
                     (int(re.findall(r'\b\d+\b', value['pAge'])[0]) >= int(filter['personAgeFrom']) and
                      int(re.findall(r'\b\d+\b', value['pAge'])[0]) <= int(filter['personAgeTo'])) or
                     (len(re.findall(r'\b\d+\b', value['pAge'])) == 1 and
                      (int(re.findall(r'\b\d+\b', value['pAge'])[0]) >= int(filter['personAgeFrom']) and
                       int(re.findall(r'\b\d+\b', value['pAge'])[0]) <= int(filter['personAgeTo']))))
                }
    else: pass

    #Сортировка по языкам
    languagesDict = {'english': 'Английский', 'german': 'Немецкий', 'french': 'Французский', 'spanish': 'Испанский', 'chinese': 'Китайский'}
    if len(filter['languages']) != 0:
        users = {key: value for key, value in users.items() if set(value['languages']) == set(languagesDict[i] for i in filter['languages'])}
    else: pass


    return users