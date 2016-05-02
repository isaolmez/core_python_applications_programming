def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print factorial(6)


def factorial2(start, n):
    if start > n:
        return 1

    return start * factorial2(start + 1, n)


print factorial2(2, 6)


def factorialRunning(start, running, n):
    if start > n:
        return running
    
    print "running factorial: %d" % (running)
    running *= start
    return factorialRunning(start + 1, running, n)


print factorialRunning(2, 1, 6)
