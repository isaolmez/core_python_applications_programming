# Different syntaxes tom import modules.
# Modules are just physical files. A file with .py extension is a module containing classes, functions and variables.

import os
from os import linesep
import sys as s
from os import (listdir, link, write)
from os import *

# Modules are searched in PYTHONPATH env variable or sys.path
print "Search path:", s.path

# sys.modules return a map:
# key = module name
# value = path of the module (file)
print "Loaded modules", s.modules
print "Keys of loaded modules", s.modules.keys()


## When function is called, import statement runs and module is imported
def localImport():
    import random   # This can be used to prevent "import loops"
    x = [1, 2, 3]
    print "modules", s.modules


print "random" in s.modules
localImport()
print "random" in s.modules

li = localImport
print type(localImport)
