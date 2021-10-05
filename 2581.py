S = int(input())
E = int(input())
arr = []

for i in range(S, E+1):
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            flag = False
            break
    if 1<i and flag: 
        arr.append(i)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print('-1')
