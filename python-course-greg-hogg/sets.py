print("Practice sets")

s = {}  # {}
s1 = {1, 4, 1, 3, 2, 3, 3}  # {1, 2, 3, 4}
s2 = set([1, 2, 3])  # {1, 2, 3}
s3 = set(range(5))  # {0, 1, 2, 3, 4}
s4 = set("abcabc")  # {'b', 'a', 'c'}

print(s, s1, s2, s3, s4)


print("Practice set basic operations")

s1.add(5)
print(s1)  # {1, 2, 3, 4, 5}

s1.pop()  # removes arbitrary element, but throw TypeError if set is empty
print(s1)  # {2, 3, 4, 5}

try:
    s.pop()  # pop from an empty set
except TypeError as e:
    print(e)  # pop expected at least 1 argument, got 0

s1.remove(3)
print(s1)  # {2, 4, 5}

try:
    s1.remove(
        10
    )  # removes element, but throws KeyError when it does not exist in a set
except KeyError as e:
    print(e)  # KeyError: 10

print(s1)  # {2, 4, 5}

s1.clear()
print(s1)  # set()

s1.add(1)
print(s1)  # {1}

s1.discard(
    1
)  # removes element without throwing exception when it does not exist in a set
print(s1)  # set()


print("Practice set union and intersection")

print(s2, s3)  # {1, 2, 3} {0, 1, 2, 3, 4}

print(f"union: {s2.union(s3)}")  # {0, 1, 2, 3, 4}
print(f"intersection: {s2.intersection(s3)}")  # {1, 2, 3}

print(s2, s3)  # {1, 2, 3} {0, 1, 2, 3, 4}

s2.update(s3)
print(s2, s3)  # {0, 1, 2, 3, 4} {0, 1, 2, 3, 4}

s1 = {1, 2, 3, 4}
s2 = {0, 1, 2, 5}
s1.intersection_update(s2)
print("intersection_update:", s1)  # {1, 2}

print("Practice set differences and symmetric differences")

s1 = {1, 2, 3, 4}
s2 = {0, 1, 2, 5}
print("difference:", s1.difference(s2))  # {3, 4}
print("symmetric_difference:", s1.symmetric_difference(s2))  # {0, 3, 4, 5}

s1.difference_update(s2)
s1.symmetric_difference_update(s2)

print("Practice set disjoint, subset and superset")

s1 = {1, 2, 3, 4}
s2 = {0, 1, 2, 5}
print("isdisjoint:", s1.isdisjoint(s2))  # False

s1 = {1, 2, 3, 4}
s2 = {1, 2}
print("issubset:", s1.issubset(s2))  # False
print("issubset:", s2.issubset(s1))  # True

print("issuperset:", s1.issuperset(s2))  # True
print("issuperset:", s2.issuperset(s1))  # False