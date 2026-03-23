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
