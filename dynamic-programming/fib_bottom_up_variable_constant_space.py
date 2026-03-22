def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, cur = 0, 1
    print(f'i:{1}, p:{prev}, c:{cur}')
    
    for i in range(2, n + 1):
        prev, cur = cur, prev + cur
        print(f'i:{i}, p:{prev}, c:{cur}')

    return cur

print(fib(5))

# Time: O(n)
# Space: O(1)


"""
fib(5)

p,c=0,1
i:1   0,1
i:2   1,1
i:3   1,2
i:4   3,3
i:5   3,5
fib(5): 5
"""
