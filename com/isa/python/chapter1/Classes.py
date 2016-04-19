## Classes
# Are there any access modifiers(public, protected, private, default) or non-access modifiers (final, volatile, strictfp, abstract, static)
class Test(object):
    """First Pyhton class
    Notes:
        1. Static variables are not declared with any keyword like static. They are just written as instance variables and they are static, accessible from all instances
        2. Instance variables seems not to be declared outside the methods but inside the init method. Not sure though, will look later.
    """
    version = 1.0
    def __init__(self, name = "isa"):
        "Initializer function that is called right after the object is created. Seems like Java constructors; but does not responsible for object creation"
        self.name = name
        print "New Test instance is created"

    def showName(self):
        "A regular method"
        print "My name is:", self.name
        print "My class name is:", self.__class__.__name__

    def showVersion(self):
        """Self server as this"""
        print "My version is:", self.version

    def addMe2Me(self, x):
        return x + x


## Class creation
# It is like method call. There is no keyword like new.
isa = Test()
hilal = Test("hilal")
print isa
print "---showName()"
isa.showName()
print "---showVersion()"
isa.showVersion()
print isa.addMe2Me(2)
