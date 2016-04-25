def getFactors(number):
    factors = [1]
    for item in range(2, number / 2 + 1):
        if number % item == 0:
            factors.append(item)

    factors.append(number)
    return factors


print getFactors(100)
