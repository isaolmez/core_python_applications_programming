import decimal

counter = 0;
name = "isa"
age = 32
kilometres = 12.2

## No unary increment operator
print ++age

## There are compound operators
age += 1
print age

## There are 3 representations of integers: octal, hexadecimal and decimal. Java's binary representation is missing
hexRepresentation = int(0x101)
print hexRepresentation
octalRep = 0101
print octalRep

## Long type can hold arbitrarily long integer values only limited to the virtual memory space allocated to the process.Java equivalent is BigInteger class.
longRep = 123L
print longRep

boolRep = bool(True)
print boolRep
boolRep = False
print boolRep

## Type is determined with assignment. Hence it is an dynamically typed language, not a statically typed language.
boolRep = 12
print boolRep

## There is no F suffix to differentiate float values from double values like in Java.
## In Java, floating-point number literals are double by default, and needs a suffix F to explicitly set to a float variable.
floatRep = 12.2
print floatRep

## It says that there will be no distinction between int and long values, and therefore no need for L suffix. It will be dynamically cast back and forth from int to long.

## Boolean variables are treated like integers in appropriate contexts like char type in Java
print True + True
boolRep = False + True
print boolRep == 1

## To get more precision for floating-point numbers, we have decimal like BigDecimal in Java.
floatRep = 1.1
print floatRep
print 1.1
decimalRep = decimal.Decimal("1.1")
print decimalRep
