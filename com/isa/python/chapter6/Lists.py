## Lists : another sequence type
print sorted("isa")
list1 = [5, 24, 11]
print sorted(list1)
print list1
list1.sort()  # Mutating sort function
print list1

## List creation
list1 = [1, 2, 3]
list2 = [1, 2, "a", [True, False]]
list3 = list(list1)
print list3 is list1

list4 = list(list2)
print list4 is list2

list5 = list("isa")
list6 = list([1, 2, 3])
print list6 is list1

multiList = [[1, 2, 3], ["a", "b", "c"]]
print multiList[0]
print multiList[0][1], multiList[1][0:3]
print type(multiList[1][0:3])

## Update: index based update, update() function
list1 = [1, 2, 3]
print id(list1)
list1 = [3, 4, 5]
print id(list1)
list1[0] = 99
print id(list1), list1
list1[0:2] = [-1, -2]
print id(list1), list1
list1[0:3] = [-1, -2, -3]
print id(list1), list1
list1.append(100)
print id(list1), list1

## Result of update on id()
print id(list1), id(list1[1:3]), id(list1[1]), id(list1[2])
list1[1:3] = [0, 0]
print id(list1), id(list1[1:3]), id(list1[1]), id(list1[2])

## Remove: del operator, remove() and pop() functions
del list1[1]
print id(list1), list1
list1.remove(100)          ## We remove with the value of element
print id(list1), list1
list1.pop()
print id(list1), list1









