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

def isMarried(name):
		member = get_member(name)
		return member and 'spouse' in member
  
def hasMother(name):
    member = get_member(name)
    return member and 'mother' in member

def get_mother(name):
    return get_member(name)['mother'] if hasMother(name) else ""
    
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

    motherDict['children'] = get_children(mother) + [ name ]

    family[name] = {'mother': mother, 'male': gender.lower() == 'male' }
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
    if not hasMother(name):
      return []
    return list(filter(lambda x: x != name, get_children(get_mother(name))))

def get_daughters(name):
    return list(
        filter(lambda x: 'male' not in family[x] or family[x]['male'] != True,
               get_children(name)))

def get_sons(name):
    return list(
        filter(lambda x: 'male' in family[x] and family[x]['male'] == True,
               get_children(name)))


def get_brothers(name):
    if not hasMother(name):
      return []

    member = get_member(name)
    bros = get_sons(member['mother'])
    if name in bros:
        bros.remove(name)
    return bros


def get_sisters(name):
    if not hasMother(name):
      return []

    member = get_member(name)
    sises = get_daughters(member['mother'])
    if name in sises:
        sises.remove(name)
    return sises


def get_paternal_uncles(name):
    if not isMember(name):
        return []

    member = family[name]
    if 'mother' not in member:
        return []

    mother = family[member['mother']]
    if 'spouse' not in mother:
        return []

    father = family[mother['spouse']]
    if 'mother' not in father:
        return []

    uncles = get_sons(father['mother'])
    uncles.remove(mother['spouse'])
    return uncles


def get_paternal_aunts(name):
    if not isMember(name):
        return []

    member = family[name]
    if 'mother' not in member:
        return []

    mother = family[member['mother']]
    if 'spouse' not in mother:
        return []

    father = family[mother['spouse']]
    if 'mother' not in father:
        return []

    tmp = get_daughters(father['mother'])
    return tmp


def get_maternal_uncles(name):
    if not isMember(name):
        return []

    member = family[name]
    if 'mother' not in member:
        return []

    mother = family[member['mother']]
    if 'mother' not in mother:
        return []

    uncles = get_sons(mother['mother'])
    return uncles


def get_maternal_aunts(name):
    if not isMember(name):
        return []

    member = family[name]
    if 'mother' not in member:
        return []

    mother = family[member['mother']]
    if 'mother' not in mother:
        return []

    tmp = get_daughters(mother['mother'])
    tmp.remove(member['mother'])
    return tmp


def get_sisters_in_law(name):
    if not isMember(name):
        return []

    member = family[name]
    sisters_in_law = []
    brothers = get_brothers(name)

    if 'spouse' in member:
        sisters_in_law = get_sisters(member['spouse'])
        brothers.extend(get_brothers(member['spouse']))
    for b in brothers:
        bro = family[b]
        if 'spouse' in bro:
            sisters_in_law.append(bro['spouse'])

    return sisters_in_law


def get_brothers_in_law(name):
    if not isMember(name):
        return []

    member = family[name]
    sisters = get_sisters(name)
    brothers_in_law = []

    if 'spouse' in member:
        brothers_in_law = get_brothers(member['spouse'])
        sisters.extend(get_sisters(member['spouse']))

    for s in sisters:
        sis = family[s]
        if 'spouse' in sis:
            brothers_in_law.append(sis['spouse'])

    return brothers_in_law


def get_relationship(name, relationship):
    ret = {
        'spouse': get_spouse,
        'siblings': get_siblings,
        'daughters': get_daughters,
        'sons': get_sons,
        'brothers': get_brothers,
        'sisters': get_sisters,
        'paternal-uncles': get_paternal_uncles,
        'paternal-aunts': get_paternal_aunts,
        'maternal-uncles': get_maternal_uncles,
        'maternal-aunts': get_maternal_aunts,
        'sisters-in-law': get_sisters_in_law,
        'brothers-in-law': get_brothers_in_law
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
