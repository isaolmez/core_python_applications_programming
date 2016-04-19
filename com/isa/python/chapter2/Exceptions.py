## Java's try catch mechanism. Questions are:
# 1. Can we declare multiple exceptions? and does order matter?
# 2. Can we propagate the errors. ie handle or declare
# 3. Is there a distinction like checked and unchecked exceptions? Are all exceptions recoverable in that sense?
# Remember that Java's runtime exceptions and errors cannot be recovered. Only checked exceptions
# 4. What is the error, exception type hierarchy and where custom exceptions start in this hierarchy?
# 5.

try:
    myFile = open("non.txt")
except IOError, e:
    print "File not found exception"
    print "Exception details are:", e

