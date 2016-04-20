## 1. Standard Operators that can be applied to most objects
s1 = "abc"
s2 = "xyz"

print "---- comparison operators"
print s1 < s2
print s1 == "abc"
print s1 is "abc"  ## Caching

## 2. Sequence Operators
# slice operator
print "---- slice operator"
text = "abcd"
print text[0:100]
print text[:100]
# print text[100] # Error
print text[-100:]
print text[-100:-1]
print text[-100:None]

# reverse slice
print text[-1:-100:]  # Does not print. Start at the end, but step is 1
print text[-1:-100:1]  # Does not print. Start at the end, but step is 1
print text[-1:-100:-1]  # Prints. Step is -1, it is in the reverse direction as intended

print text[::]

print "---- in operator"
print "z" in text
print "a" in text
print "d" in text

## Runtime String Concatenation

print "---- concatenation"
print "%s %s" % ("isa", "olmez")
print "".join(("a", "b", "c"))
print "".join(["a", "b", "c"])

# Compile-time String Concatenation
s1 = "a" "b" "c"
s2 = ("a"  # Can be useful in parameter passing
      "b"
      "c")
print s1, s2

## Coercion
print repr("a" + u"b" + "c")

## Repetition
print "xyz" * 3





