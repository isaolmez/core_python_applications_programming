## In fact we must make a distinction between parameters and arguments:
# Parameters are the ones specified in function declaration. They are placeholders
# Arguments are the ones specified in function invocation. They are actual instances/values.
# Declaration Terminology: required, default, formal, informal, grouped
# Invocation Terminology: positional, keyword

x, y, z = (1, 2, 3)
aa, bb, cc = (1, 2, 3)
print x, y, z
print aa, bb, cc

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

## Default Arguments: Meaningful in function declaration. Must come after required parameters.
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

## Different invocations
print "---- Different Invocations"


def func1(a, b, c, d=1, e=1, *tuples):
    print "a:", a
    print "b:", b
    print "c:", c
    print "d:", d
    print "e:", e
    print "tuples:", tuples


func1(1, 1, 1)

# Positional comes before keyword
func1(1, 1, e=1, d=1, c=1)

# Cannot specify more than once
# func1(1, 1, e=1, d=1, c=1, a = 11)

# Compile Error: Positional arguments must come before keyword arguments
# func1(e=1, 1, 1, d=1, c=1)

# Error: You cannot use keyword arguments with grouped non-keyword arguments(tuples). Also you must specify all formal parameters
func1(1, 1, 1, 2, 2, 0, 0)
# func1(a=1, b=1, c=1, d=2, e=2, 0, 0)    # Compile Error
