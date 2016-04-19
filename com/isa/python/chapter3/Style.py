import sys
name = "style"
class Style(object):
    "A class to test style"

    def method1(self):
        print "method1"

    def method2(self):
        print "method2"




def moduleMethod1():
    print "Module method1"

def moduleMethod2():
    print "Module method2"


## This line prevents the code to run when imported. It only runs when this file is run as a script
if(__name__ == "__main__"):
    moduleMethod1()

## This line runs whether this module is imported or started as a script
moduleMethod1()
