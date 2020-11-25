from family_tree import add_child, family, get_relationship, add_spouse
import json


def print_family():
    print(json.dumps(family, sort_keys=True, indent=2))


# print(family)
assert add_child("Queen Margret", "Bill", "Male") == True
# print_family()
assert get_relationship("Queen Margret", "Spouse") == "King Arthur"

assert add_spouse("Bill", "Flora") == True
print_family()
assert get_relationship("Flora", "Spouse") == "Bill"
