from decimal import Decimal
print Decimal(1)
print Decimal("1")

## Cannot use float
print Decimal(1.0)

dec1 = Decimal(10)
dec2 = Decimal(12);
result = dec1 + dec2
print result
print type(result)