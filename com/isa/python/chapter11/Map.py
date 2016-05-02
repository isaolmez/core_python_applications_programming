## map() built-in function: gets a sequence and returns a sequence

def mapFunc(num):
    return num + 5


print map(mapFunc, range(9))

print map(lambda num: num + 5, range(9))

# With list comprehensions
print [num + 5 for num in range(9)]