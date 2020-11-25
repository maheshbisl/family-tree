from family_tree import add_child, family, get_relationship, add_spouse
import json


def print_family():
    print(json.dumps(family, sort_keys=True, indent=2))


assert add_child("Queen Margret", "Bill", "Male") == True
assert add_child("Queen Margret", "Bill", "Male") == False
assert add_child("Queen Margret", "Charlie", "Male") == True
assert add_child("Queen Margret", "Percy", "Male") == True
assert add_child("Queen Margret", "Ronald", "Male") == True
assert add_child("Queen Margret", "Ginerva", "Female") == True

assert get_relationship("Queen Margret", "Spouse") == "King Arthur"

assert add_spouse("Bill", "Flora") == True
assert add_spouse("Bill", "Flora") == False
assert add_spouse("Bill", "Julia") == False
assert add_spouse("Percy", "Audrey") == True
assert add_spouse("Ronald", "Helen") == True
assert add_spouse("Ginerva", "Harry") == True

assert get_relationship("Flora", "Spouse") == "Bill"
assert get_relationship(
    "Bill", "Siblings") == ['Charlie', 'Ginerva', 'Percy', 'Ronald']
assert get_relationship("Bill", "Sisters") == ['Ginerva']
assert get_relationship("Bill", "Brothers") == ['Charlie', 'Percy', 'Ronald']

assert get_relationship("Queen Margret", "Daughters") == ['Ginerva']
assert get_relationship("Queen Margret",
                        "Sons") == ['Bill', 'Charlie', 'Percy', 'Ronald']

assert add_child("Flora", "Louis", "Male") == True
assert add_child("Flora", "Victoire", "Female") == True
assert add_child("Flora", "Dominique", "Female") == True

assert add_child("Audrey", "Molly", "Female") == True
assert add_child("Audrey", "Lucy", "Female") == True

assert add_child("Ginerva", "James", "Male") == True
assert add_spouse('James', 'Darcy') == True
assert add_child("Darcy", "William", "Male") == True
assert add_child("Ginerva", "Albus", "Male") == True
assert add_spouse("Albus", "Alice") == True
assert add_child("Alice", "Ron", "Male") == True
assert add_child("Alice", "Ginny", "Female") == True
assert add_child("Ginerva", "Lily", "Female") == True

assert add_child("Helen", "Hugo", "Male") == True
assert add_child("Helen", "Rose", "Female") == True
assert add_spouse("Rose", "Malfoy") == True
assert add_child("Rose", "Draco", "Male") == True
assert add_child("Rose", "Aster", "Female") == True

assert add_child("Victoire", "Rameus", "Male") == True
assert add_spouse("Victoire", "Ted") == True

assert get_relationship('Louis',
                        'Paternal-Uncles') == ['Charlie', 'Percy', 'Ronald']
assert get_relationship('Louis', 'Paternal-Aunts') == ['Ginerva']

assert get_relationship('Rameus', 'Maternal-Uncles') == ['Louis']
assert get_relationship('Rameus', 'Maternal-Aunts') == ['Dominique']

assert get_relationship('Ted', 'Brothers-In-Law') == ['Louis']
assert get_relationship('Louis', 'Brothers-In-Law') == ['Ted']

assert get_relationship('Dominique', 'Brothers-In-Law') == ['Ted']
assert get_relationship('Ted', 'Sisters-In-Law') == ['Dominique']

assert get_relationship(
    'James', "Maternal-Uncles") == ["Bill", "Charlie", "Percy", "Ronald"]
assert get_relationship("Lily", "Sisters-In-Law") == ["Alice", "Darcy"]
assert get_relationship("William", "Paternal-Uncles") == ["Albus"]
assert get_relationship("William", "Paternal-Aunts") == ["Lily"]
assert get_relationship("Darcy", "Brothers-In-Law") == ["Albus"]
assert get_relationship(
    "Helen", "Brothers-In-Law") == ["Bill", "Charlie", "Harry", "Percy"]
