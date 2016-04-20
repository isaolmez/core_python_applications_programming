# Comparison operators(for all standard types): == >= <= > < !=
# Boolean operators(boolean type): and or not
# Arithmetic(numeric types) operators: + - * / %
# Bit operators(integer numeric types): & | ~ << >>
# Idetity comparsion operators: is
# Functions: isinstance() type() cmp() repr() str()


## There are 3 levels of division
# / => performs classic division depending on the types of operands
# // => performs floor division regardless of the types of operands
# true division import which make all implicit floor divisions(integer division) true division

## Comment out to see different versions
# from __future__ import division # Makes all divisions true division


def division():
    print "Classic division"
    print 2 / 4  # Floor division
    print 2.0 / 4.0  # True division
    print 2.0 // 4.0  # Floor division
    print -1 // 2


division()
expr1 = 1
expr2 = 4

print expr1 ** expr2
print +expr1  # (unary) expr sign unchanged
print -expr1  # (unary) negation of expr
print expr1 ** expr2
print expr1 * expr2  # expr1 times expr2
print expr1 / expr2  # expr1 divided by expr2 (classic or true division)
print expr1 // expr2  # expr1 divided by expr2 (floor division [only])
print expr1 % expr2  # expr1 modulo expr2
print expr1 + expr2  # expr1 plus expr2
print expr1 - expr2  # expr1 minus expr2
