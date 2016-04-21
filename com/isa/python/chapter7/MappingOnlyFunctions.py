## 3. Mapping Type Functions
# Dictionary is unordered as expected, since it is a symbol table based on hashing
# Dictionary is mutable
d1 = dict(x=1, y=2, z=3)
print d1.keys()
print d1.values()
print d1.items()
d2 = {"a": "1", "b": "1", "a": "99"}    # Last key wins and overwrites others
d1.update(d2)
print d1
print d1.get("a")

# setdefault()
# print d1["abc"] # ERROR
print d1.get("abc")
d1.setdefault("abc", "Absent")
print d1.get("abc")
d1["abc"] = "Existent"
print d1.get("abc")
