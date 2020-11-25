family = {
    "King Arthur": {
        "male": True,
        "spouse": "Queen Margret"
    },
    "Queen Margret": {
        "spouse": "King Arthur",
        "children": []  # Names of the children
    }
}


def isMale(name):
    if name not in family:
        return False

    if 'male' in family[name] and family[name]['male'] == True:
        return True

    return False


def add_child(mother: str, name: str, gender: str):
    if isMale(mother):
        return False, mother + " is not a mother"

    motherDict = family[mother]
    if 'children' not in motherDict:
        motherDict['children'] = []

    motherDict['children'].append(name)

    tmp = {}
    if gender.lower() == 'male':
        tmp['male'] = True

    family[name] = tmp
    #     print(family)
    return True
