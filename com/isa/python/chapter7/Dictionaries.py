## DICTIONARIES
# Only mapping type in Python
# Dictionaries are mutable mapping type. Keys can be any IMMUTABLE type. Values can be any type. Keys should be immutable though.
# It differs from JSON in the sense that keys can be any type. And it does not need to be. It just needs to produce a hash value.

## Create dictionaries
dict1 = {}
print dict1
print type(dict1)
print type(type(dict1))

dict2 = {"name": "isa", "surname": "olmez"}
print dict2

d1 = {}.fromkeys(("name", "surname"), "1")
d2 = {}.fromkeys(("a", "b"))
print d1, d2

## Access elements
print d1["name"]
print d1.get("name")
print dict2["name"]
# print d1["x"] # ERROR

## Iterate over keys
print "---- Iterate keys"
d1 = {"a": "1", "b": "2", "c": "3", "d": "4"}
for key in d1:
    print d1[key], "at key: ", key

# Identical to above. But redundant to call keys() on dictionary object inside for loop.
for key in d1.keys():
    print d1[key], "at key: ", key

## Key existence check
print "---- Membership check"
print "a" in d1
print d1.has_key("a")
print "x" in d1
print d1.has_key("x")

## Set key/values: Update and add values
print "---- Set/Add keys"
# Keys can be any type, numbers, string or others.
d1["d"] = 44  # Update
d1["e"] = 5  # Add
d1[12] = 12
print d1

# Contrast with lists
list1 = [1, 2]
list1[0] = 99  # Update
list1.append(99)
print list1

## Delete keys/values:
print "---- Delete single key"
import copy
temp = copy.deepcopy(d1)
print d1
del d1["c"]
print d1

d1 = copy.deepcopy(temp)
print "---- Delete dictionary object"
del d1
# print d1 # ERROR

d1 = copy.deepcopy(temp)
print "---- Remove and return key"
print d1
print "a,", d1.pop("a")
print d1

d1 = copy.deepcopy(temp)
print "---- Delete all keys"
d1.clear()
print d1
