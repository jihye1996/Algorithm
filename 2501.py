arr=[]
N, K = map(int, input().split())
answer = 0
for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)
        if len(arr) == K:
            answer = arr[K-1]
            break
print(answer)
