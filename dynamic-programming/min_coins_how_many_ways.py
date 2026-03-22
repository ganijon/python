# Time complexity: O(m*k)
# Space complexity: O(m)

def coins_how_many_ways(m, coins):
    print(f"\n m={m}  coins={coins}")

    memo = {0: 1}

    for i in range(1, m + 1):
        memo[i] = 0
        
        print(f"  i={i} in {range(1,m+1)}, memo={memo}")
        
        for coin in coins:
            subproblem = i - coin
            
            print(f"    coin={coin}, subproblem={subproblem}")

            if subproblem < 0:
                continue

            print(f"      memo[{i}]={memo.get(i)}, memo[{subproblem}]={memo.get(subproblem)}")
            
            memo[i] = memo[i] + memo[subproblem]
            
            print(f"      memo[{i}]={memo.get(i)}, memo={memo}")
    
    return memo[m]


print(f"\n coins_how_many_ways(3,[1,2,3]): {coins_how_many_ways(2, [1, 2, 3])}\n")
