from time import ctime


def Logger(when):
    def log(*nkwargs, **kwargs):
        print "Time is: [%s] with variables %s" % (ctime(), nkwargs)

    def logBefore(func, *nkwargs, **kwargs):
        def wrapped(*nkwargs, **kwargs):
            log(*nkwargs, **kwargs)
            return func(*nkwargs, **kwargs)

        return wrapped

    def logAfter(func, *nkwargs, **kwargs):
        def wrapped(*nkwargs, **kwargs):
            result = func(*nkwargs, **kwargs)
            log(*nkwargs, **kwargs)
            return result

        return wrapped

    try:
        return {"before": logBefore, "after": logAfter}[when]
    except KeyError, e:
        raise ValueError(e)  # Propogate the exception


@Logger("after")
def testFunction(a, b, c, d):
    print "inside testFunction"


testFunction(1, 2, 3, 4)
