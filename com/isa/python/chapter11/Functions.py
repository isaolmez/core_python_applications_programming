x, y, z = (1, 2, 3)
a, b, c = (1, 2, 3)
print x, y, z
print a, b, c

## There is no overloading in Python like Java. Last written function overwrites the others, signature-wise.
print "---- No Overloaded Functions"


def method1():
    print "No arg"


def method1(a1):
    print "1 arg"


def method1(a1, a2):
    print "2 arg function:", a1, a2


# method1()
# method1(1)
method1(1, 2)

## Keyword arguments: Enables us to redefine the order of arguments when passed to the function.
# These are known as keyword arguments. Standard arguments are known as nonkeyword arguments.
print "---- Keyword Arguments"
method1(a2=2, a1=1)

## Default Arguments
print "---- Default Arguments"


def lazy(a, b, c="Default"):
    print a, b, c


lazy(1, 2, 3)
lazy(1, 2)

## Grouped Arguments
print "---- Grouped Arguments"


def grouped(*arguments_as_tuple, **arguments_as_dictionary):
    print arguments_as_tuple
    print arguments_as_dictionary


args = (11, 2, 3)
grouped(args)

args2 = {"a": 11, "b": 22, "c": 33}
grouped(args2)

grouped()

print 1 == "1"
