print("Practice tuples")

t = ()  # ()
t1 = (0, 1)  # (0, 1)
t2 = ('a', 'b', 'c')    # ('a', 'b', 'c') 
t3 = tuple(range(5,51,5)) # (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
t4 = tuple([_ for _ in 'xyz'])  #  ('x', 'y', 'z')

print(t, t1, t2, t3, t4)

print(t1[0]) # 0
print(t1.count(1)) # 1
print(t1.index(1)) # 1

for item in t3:
    print(item, end=' ') # 5 10 15 20 25 30 35 40 45 50

try:
    print(t[0])   # empty tuple, nothing at index 0
except IndexError as e:
    print(e) # tuple index out of range
    
try:
    t[0] = 1   # tuples are immutable
except TypeError as e:
    print(e) # 'tuple' object does not support item assignment
    

try:
    print(t2.index(1))
except ValueError as e:
    print(e) # tuple.index(x): x not in tuple
