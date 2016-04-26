import sys

try:
    open("test.txt")
except IOError, e:
    info = sys.exc_info()
    print info
    for line in info:
        print line
