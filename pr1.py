a= {}
print(type(a))
# this syntax will create an empty dictionary and not an empty set
# An empty set is created using the following syntax:
b = set()
print(type(b))
# adding values to empty set
b.add(4)
b.add(5)
b.add(5)# adding a value repeatedly cannot change a set
# b.add({3:4}) we cannot add lists and dictionaries in sets because they are hashable and their contents are changeable
b.add((3,4,5))
print(b)
# Length of the set
print(len(b))
# Removal of an item in sets
b.remove(4)#remove 4 from setb
print(b)
print(b.pop())# Removes an arbitarary element from the set ans returns the element removed
print(b)
#b.clear()#Empties the set
#print(b)
b.union({7,8,9})
print(b)
