def filtering(data, languages, personType, ageFrom, ageTo):
    filtered = []
    languageTEMP = []
    personTypeTEMP = []

    if personType == 'adult':
        personType = 'Для себя'
    elif personType == 'child':
        personType = 'Для ребенка'

    if len(languages) != 0:
        for item in data:
            if len(item[5]) == len(languages) and set(languages).issubset(item[5]):
                languageTEMP.append(item)
    else: languageTEMP = data

    if personType != 'empty':
        for item in languageTEMP:
            if item[3] == personType:
                personTypeTEMP.append(item)
    else: personTypeTEMP = languageTEMP

    for item in personTypeTEMP:
        if int(item[4][0]) >= int(ageFrom) and int(item[4][1]) <= int(ageTo):
            filtered.append(item)

    return filtered