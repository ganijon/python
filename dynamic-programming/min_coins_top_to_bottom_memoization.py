# Time: O(k*m)
# Time w/o memo: O(k^m)
# m - target sum
# k - number of coins


# Add memoization using a dictionary
memo = {}

# Recursively find minimum number of 
# coins required for target sum m

def min_coins(m, coins) -> int:
    print(f"min_coins({m})")
    
    if m in memo:
        return memo[m]  # Return cached result

    if m == 0:
        return 0  # solution found

    answer = None
    for coin in coins:
        subproblem = m - coin
        if subproblem < 0:
            continue  # no solution

        sub_result = min_coins(subproblem, coins)
        if sub_result is not None:
            answer = min_ignore_none(answer, sub_result + 1)

    memo[m] = answer  # Cache the result
    return answer


def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


print(min_coins(13, [5, 4, 1]), memo)
