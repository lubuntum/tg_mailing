import re
def filterFunc(users, filter):

    # Сортировка по возрасту
    users = filterByAgeRange(users, filter, dataAgeKey='pAge', ageFromKey='personAgeFrom', ageToKey='personAgeTo')
    users = filterByAgeRange(users, filter, dataAgeKey='child', ageFromKey='childAgeFrom', ageToKey= 'childAgeTo' )

    #Сортировка по языкам
    languagesDict = {'english': 'Английский', 'german': 'Немецкий', 'french': 'Французский', 'spanish': 'Испанский', 'chinese': 'Китайский'}
    if len(filter['languages']) != 0:
        users = {key: value for key, value in users.items() if len(set(value['languages']).intersection(set(languagesDict[i] for i in filter['languages']))) != 0}
    else: pass

    return users
'''
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
'''
def extract_ages(age_str):
    return list(map(int, re.findall(r'\b\d+\b', age_str)))
def is_within_range(user_ages, filter_from, filter_to):
    if len(user_ages) == 2:
        start, end = user_ages
        return (start <= filter_from <= end) or (start <= filter_to <= end) or (filter_from <= start <= filter_to)
    elif len(user_ages) == 1:
        age = user_ages[0]
        return filter_from <= age <= filter_to
    return False


def filterByAgeRange(users, filter, dataAgeKey, ageFromKey, ageToKey):
    filter_from = int(filter[ageFromKey])
    filter_to = int(filter[ageToKey])

    if filter_from >= filter_to:
        return users

    return {
        key: value for key, value in users.items()
        if is_within_range(extract_ages(value[dataAgeKey]), filter_from, filter_to)
    }