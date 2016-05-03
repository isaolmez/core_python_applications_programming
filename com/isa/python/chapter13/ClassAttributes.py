## Class Methods: They are mostly considered as bound. But unbound ones can also be called

class Test(object):
    ## Class Attribute or static variables like in Java
    var = "class variable"

    # This is method attribute. Although it is called on instances, it can also be called on class objects and thus it is a class atrribute.
    def instanceMethod(self):
        pass


print dir(Test)
print Test.__dict__
print Test.__name__
print Test.__doc__
print Test.__class__
print Test.__bases__
