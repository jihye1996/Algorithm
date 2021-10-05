def fina(n):
    if n <= 1:
        return n
    else:
        return fina(n-1) + fina(n-2)
    
        
N = int(input())
print(fina(N))
