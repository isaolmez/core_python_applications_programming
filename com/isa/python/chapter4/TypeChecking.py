def displayNumType(num):
    print num, ":",
    if (isinstance(num, (int, long, float, complex))):
        print "a number of type:", type(num).__name__
    else:
        print "not a number"


displayNumType(12)
displayNumType(-12)
displayNumType(True)
displayNumType("abc")

print type(True)
print type(True) == type(0)


def displayNumType1(num):
    source = type(num)
    print num, ":",
    if source == type(0):
        print "int"
    elif source == type(0L):
        print "long"
    elif source == type(0.0):
        print "float"
    elif source == type(0 + 0j):
        print "complex"
    else:
        print "not a number"


displayNumType1(12)
displayNumType1(-12)
displayNumType1(True)
displayNumType1("abc")

import types
def displayNumType2(num):
    source = type(num)
    print num, ":",
    if source == types.IntType:
        print "int"
    elif source == types.LongType:
        print "long"
    elif source == types.FloatType:
        print "float"
    elif source == types.ComplexType:
        print "complex"
    else:
        print "not a number"


displayNumType2(12)
displayNumType2(-12)
displayNumType2(True)
displayNumType2("abc")

## The most tuned version. Lookup is minimal for module attributes. We are using "is" instead of "==". We store the type of num in a seperate variable, thus not doing a function call.
from types import IntType, LongType, FloatType, ComplexType
def displayNumType3(num):
    source = type(num)
    print num, ":",
    if source is types.IntType:
        print "int"
    elif source is types.LongType:
        print "long"
    elif source is types.FloatType:
        print "float"
    elif source is types.ComplexType:
        print "complex"
    else:
        print "not a number"


displayNumType3(12)
displayNumType3(-12)
displayNumType3(True)
displayNumType3("abc")
