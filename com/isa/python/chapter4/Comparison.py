class MyClass(object):
    def __init__(self, nm="isa"):
        self.name = nm

    def toString(self):
        print str(self)


if (__name__ == "__main__"):

    one = MyClass()
    print one
    two = MyClass("isa")

    ## Object Value Comparison
    ## Unlike Java, objects can be compared with operators. In Java we use compareTo() or equals() methods.
    if one == two:
        print "Equals"
    elif one < two:
        print "Smaller"
    elif one > two:
        print "Greater"
    else:
        print "Dead code"

    alias = one
    if one == alias:
        print "Aliased"
    if one is alias:
        print "Refer to the same object"
    if id(one) == id(alias):
        print "Refer to the same object"
    alias = MyClass

    if one == alias:
        print "Values are equal"

    ## Object Identity Comparison
    ## It seems Python is caching objects with the same literals. But when the value is same but the literal is not same, it creates a new object
    num1 = 300
    num2 = num1
    if num1 is num2:
        print "Aliased"

    num3 = 200 + 100
    if num1 is num3:
        print "Aliased"

    print "Id of num1:", id(num1)
    print "Id of num2:", id(num2)
    print "Id of num3:", id(num3)

    ## It also caches for string objects. When there is an expression which the interpreter cannot decide what the result is, it creates a new object.
    name1 = "a"
    name2 = name1
    name3 = "a"
    name4 = "ab"[0:0]

    print "Id of name1:", id(name1)
    print "Id of name2:", id(name2)
    print "Id of name3:", id(name3)
    print "Id of name4:", id(name4)

    ## Comparasions

    if 3 < 4 < 7:
        print "Multiple comparisons in single expression"

    num = 5
    if 1 < num < 100:
        print num, "is between 1 and 100"
