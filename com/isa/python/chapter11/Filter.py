## filter() built-in function: gets a sewuence and returns a sequence after filtering
# Applies the function to each sequence element
def filterFunc(num):  # Even numbers
    return num % 2 == 0


print filter(filterFunc, range(9))  # can be passed tuple or list, but converted to tuple

print filter(lambda num: num % 2 == 0, range(9))

## With list comprehensions
print [num for num in range(9) if num % 2 == 0]
