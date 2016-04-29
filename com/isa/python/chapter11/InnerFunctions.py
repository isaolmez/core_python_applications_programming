## Inner Functions:
# Inner functions create a closure where they can access parent functions scope.
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
    closureDummy(item)

for func in funcs:
    func()
