# 투 포인터 방식 1
H, W = map(int,input().split())
rains = list(map(int,input().split()))
left, right, total = 0, W-1, 0
left_max, right_max = rains[left], rains[right]

while left < right:
    left_max = max(left_max, rains[left])
    right_max = max(right_max, rains[right])
    
    
    if left_max < right_max:
        total += (left_max - rains[left])
        left += 1
    else:
        total += (right_max - rains[right])
        right -= 1

print(total)

'''
# 투 포인터 방식 2
H, W = map(int,input().split())
rains = list(map(int,input().split()))
total = 0
 
for i in range(1, W-1):
    left = max(rains[:i])
    right = max(rains[i+1:])
    middle = min(left, right)
    
    if rains[i] < middle:
        total += (middle - rains[i])
        
print(total)
'''
