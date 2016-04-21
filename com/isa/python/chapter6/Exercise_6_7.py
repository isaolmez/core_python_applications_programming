# !/usr/bin/env python  #
num_str = raw_input('Enter a number: ')

# Create a int object
num_num = int(num_str)

# craete range from 1 to num_num (included) and assign it to indexes from 0 to num_num -1
fac_list = range(1, num_num + 1)
print "BEFORE:", fac_list  # 1,2,3,4... num_num
i = 0

# iterate num_num times initially, but length changes
while i < len(fac_list):
    # If modulus is 0, delete that entry. This decreases the length of list and causes an entry to be skipped. If deletion has occured no increment of counter must be done.
    if num_num % fac_list[i] == 0:
        del fac_list[i]
    # Increment counter
    else:
        i = i + 1

#
print "AFTER:", fac_list
