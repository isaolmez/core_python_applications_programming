## First of all there is no such thing as function declaration like in C or Java
## Functions cannot be called before they are defined

def foo():
    bar()

# foo()   # ERROR: bar is not defined yet, when foo is called

def bar():
    pass

foo()       # VALID

## Order of definition does not matter, as long as function call is after these definitions.
def b():
    pass
def a():
    b()
