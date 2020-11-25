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


def isMember(name):
    return name in family


def isMale(name):
    return isMember(
        name) and 'male' in family[name] and family[name]['male'] == True


def add_child(mother, name, gender):
    if isMale(mother):
        return False

    motherDict = family[mother]
    if 'children' not in motherDict:
        motherDict['children'] = []

    motherDict['children'].append(name)

    tmp = {}
    if gender.lower() == 'male':
        tmp['male'] = True

    family[name] = tmp
    return True


def add_spouse(name, spouse):
    if isMember(spouse):
        return False

    if 'spouse' in family[name]:
        return False

    family[name]['spouse'] = spouse
    family[spouse] = {'spouse': name}
    if not isMale(name):
        family[spouse]['male'] = True

    return True


def get_spouse(name):
    return family[name]['spouse']


def get_relationship(name, relationship):
    return {'spouse'.lower(): get_spouse}[relationship.lower()](name)
