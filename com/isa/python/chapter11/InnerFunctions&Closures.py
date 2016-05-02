## Inner Functions:
# Inner functions create a closure where they can access an outer scope(but not the global scope).
def foo(num):
    def bar():
        print "in bar with %d" % (num)

    bar()


foo(12)

## Closure Test: What is the problem?
funcs = []
for item in range(9):
    def inner():
        print item,


    funcs.append(inner)

for func in funcs:
    func()

# Solution: Usage of closure to snapshot the scope of its parent. This way we have intended result.
print
funcs = []
for item in range(9):
    def closureDummy(arg):
        def inner():
            print arg,
        funcs.append(inner)
    closureDummy(item)      # Calls the outer and creates the closure

for func in funcs:
    func()


## Another Example
print
def counter(num):
    count = [num]
    def inc():          # Operates as a callback with scope of the outer function counter
        count[0] += 1
        return count[0]
    return inc

incFunc = counter(5)    # Calls the outer func and Create the closure
print incFunc()
print incFunc()
print incFunc()
print incFunc()

