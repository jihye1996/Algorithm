N, S = map(int, input().split())
N_list = list(map(int, input().split()))

left, right, total = 0, 0, 0
min_len = 100001
while True: 
    if S <= total:
        min_len = min(min_len, right - left)
        total -= N_list[left]
        left += 1
    else:
        if right == N:
            break
        else:
            total += N_list[right]
            right += 1
if min_len == 100001:
    print(0)
else:
    print(min_len)
