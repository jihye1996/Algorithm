a,b = map(int,input().split())
arr = []
i = 1

while len(arr) <= b:
    arr.extend([i]*i)
    i+=1

print(sum(arr[a-1:b]))
