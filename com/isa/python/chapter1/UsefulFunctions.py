## Useful Functions for beginners

name = "isa"
print "\n---- String"
## Prints the attributes of the object. Both variables and methods.
# Java: Java does not have a method like this rightaway. Reflection must be used.
print dir(name)

## Pyhton documentation for the
# Java: I do not know a Java equivalent for this function.
print help(name)

## Casts to integer. But string cannot be cast.
#Java : Integer.valueOf() is equivalent. But like this method, it must get a string representation of a number.
## print int(str)

print len(name)


print "\n---- Object"
obj = object()
print dir(obj)
print help(obj)
# len cannot be called with object/int type.
#print len(obj)
#print len(123)


evenList = range(0,10,2)
print range(0,10,2)

print str(evenList)


## Type
print type(obj)
print type(name)
print type(evenList)
print type(True)