T = int(input())
arr = list(map(int, input().split()))
count = 0
for v in arr:
    flag = True
    for i in range(2, int(v**0.5) + 1):
        if v % i == 0:
            flag = False
            break
    if 1<v and flag: 
        count += 1

print(count)
