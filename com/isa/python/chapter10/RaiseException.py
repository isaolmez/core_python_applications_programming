## Raising Exceptions: We can as developer can raise exceptions, also finally without except raises exception

# Class and arguments. Instance is created for the given class with given arguments
def inner():
    raise IOError, "File not found"


def outerWithoutHandle():
    inner()


def outerWithHandle():
    try:
        inner()
    except IOError, e:
        print e


outerWithHandle()
outerWithoutHandle()


# Instance
def inner2():
    raise IOError()
