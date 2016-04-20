import math

## For ALL types : cmp(), str() and type() built-in functions apply to all standard types including number types
print "For ALL types"
print cmp(1, 1)
print str(123)
print type(0.0 + 0.1j)

## For NUMERIC types: There are some built-in functions that operate only on number types
# 1. Conversion functions or factory functions or constructors
# 2. Operational functions
print "Exclusive to NUMERIC types"

## Conversion functions
# int(), long(), float(), complex(), bool()
print "Conversion Functions"
print int(213.2)
print int("213")
# print int("213.2") # gives error

print "long()", long(12)

print "float()", float(12)

print "complex()", complex(12)
print "complex()", complex(12, 3)

## Only 0 is false other positive/negative numbers are true
print "bool()", bool(12)
print "bool()", bool(0)
print "bool()", bool(-1)
print "bool()", bool(-1.0)

## Operational Functions
# abs(), coerce(), divmod(), round(), pow()
print "Operational Functions"
print abs(-2.3)
print abs(-2)

print coerce(1, 1.0)
print coerce(1.0, 1L)

print divmod(5, 2)
print divmod(5.0, 2.0)

print pow(3, 2)
print pow(3, 2, 5)

print round(1.12345)
print round(1.12345, 1)
print round(1.12345, 2)
print round(1.12345, 3)

## the middle point is rounded by moving away from ZERO
print "round(0.5)", round(0.5)

## Differences between int() math.floor() and round()
print int(1.7)
print round(1.7)
print math.floor(1.7)

print int(1.2)
print round(1.2)
print math.floor(1.2)

print int(-1.7)
print round(-1.7)
print math.floor(-1.7)

print int(-1.2)
print round(-1.2)
print math.floor(-1.2)

## For INTEGER types:
print "Exclusive to INTEGER types"
print hex(100)
print oct(100)

print ord("a")
print chr(ord("a"))
