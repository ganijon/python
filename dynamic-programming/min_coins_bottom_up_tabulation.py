# Time complexity: O(m*k)
# Space complexity: O(m)

def min_coins(m, coins):
    memo = {0: 0}
    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
    return memo[m]


def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


print(f"\n min_coins(3,[1,2,3]): {min_coins(3, [1, 2, 3])}\n")
