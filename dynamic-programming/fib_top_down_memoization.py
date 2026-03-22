def fib(n):
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x - 1) + f(x - 2)
            return memo[x]
    
    return f(n)


# Time: O(n)
# Space: O(n)

# Uses recursion that fails at large numbers
print(fib(6000))
