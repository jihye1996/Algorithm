from math import gcd

# a, b의 최소공배수 = a * b / 최대공약수(a, b)
def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = int(n * answer / gcd(n, answer))    
    return answer
