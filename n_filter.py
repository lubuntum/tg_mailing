import re
pTypeDict = {'adult': 'Для себя', 'child': 'Для ребенка', 'empty': ''}
def filterFunc(users, filter):

    #Сортировка по типу

    if pTypeDict[filter['personType']] != '':
        users = {key: value for key, value in users.items() if value['pType'] == pTypeDict[filter['personType']]}
    else: pass
    # Сортировка по возрасту
    users = filterByAgeRange(users, filter, dataAgeKey='pAge', ageFromKey='personAgeFrom', ageToKey='personAgeTo')
    users = filterByAgeRange(users, filter, dataAgeKey='child', ageFromKey='childAgeFrom', ageToKey= 'childAgeTo' )
    #Сортировка по языкам
    languagesDict = {'english': 'Английский', 'german': 'Немецкий', 'french': 'Французский', 'spanish': 'Испанский', 'chinese': 'Китайский'}
    if len(filter['languages']) != 0:
        users = {key: value for key, value in users.items() if len(set(value['languages']).intersection(set(languagesDict[i] for i in filter['languages']))) != 0}
    else: pass

    for i in users:
        print(len(set(users[i]['languages']).intersection(set(languagesDict[i] for i in filter['languages']))) != 0)


    return users

def filterByAgeRange(users, filter, dataAgeKey, ageFromKey, ageToKey):
    if int(filter[ageFromKey]) < int(filter[ageToKey]):
        return {key: value for key, value in users.items()
                 if (len(re.findall(r'\b\d+\b', value[dataAgeKey])) == 2 and
                     (int(re.findall(r'\b\d+\b', value[dataAgeKey])[0]) <= int(filter[ageFromKey]) and
                      int(re.findall(r'\b\d+\b', value[dataAgeKey])[1]) >= int(filter[ageFromKey]) or
                      int(re.findall(r'\b\d+\b', value[dataAgeKey])[0]) <= int(filter[ageToKey]) and
                      int(re.findall(r'\b\d+\b', value[dataAgeKey])[1]) >= int(filter[ageToKey])) or
                     (int(re.findall(r'\b\d+\b', value[dataAgeKey])[0]) >= int(filter[ageFromKey]) and
                      int(re.findall(r'\b\d+\b', value[dataAgeKey])[0]) <= int(filter[ageToKey])) or
                     (len(re.findall(r'\b\d+\b', value[dataAgeKey])) == 1 and
                      (int(re.findall(r'\b\d+\b', value[dataAgeKey])[0]) >= int(filter[ageFromKey]) and
                       int(re.findall(r'\b\d+\b', value[dataAgeKey])[0]) <= int(filter[ageToKey]))))
                }
    else:
        return users