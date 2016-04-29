def TestFunc(func, *nkwargs, **kwargs):
    try:
        returnVal = func(*nkwargs, **kwargs)
        result = (True, returnVal)
    except Exception, e:
        result = (False, e)

    return result


print TestFunc(int, 1)
print TestFunc(str, 1)
print TestFunc(float, "a")
