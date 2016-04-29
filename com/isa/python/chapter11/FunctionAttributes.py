## Function Atrributes: Another perk of being an object, first-class citizen in a language.
def foo():
    'foo function'
    bar()
    bar.__dict__["x"] = "modified x"


def bar():
    x = 1
    print x
    pass


bar.__doc__ = "bar function"
bar.__dict__["x"] = "x"
print foo.__doc__
print bar.__doc__
print bar.__dict__["x"]
foo()
print bar.__dict__["x"]
bar()