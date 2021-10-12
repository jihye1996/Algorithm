# 21.10.12: 수정 필요 
# 10 0, 1 1 1 1 1 1 1 1 1 1 케이스 틀림
N, S = map(int, input().split())
N_list = list(map(int, input().split()))

left, right, total = 0, 0, N_list[0]
min_len = 100001
index = 1
while left < N-1: 
    if S <= total:
        min_len = min(min_len, right - left + 1)
        total -= N_list[left]
        left += 1
    else:
        if right < N - 1:
            right += 1
            total += N_list[right]
        else:
            total -= N_list[left]
            left += 1

    #print(index, ': ', left, ' ', right, ' ', total, ' ', min_len)
    index+= 1
if min_len == 100001:
    print(0)
else:
    print(min_len)
