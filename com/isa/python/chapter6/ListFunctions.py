## List Related Standard Functions
## 1. Standard Type Functions: can be applied to most classes
list1 = [1, 2, 3, 6, 5, 4]
list2 = [4, 5, 6]
print cmp(list1, list2)  # iterate the list and compare if types are same
list3 = ["a", "b", "c"]
print cmp(list1, list3)  # iterate the list and numbers are always smaller than other objects

## 2. Sequence Type Functions: can be applied to sequence types
# len(), max(), min(), sorted(), reversed(), enumerate(), zip(), sum()
print len(list1)
print max(list1)
print min(list1)
print sorted(list1)
for item in reversed(list1):
    print item,

print

for i, item in enumerate(list1):
    print item, "at index", i

print

names = ["isa", "hilal"]
surnames = ["olmez", "kiran"]
for name, surname in zip(names, surnames):
    print name, surname

print sum(list1)

## Factory functions and identity
print "---- Factory functions and identity"
tuple1 = tuple(list1)
print tuple1 == list1   # ! Although values are same a list cannot be equal (value-wise) to a tuple
print tuple1 is list1   # A tuple cannot be same object as a list
list2 = list(list1)
print list1 == list2    # Values are equal
print list1 is list2    # Two different list objects


## 3. List Type Functions: There is NONE