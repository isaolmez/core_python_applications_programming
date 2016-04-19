## Methods

def method1():
    print "hello world"


method1()
number = 12


def method2(number):
    number = 24
    return number


print "Before", number
returned = method2(number)
print "After", number
print "Method return", returned


# Methods with concetanation operator. + sign supports not only addition and string concatenation, it also supports sequence concatenation.
def concat(item):
    print item + item

concat(1)
concat("isa")
concat("isa" * 2)
concat([1, 2])
concat((1, 2));
## Does not support dictionary; because uniqueness constraint would be violated.
# Side not after an exception is encountered
## concat({"name": "isa", "age": 32})



## Default parameters
def ticketPrices(adult = True):
    if(adult):
        print "Give 100 Coins"
    else:
        print "Give 50 Coins"

ticketPrices()
ticketPrices(False)