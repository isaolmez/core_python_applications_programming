## Is prime check

def isPrimeBasic(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def isPrime(number):
    for num in range(2, number / 2 + 1):
        if number % num == 0:
            return False
    return True

print isPrimeBasic(997)
print isPrime(997)
