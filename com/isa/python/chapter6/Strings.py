## Strings are immutable so you cannot modify an existing string object. You can create a new string object with contents taken from source string and then manipulated.

first = "a"
second = 'a'
print first is second
listStr = str(range(3))
print listStr

text = "isaolmez"
print text[1:]


s1 = "a"
s2 = s1
s1 = "b" ## This is reference assignment so they refer to different string objects, no magic.
print s1 is s2
# But if there was a mutating function of string both s1 and s2 could see the changes done by the other. But there is no such method. Strings are immutable.

del s1
