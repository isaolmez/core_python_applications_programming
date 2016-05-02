## Variable Scope:
# Global: Script level, defined in the script outside any class or function
# Function Local Scope: Function level, defined inside the function

isGlobal = "global"


def func():
    isLocal = "function local"
    if True:
        isBlock = "no block"  # NO. There is no block scope like in Java.

    print "%s and %s" % (isLocal, isGlobal)


func()

# Shadowing

num = 0


def foo():
    # print "Value before assignment: %s" % (num) # ERROR: Cannot use global before assignment, if there is a local variable with the same name. Java does not give this compile error.
    num = 2  # Local variable, shadowing
    print "Value inside the function: %s" % (num)


foo()
print "Value outside the function: %s" % (num)


## Global keyword does two things, if there is an assignment of a variable with the name of global:
# * You can reach the variable before assignment
# * You do not create a local variable with the same name and modify the global variable.
# So since there is no declaration in Python, you cannot modify global variable without "global" keyword

def foo2():
    global num
    print "Value before assignment: %s" % (num)
    num = 2  # Local variable, shadowing
    print "Value inside the function: %s" % (num)


foo2()
print "Value outside the function: %s" % (num)
