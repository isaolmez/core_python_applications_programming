for item in range(0,21,2):
    print item,

print

for item in range(0, 21):
    if item % 2 == 0:
        print item,

print

for item in range(1,21,2):
    print item,

print


for item in range(0, 21):
    if item % 2 == 1:
        print item,

print

## If you omit return type, it does not give warning but returns None
def isDivisible(num1, num2):
    if num1 % num2 == 0:
        return True
    return False

print isDivisible(10, 2)
print isDivisible(10, 20)
