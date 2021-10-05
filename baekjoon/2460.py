max_p = 0
cur_p = 0

for _ in range(10):
    outs, ins  = map(int, input().split()) 
    cur_p += ins - outs
    max_p = max(max_p, cur_p)
print(max_p)
