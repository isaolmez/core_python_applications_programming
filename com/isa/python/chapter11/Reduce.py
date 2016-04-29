## reduce() built-in function: gets a sequence and returns a single scalar value
# parameter func must accept 2 arguments
# Can be benefical for running statistics

def reduceFunc(arg1, arg2):
    result =  max(arg1, arg2)
    print result
    return result


list1 = [1, 23, 4, 5, 6, 89, 0, -1]
# Calculates and Shows RUNNING/local maximum
print reduce(reduceFunc, list1)

# Calculates RUNNING maximum but Shows FINAL/global maximum
print reduce(lambda arg1, arg2: max(arg1, arg2), list1)
print reduce(lambda arg1, arg2: max(arg1, arg2), list1, 999)

