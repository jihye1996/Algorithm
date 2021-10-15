n, k = map(int, input().split()) 
coins = [int(input()) for _ in range(n)]
dp = [0] + [10001] * (k)

for i in range(n):
    for j in range(coins[i], k+1):
        dp[j] = min(dp[j], dp[j-coins[i]]+1)

print(dp[-1] if dp[-1] != 10001 else -1)
