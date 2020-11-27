family = {
    "King-Arthur": {
        "male": True,
        "spouse": "Queen-Margret"
    },
    "Queen-Margret": {
        "spouse": "King-Arthur",
        "children": []  # Names of the children
    }
}


def isMember(name):
    return name in family


def get_member(name):
    return family[name] if isMember(name) else None


def isMale(name):
    member = get_member(name)
    return member and 'male' in member and member['male'] == True


def isFemale(name):
    return not isMale(name)


def isMarried(name):
    member = get_member(name)
    return member and 'spouse' in member


def hasMother(name):
    member = get_member(name)
    return member and 'mother' in member


def get_mother(name):
    return get_member(name)['mother'] if hasMother(name) else ""


def get_father(name):
    mother = get_member(get_mother(name))
    return mother['spouse'] if mother else ""


def get_children(name):
    member = get_member(name)
    if not member:
        return []

    if isMale(name) and isMarried(name):
        return get_children(member['spouse'])

    return member['children'] if 'children' in member else []


def hasChildren(name):
    return get_childern(name) != []


def add_child(mother, name, gender):
    motherDict = get_member(mother)

    if isMember(name) or not motherDict or isMale(mother):
        return False

    motherDict['children'] = get_children(mother) + [name]

    family[name] = {'mother': mother, 'male': gender.lower() == 'male'}
    return True


def add_spouse(name, spouse):
    member = get_member(name)
    if not member or isMember(spouse) or isMarried(name) or isMarried(spouse):
        return False

    member['spouse'] = spouse
    family[spouse] = {'spouse': name, 'male': not isMale(name)}
    return True


def get_spouse(name):
    member = get_member(name)
    return member['spouse'] if member and isMarried(name) else ""


def get_siblings(name):
    return [x for x in get_children(get_mother(name)) if x != name]


def get_daughters(name):
    return [x for x in get_children(name) if isFemale(x)]


def get_sons(name):
    return [x for x in get_children(name) if isMale(x)]


def get_brothers(name):
    return [x for x in get_sons(get_mother(name)) if x != name]


def get_sisters(name):
    return [x for x in get_daughters(get_mother(name)) if x != name]


def get_paternal_uncles(name):
    father = get_father(name)
    father_mother = get_mother(father)
    return [x for x in get_sons(father_mother) if x != father]


def get_paternal_aunts(name):
    father = get_father(name)
    father_mother = get_mother(father)
    return get_daughters(father_mother)


def get_maternal_uncles(name):
    return get_sons(get_mother(get_mother(name)))


def get_maternal_aunts(name):
    mother = get_mother(name)
    return [x for x in get_daughters(get_mother(mother)) if x != mother]


def get_sisters_in_law(name):
    spouse = get_spouse(name)
    return get_sisters(spouse) + [
        get_spouse(x)
        for x in get_brothers(name) + get_brothers(spouse) if isMarried(x)
    ]


def get_brothers_in_law(name):
    spouse = get_spouse(name)
    return get_brothers(spouse) + [
        get_spouse(x)
        for x in get_sisters(name) + get_sisters(spouse) if isMarried(x)
    ]


def get_uncles(name):
    return get_paternal_uncles(name) + get_maternal_uncles(name)


def get_aunts(name):
    return get_paternal_aunts(name) + get_maternal_aunts(name)


def get_siblings_in_law(name):
    return get_brothers_in_law(name) + get_sisters_in_law(name)


def get_relationship(name, relationship):
    ret = {
        'mother': get_mother,
        'father': get_father,
        'spouse': get_spouse,
        'siblings': get_siblings,
        'daughters': get_daughters,
        'sons': get_sons,
        'brothers': get_brothers,
        'sisters': get_sisters,
        'paternal-uncles': get_paternal_uncles,
        'paternal-aunts': get_paternal_aunts,
        'uncles': get_uncles,
        'maternal-uncles': get_maternal_uncles,
        'maternal-aunts': get_maternal_aunts,
        'aunts': get_aunts,
        'sisters-in-law': get_sisters_in_law,
        'brothers-in-law': get_brothers_in_law,
        'siblings-in-law': get_siblings_in_law
    }[relationship.lower()](name)

    if not isinstance(ret, list):
        return ret

    ret.sort()
    return ret


if __name__ == '__main__':
    import sys
    for line in open(sys.argv[1], "r").readlines():
        para = line.split()

        if para[0].lower() == 'add_child':
            if add_child(para[1], para[2], para[3]):
                print("CHILD_ADDED")
            else:
                print("CHILD_NOT_ADDED")

        elif para[0].lower() == 'add_spouse':
            if add_spouse(para[1], para[2]):
                print("SPOUSE_ADDED")
            else:
                print("SPOUSE_NOT_ADDED")

        elif para[0].lower() == 'get_relationship':
            if para[2].lower() == 'spouse':
                print(get_relationship(para[1], para[2]))
            else:
                print(" ".join(get_relationship(para[1], para[2])))
