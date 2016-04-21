## List only functions are defined in List type. They are called on an object. These are in fact called methods: function dependent on objects to be called.
# These methods can mutate the list and mutating methods do not return any value. They return None.
# In contrast, methods of immutable objects does have to return values.
# Also note that sorted() and reversed() return values but they do not mutate the original object.
list1 = [0, 1, 2, 3, 4, 5, 6]
list1.append(7)  # Mutates and returns None
print list1
print list1.count(1)
list1.reverse()  # Mutates and returns None
print list1
list1.reverse()
list1.insert(7, 8)
print list1
list1.remove(8)
print list1
list1.insert(0, "isa")
print list1

print "isa" in list1
print list1.index("isa")
print 11 in list1
if 11 in list1:
    print list1.index(
        11)  # If index() cannot find element, it throws an exception. Better guard with an membership test

list1.sort()
print list1  # Note that string has gone to end. Number objects are smaller than all other objects

list1.extend([True, False])
print list1
list1.extend("isa")
print list1
list1.extend(["isa"])
print list1

print "---- pop() mutates and returs"
print list1.pop()
print list1.pop(0)
