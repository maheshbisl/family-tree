from family_tree import add_child, family, get_relationship, add_spouse
import json


def print_family():
    print(json.dumps(family, sort_keys=True, indent=2))


assert add_child("Queen Margret", "Bill", "Male") == True
assert add_child("Queen Margret", "Charlie", "Male") == True
assert add_child("Queen Margret", "Percy", "Male") == True
assert add_child("Queen Margret", "Ronald", "Male") == True
assert add_child("Queen Margret", "Ginerva", "Female") == True

assert get_relationship("Queen Margret", "Spouse") == "King Arthur"

assert add_spouse("Bill", "Flora") == True
assert add_spouse("Percy", "Audrey") == True
assert add_spouse("Ronald", "Helen") == True
assert add_spouse("Ginerva", "Harry") == True

assert get_relationship("Flora", "Spouse") == "Bill"
assert get_relationship("Bill", "Siblings") == ['Charlie', 'Percy', 'Ronald', 'Ginerva']
assert get_relationship("Bill", "Sisters") == ['Ginerva']
assert get_relationship("Bill", "Brothers") == ['Charlie', 'Percy', 'Ronald']

assert get_relationship("Queen Margret", "Daughters") == [ 'Ginerva' ]
assert get_relationship("Queen Margret", "Sons") == [ 'Bill', 'Charlie', 'Percy', 'Ronald']

# Flora's children
assert add_child("Flora", "Louis", "Male") == True
assert add_child("Flora", "Victoire", "Female") == True
assert add_child("Flora", "Dominique", "Female") == True

# Victoire's children
assert add_child("Victoire", "Rameus", "Male") == True

assert get_relationship('Louis', 'Paternal-Uncles') == ['Charlie', 'Percy', 'Ronald']
assert get_relationship('Louis', 'Paternal-Aunts') == ['Ginerva']

assert get_relationship('Rameus', 'Maternal-Uncles') == ['Louis']
assert get_relationship('Rameus', 'Maternal-Aunts') == ['Dominique']

assert get_relationship('Ted', 'Brothers-In-Law') == ['Louis']
assert get_relationship('Louis', 'Brothers-In-Law') == ['Ted']

assert get_relationship('Dominique', 'Brothers-In-Law') == ['Ted']
assert get_relationship('Ted', 'Sisters-In-Law') == ['Dominique']


