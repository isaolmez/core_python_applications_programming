## If statements
# There are no curly braces to specify a block of code as it is in Java. We will use indentation to define a block of code. A code of block can consist of a single line of code.
# We will also use  colons to start the block
if(True):
    print "yes true"

if(1 < 2):
    print "1 is smaller than 2"

if(True):
    print "if block"
else:
    print "else block"

## if elif elif else
## Interpreter in IDE does not give any warning related to dead code, since there are some in this example
if(False):
    print "if block"
elif(True):
    print "else if block"
elif (True):
    print "else if block"
else:
    print "else block"


## Parantheses are redundant. Also to write empty statements like ";" in Java, we can use pass keyword to skip statement speficifation.

if True:
    pass
elif False:
    pass
elif True:
    pass
else:
    pass

## There is no switch statement in Python