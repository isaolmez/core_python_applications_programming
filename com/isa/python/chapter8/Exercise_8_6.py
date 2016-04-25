def primeFactors(number):
    factors = []
    while number != 1:
        divident = 2
        while divident <= number / 2:
            if number % divident == 0:
                factors.append(divident)
                number = number / divident
                break
            else:
                divident += 1
        else:
            factors.append(number)
            break

    return factors


print primeFactors(1000)
