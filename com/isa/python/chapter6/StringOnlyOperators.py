## String only operators
## Format operator

# Hexadecimal output
print "%x" % 108
print "%X" % 108
print "%#x" % 108
print "%#X" % 108

# Floating point and exponential output
print "%f" % 12.12345
print "%.2f" % 12.12345  # Limit the decimal points to 2

# Integer and string output
print "%+d" % 22
print "%s" % 22
print "%f" % 22
print "%.2f" % 22
print "%d%%" % 75

# Tuple arguments
print "%d, %d" % (99, 11)
print "%s %.2f" % ("abc", 12.23)

# Dictionary arguments
print "%(first)s %(second)d" % {"first": "isa:", "second": 32}

## String templates
from string import Template

s = Template("There are ${count} houses in ${city}")
print s.substitute(count=123, city="izmir")
print s

## Raw Strings
# Does not treat any character as special.
s1 = "abc\ndef"
print s1
s1 = r"abc\ndef"
print s1

import re

m = re.search("\\[rtfvn]", r'Hello World!\n')
if m is not None: m.group()
## Regular expression also have their special escape characters so we must use raw regex. If we did not, we must use 4 backslashes in regex to catch single backslash in the string.
m = re.search(r"\\[rtfvn]", r'Hello World!\n')
if m is not None: m.group()

