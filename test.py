from family_tree import add_child, family

print(family)
assert add_child("Queen Margret", "Bill", "Male") == True
print(family)