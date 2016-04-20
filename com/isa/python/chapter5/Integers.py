# boolean
# integer : 32 bit on 32-bit systems, 64 bits on 64-bit systems
# long : only limited to the size of virtual memory

num = 99999999L
print num
print str(num)
# Only repr() preserves the L suffix, others drop it
print repr(num)

# So only repr() can be used to recreate the object from its string representation
print type(eval(str(num)))
print type(eval(repr(num)))


# Integers does not cause overflow. They are converted to long
print repr(99999**8)