## Python caches literals

a = 10
b = 10
c = 1000
d = 1000
e = 10.0
f = 10.0

print a is b
print c is d
print e is f

## But there seems a limit when there is an expression involved. Much complex caching mechanism than Java.
x = 10
y = 2 + 8
print x is y

x = 1000
y = 200 + 800
print x is y