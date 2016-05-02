## Creates and returns the function reference
# Constructs a CLOSURE
def func():
    y = 5
    lam1 = lambda x: y + x
    return lam1


print func()(12)

## Creates the function reference and calls the function
# Constructs a CLOSURE
def func():
    y = 5
    lam1 = lambda x: y + x
    print lam1(10)
    y = 20
    print lam1(10)


func()

## Does NOT constructs a closure
def func():
    y = 5
    lam1 = lambda x, y: y + x
    print lam1(y, 10)
    y = 20
    print lam1(y, 10)


func()

glob = 99
def func():
    y = 5
    lam1 = lambda x: y + x + glob
    return lam1

print func()(12)