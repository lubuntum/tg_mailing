import re

def filterFunc(users, filter):

    #Сортировка по типу
    pTypeDict = {'adult': 'Для себя', 'child': 'Для ребенка', 'empty': ''}
    if pTypeDict[filter['personType']] != '':
        users = {key: value for key, value in users.items() if value['pType'] == pTypeDict[filter['personType']]}
    else: pass

    #Сортировка по возрасту
    if filter['personAgeFrom'] < filter['personAgeTo']:
        users = {key: value for key, value in users.items()
                if len(re.findall(r'\b\d+\b', value['pAge'])) == 2 #Если в базе возраст указан так: "от 20 до 25 лет" - пример. Типа 2 целочисленных
                and ((int(filter['personAgeFrom']) <= int(re.findall(r'\b\d+\b', value['pAge'])[0]) <= int(filter['personAgeTo'])) # И --- 1-ое целочисленное больше числа ОТ и меньше числа ДО
                    or (int(filter['personAgeFrom']) <= int(re.findall(r'\b\d+\b', value['pAge'])[1]) <= int(filter['personAgeTo']))) # ИЛИ --- 2-ое целочисленное больше числа ОТ и меньше числа ДО
                    or len(re.findall(r'\b\d+\b', value['pAge'])) == 1 #Если в базе возраст указан так: "страше 45" - пример. Типа 1 целочисленое
                    and (int(filter['personAgeFrom']) <= int(re.findall(r'\b\d+\b', value['pAge'])[0]) <= int(filter['personAgeTo']))} # И --- целочисленное больше числа ОТ и меньше чилса ДО
    else: pass

    #Сортировка по языкам
    languagesDict = {'english': 'Английский', 'german': 'Немецкий', 'french': 'Французский', 'spanish': 'Испанский', 'chinese': 'Китайский'}
    if len(filter['languages']) != 0:
        users = {key: value for key, value in users.items() if set(value['languages']) == set(languagesDict[i] for i in filter['languages'])}
    else: pass

    return users