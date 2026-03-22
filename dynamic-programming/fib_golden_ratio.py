def fib(n):
    golden_ratio = (1 + 5**0.5) / 2
    return int(round(golden_ratio**n) / 5**0.5)


# Time: O(1)
# Space: O(1)

# OverflowError: (34, 'Result too large') at:
# golden_ratio**n
print(fib(6000)) 
