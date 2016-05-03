## Old-style : A base class is not specified. Or specified class does not inherit from class "object"

class Old():
    def __init__(self):
        print "Old style without base class"

class Old2(Old):
    def __init__(self):
        print "Still old style, base class does not inherit from object"


old1 = Old()
old2 = Old2()
print type(Old)     # classobj
print type(old1)    # instance
print type(Old2)
print type(old2)


## New-style: Base class should be either class "object" or one inheriting from "object"
# Notice the first parameter of instance methods is self, the instance itself.
# __init__ is like constructor.
class New(object):
    def __init__(self):
        print "New style with base class that inherits from object"

class New2(New):
    def __init__(self):
        New.__init__(self)      # Constructor chaining like behaviour
        print "New style with base class that inherits from object"


new1 = New()
new2 = New2()
print type(New)     # instance of type
print type(new1)    # Class name is prepended with module name
print type(New2)
print type(new2)

print type(1)