from time import ctime


def Logger(when):
    def log():
        print "Time is: [%s]" % ctime()

    def logBeforeBad(func):
        log()
        return func

    def logBefore(func):
        def wrapped():
            log()
            func()

        return wrapped

    def logAfter(func):
        def wrapped():
            func()
            log()

        return wrapped

    return {"before": logBefore, "after": logAfter}[when]


@Logger("after")
def testFunction():
    print "inside testFunction"

# Does nothing as intended, but packs all the code into one logical block.
# Decorator does not run any logic it just gives me decorated function. All code runs when I call the original function
testFunction


testFunction()

