## Preventing import of some attributes
# As an API developer, prepend with underscore, "_"
# Attributes with "_" does not get imported with from .. import *.
# But full module import and specific imports still get the underscored variables.
# from os import *

from pickle import *
# print _binascii   # Hidden
import pickle
print pickle._binascii