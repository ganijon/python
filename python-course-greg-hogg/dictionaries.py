print("Time to init dictionaries")

# literal syntax
d1 = {}  # empty
d2 = {"key": "value", "a": 1, "b": []}

# constructor
d3 = dict()  # empty
d4 = dict(key="val", a=1, b={})
d5 = dict([("a", 1), ("b", 2)])  # from array of tuples

# comprehension
d6 = {k: v * 2 for k, v in [("a", 1), ("b", 2)]}

# from keys with default value
d7 = dict.fromkeys(["a", "b"], 0)

# keys must be hashable (immutable):
# . int, float, str, bytes
# . tuple (if all elements are hashable)
# . frozenset
# . None, bool

d8 = {(1, 1): "ones", (2, 2): "twos"}

print(d1, d2, d3, d4, d5, d6, d7, d8)

print("Dictionary operations")

# read values by keys
print(d8[(1, 1)])
print(d8.get((2, 2)))
print(d8.get((3, 3)))
print(d8.get((4, 4), "not found").upper())

# read key, values, items
print(d8.keys())
print(d8.values())
print(d8.items())

# clear out
d1.clear()

# get a copy
d22 = d2.copy()
print(d2, d22)

# find and remove item by key
print("d4:", d4)
d4.pop("key")
print(f"d4's key removed:{d4}")

# remove last item
print(f"d5:{d5}")
d5.popitem()
print(f"d5's last item removed:{d5}")

# set new or update existing item key, value and return value
print(f"d6:{d6}")
val = d6.setdefault("c", 0)
print(f"val:{val}, d6:{d6}")
val = d6.setdefault("a", 0)
print(f"val:{val}, d6:{d6}")

# upsert items
print(f"d7:{d7}")
d7.update([("b", 5), ("c", 6), ("d", 7), ("e", 8)])
print(f"d7:{d7}")

print("Dictionary iteration")

# iterate over keys (default)
print("Keys:", end=" ")
for k in d7:
    print(k, end=",")

# iterate over values
print("\nValues:", end=" ")
for v in d7.values():
    print(v, end=",")

# iterate over items
print("\nItems:")
for k, v in d7.items():
    print(f"{k}: {v}")

print("Dictionary sorting")

# sort by keys
d9 = {"x": 9, "a": 1, "y": 8, "b": 2}
print(d9)  # {'x': 9, 'a': 1, 'y': 8, 'b': 2}

list9 = sorted(d9.items(), key=lambda x: x[0])
print(list9)

tpoint = (tuple([0, 0]), tuple([1, 1]))
print(tpoint)

d10 = {tpoint: 1}
print(d10)
