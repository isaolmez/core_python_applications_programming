## Python Exceptions
# 1. There is no distinction between checked and unchecked exception, recoverable and unrecoverable exceptions.Hence there is no handle or declare rule
# 2. Exception propagation is similar, exception is propagated until the stack is exhausted.
# 3. Root class for exceptions is BaseException. There are 3 children: KeyboardInterrupt, SystemExit and Exception which is the super class for all other exceptions

## try-except
try:
    file1 = open("test.txt")
except IOError, e:
    print e
    print type(e)

## try-except-else
try:
    file1 = open("test.txt", "r")
except IOError, e:
    print e.args
    print type(e.args)
else:
    print "No errors have been encountered!"

## try-except-finally
try:
    file1 = open("test.txt", "r")
except:
    print "Error has occured!"
finally:
    print "Cleanup"
    # file1.close() # ERROR: file1 is not defined, since test.txt does not exist.

## try-except-else-finally
try:
    file1 = open("test.txt", "r")
except:
    print "Error has occured!"
else:
    print "No exception"
finally:
    print "Cleanup"

## Multiple except statements
try:
    pass
except IOError, e:
    print e
except ArithmeticError, e:
    print e

## Multiple exceptions
try:
    pass
except (IOError, ArithmeticError), e:
    print e


## catch all
try:
    pass
except:
    print "All exceptions are catched"

## catch without argument
try:
    pass
except IOError:
    print "Error!"