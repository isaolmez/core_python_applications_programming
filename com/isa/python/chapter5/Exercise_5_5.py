def modulus(number):
    temp = number
    number = int(number)
    quarter, number = divmod(number, 25)
    dime, number = divmod(number, 10)
    nickel, number = divmod(number, 5)
    penny, number = divmod(number, 1)

    print temp, "is", quarter,"quarters",dime,"dimes",nickel,"nickels",penny,"pennies"


modulus(76)
modulus(56)