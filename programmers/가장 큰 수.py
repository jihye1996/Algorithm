import functools

# -1: first arg is smaller, 0: equl, 1: first arg is greate
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) # 아스키코드로 변환해서 한개씩 비교 
    #numbers.sort(key=functools.cmp_to_key(comparator), reverse=True)
    
    return str(int(''.join(numbers)))
