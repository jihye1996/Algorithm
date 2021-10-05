from math import gcd
x, y = map(int, input().split())
print(gcd(x,y))
print(int(x*y/gcd(x,y)))
