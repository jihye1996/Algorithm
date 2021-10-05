arr = []
for _ in range(9):
    arr.append(int(input()))

arr.sort()
target = sum(arr)-100
S, E = 0, 8

while True:
    if arr[S]+arr[E]<target:
        S+=1
    elif arr[S]+arr[E]>target:
        E-=1
    else:
        break

for i in range(9):
    if i not in (S, E):
        print(arr[i])
