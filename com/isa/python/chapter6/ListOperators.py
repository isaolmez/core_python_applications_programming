## 1. Standard Type Operators: applied to most types.

# List comparison compares the elements from index 0 until the tie breaks and one element of one list is smaller/greater than other's.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print list1 < list2

list3 = [1, 2, 1]
print list1 < list3

print "---- Value equality"
print list1 == list2
print list1 == [1, 2, 3]

## 2. Sequence Type related operators
list1 = [0, 1, 2, 3, 4, 5, 6]
print "---- Slicing with positive index"
print list1[0:7:2]
print list1[0:7]
print list1[6:]
# Indexes can also be specified by negative numbers from -len to -1
print list1[0:-1]

print "---- Slicing with negative index"
print list1[-1:]  # Default did not change. step is 1 and endIndex is len -1
print list1[:0]

## Negative Step: Changing step CHANGES default start and end indexes!
print "---- Negative Step"
print list1[::-1]
print list1[0::-1]
print list1[-1::-1]
print list1[len(list1) - 1::-1]

# Slice operator gives another list of elements. However, indexed access only give the element.
print type(list1[1]), list1[1]
print type(list1[1:1]), list1[1:2]

# Also note that list1 and list1[:] have different identities
print id(list1), id(list1[:]), id(list1[1:3]), id(list1[1]), id(list1[2])
list1[1:3] = [0, 0]
print id(list1), id(list1[:]), id(list1[1:3]), id(list1[1]), id(list1[2])

## Membership
print list1
print 0 in list1
print "isa" in list1

## Concatenation Operator: Returns a new list with the elements of both list
list1 = [0, 1, 2]
print list1 + ["a", "b", "c"]
# NOTE: We cannot concatenate different sequence types, only the same types
# print [0, 1, 2] + ("a", "b", "c") # Gives error. Tuple and List

# NOTE: extend() also concatenates two lists; but the first list holds the result. append() method just adds one element. But These are functions, not operators.
list1.extend(["a", "b", "c"])
print list1
list1.append([9, 9, 9])
print list1

## Repetition
list1 = [1, 2, 3]
print list1 * 2

## There are NO list-specific operators. Strings have.
