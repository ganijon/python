# Time: O(2^n)
# Space: O(1)

# Recursively find Fibonnaci number
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)


print(f'fib(10):{fib(10)}')
print(f'fib(40):{fib(30)}')