## Scope and namespaces are very similar.
# Local scope has local namespace
# Global scope has global namespace and built-in namespace
#
#
# Also all modules have module namespaces which can be global or local depending on where they are imported
# You can get namespaces everywhere, even instances to hold temporary variables not defined in class definition.
# But these specific scopes falls into two categories(lcoal, global) when used in a running code.


## SCOPE = Can I see it? NAMESPACE = "Does it have it?"
# Summary: Because of scope rules, namespaces occur and those names in that scope are accessed in a certain way. So what matters most is how we define the scopes.
# Process= Obtain the name to be accessed, then:
# 1. Search local, global and built-in namespaces
# 2. If it contains, you can access it.
# 3. If it does not contain, this means that because of scoping the name is not in the namespaces in the first place.
name = "isa"  # Global namespace


def func1():  # Global namespace
    name = "isa"  # Local namespace


print name  # Can access global namespace. Can access

# Importing actually means getting an object of the module, so we can access its attributes
import sys  # Added module name to the current namespace: global namespace

print sys.path  # Access sys name from global/local namespace and then access module namespace.


def functionLocal():
    x = 1
    print sys.path
    import os               # Added module name to the current namespace: local namespace
    print [os.linesep]      # In the local namespace, can access it
    print "globals()", globals()
    print "locals()", locals()


functionLocal()
# print os.linesep  # It is not in the local namespace nor in the global of main script.

# Lets see
print "globals()", globals()
print "locals()", locals()
