import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [0 for i in range(K+1)]
coins[0] = 1

for _ in range(N):
    coin = int(input())
    for j in range(coin, K+1):
        coins[j] += coins[j-coin]

print(coins[K])
    
