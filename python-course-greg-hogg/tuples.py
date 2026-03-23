print("Practice tuples")

t = ()  # empty tuple
t1 = (0, 1)
t2 = ('a', 'b', 'c')
t3 = tuple(range(5,51,5))
t4 = tuple([_ for _ in 'xyz'])

print(t, t1, t2, t3, t4)

print(t1[0])
print(t1.count(1))
print(t1.index(1))

for item in t3:
    print(item, end=' ')

try:
    print(t[0])   # empty tuple, nothing at index 0
except IndexError as e:
    print(e)
    
try:
    t[0] = 1   # tuples are immutable
except TypeError as e:
    print(e)

try:
    print(t2.index(1))
except ValueError as e:
    print(e)
