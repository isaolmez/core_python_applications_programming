## we call generator function once and get a generator object. To get values, we call next() method.

def generator1():
    yield 1
    yield 2
    yield 3


gen1 = generator1()
print gen1.next()
print gen1.next()
print gen1.next()
try:
    print gen1.next()
except Exception, e:
    print "Error", e


def generator2(counter):
    while True:
        yield counter
        counter += 1


gen2 = generator2(1)
print type(gen2.next())
print gen2.next()
print gen2.next()
print gen2.next()
gen2.close()

## For loops automatically calls next() and handles StopIteration example.
for item in generator2(1):
    if item == 100:
        break
    print item,
print


def advanced(counter):
    while True:
        val = (yield counter)
        if val is not None:
            counter = val
        else:
            counter += 1


adv = advanced(1)
print adv.next()
print adv.next()
print adv.next()
adv.send(100)
print adv.next()
print adv.next()
adv.close()
