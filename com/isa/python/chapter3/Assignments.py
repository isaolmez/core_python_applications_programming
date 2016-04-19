## Assignment resemble to Java.
# Object references are copied not the objects are copied.
# For references assignment results in 2 reference variables pointing to the same object.
# For primitives, 2 variables do not point anything but store the same value. They do not have any relation other than that.
numbers = [1, 2, 3, 4, 5];
numbersCopy = numbers;
numbers.append(12)
print numbers, type(numbers);
print numbersCopy, type(numbersCopy);

single = 12;
singleCopy = single;
single = 13;
print single, type(single);
print singleCopy, type(singleCopy);

## Assignments are not expression. In Java, assignment statement has a value and it is the right-hand side of the assignment.
x = 1
# y = (x = x +1) # Not valid


# This is valid though. Weird.
y = x = x + 1

## Compound(Augmented) Operators
x = 1
print x
x += 1
print x
x **= 2
print x
myList = [1, 2, 3]
myList += [7]
print myList

## No pre/post increment/decrement operators.

## Multiple assignmens

x = y = z = 1
print "Multiple assignments", x, y, z

## Multuple assignments
a, b = "a", "b"
print "Multuple assignments", a, b
(x, y, z) = (1, 2, "isa")
print "Multuple assignments", x, y, z

# Swap without temporary
(x, y) = (y, x)
print "Swapped", x, y
