fileName = raw_input("Please enter a file name: \n");
try:
    file = open(fileName); # Variable scope is also interesting. In Java file reference variable must be declared outside the try-catch statement.
except IOError, e:
    print e;
else:
    for line in file:
        print line,

print "DONE!"
