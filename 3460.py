T = int(input())
result = ''
for i in range(T):
    N = int(input())
    i = 0
    while 0 <  N:
        if N % 2 == 1:
            result += str(i)+' ' 
        N = N // 2
        i+=1
print(result)
