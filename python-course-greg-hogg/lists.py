print("Let's practice ways to init lists")

# literal, fastest, empty list
a = []  # []
b = [0, 1]  # [0, 1] 

# from constructor
c = list()  # []

# from iterables
d = list((1, 2, 3))  # from tuple # [1, 2, 3] 
e = list(range(10,0,-2)) # from range # [10, 8, 6, 4, 2]

# from repeated values 
f = [0] * 5  # repeated numbers # [0, 0, 0, 0, 0]
g = [{}] * 3  # repeated objects # [{}, {}, {}]

# from comprehension, most flexible
h = [i * 2 for i in range(5)]  # [0, 2, 4, 6, 8] 
i = [_.upper() for _ in "abc"] # ['A', 'B', 'C']
j = [{f"2^{i}": 2**i} for i in range(5)] # [{'2^0': 1}, {'2^1': 2}, {'2^2': 4}, {'2^3': 8}, {'2^4': 16}]

print(a, b, c, d, e, f, g, h, i, j)

print("\n Now let's do some ops")
a.append('a') 
a.append(1)
l = len(a)
print(l)

b.insert(0, {})
bb = b.copy() 
bb.extend(a)
print(bb.index('a'))
print(bb.pop())
bb.remove('a')
bb.reverse()

d.sort()
e.clear()

for i in f:
    print(i)

for i, v in enumerate(g):
    print(f"{i}:{v}")

for i in range(len(h)):
    print(i, h[i])

for i, sqrt in enumerate([x**0.5 for x in h]):
    print(f"{i}:{sqrt}")
    
print(a, b, bb, c, d, e, f, g, h, i, j)
