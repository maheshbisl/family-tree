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

    tmp = {'mother': mother}
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
    member =  family[name]
    if 'spouse' not in member:
      return None
    
    return member['spouse']


def get_siblings(name):
    member =  family[name]
    if 'mother' not in member:
       return []
    
    mother = family[member['mother']]
    if 'children' not in mother:
       return []
      
    ret = list(filter(lambda x: x != name, mother['children']))
    return ret

  
def get_daughters(name):
    mother = family[name]
    if isMale(name) and 'spouse' in mother:
      mother = family[family[name]['spouse']]
    
    ret = list(filter(lambda x: 'male' not in family[x] or family[x]['male'] != True, mother['children']))
    return ret


def get_sons(name):
    mother = family[name]
    if isMale(name)  and 'spouse' in mother:
      mother = family[mother['spouse']]
      
    ret = list(filter(lambda x: 'male' in family[x] and family[x]['male'] == True, mother['children']))
    return ret
  

def get_brothers(name):
    member = family[name]
    if 'mother' not in member:
      return []
    
    bros = get_sons(member['mother'])
    if name in bros:
      bros.remove(name)
    return bros


def get_sisters(name):
    member = family[name]
    if 'mother' not in member:
       return []
      
    sises = get_daughters(member['mother'])
    if name in sises:
        sises.remove(name)
    return sises
  

def get_paternal_uncles(name):
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
    member = family[name]
    if 'mother' not in member:
      return []
    
    mother = family[member['mother']]
    if 'spouse' not in mother:
      return []
    
    father =family[mother['spouse']]
    if 'mother' not in father:
      return []
    
    tmp = get_daughters(father['mother'])
    return tmp                       

 
def get_maternal_uncles(name):
    member = family[name]
    if 'mother' not in member:
      return []
    
    mother = family[member['mother']]
    if 'mother' not in mother:
      return []
    
    uncles = get_sons(mother['mother'])
    return uncles                           

  
def get_maternal_aunts(name):
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
    sisters_in_law = []
    
    try:
      sisters_in_law = get_sisters(family[name]['spouse'])
    except:
      pass
    
    brothers = []
    try:
      brothers = get_brothers(name)
    except:
      pass
    
    for bro in brothers:
       try:
          sisters_in_law.append(family[bro]['spouse'])
       except:     
          pass
     
    return sisters_in_law

  
def get_brothers_in_law(name):
    brothers_in_law = []
    if 'spouse' in family[name]:
      brothers_in_law = get_brothers(family[name]['spouse'])
    sisters = get_sisters(name)

    for sis in sisters:
       try:
          brothers_in_law.append(family[sis]['spouse'])
       except Exception as e:     
          pass
        
    return brothers_in_law  
 

  
def get_relationship(name, relationship):
    return {
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
