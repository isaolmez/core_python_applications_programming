import os

## List Comprehensions
# Compare list comprehensions with map(),filter() functions
list1 = [num ** 2 for num in range(5)]

print list1
print map(lambda num: num ** 2, range(5))

print [num ** 2 for num in range(5) if num % 2 == 0]
print map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, range(5)))

## Files
file1 = open("test.txt", "r")
print os.stat("test.txt").st_size
# word count -1 = space count
wordCount = len([word for line in file1 for word in line.split()])  # Here file1's iterator has been called
print "Word count", wordCount  # So space count is

# Iterator has exhausted the file.
file1.seek(0)
nonSpaceCharCount = sum([len(word) for line in file1 for word in line.split()])
print "Non-space char count:", nonSpaceCharCount
