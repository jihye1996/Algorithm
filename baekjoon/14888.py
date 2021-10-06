N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

arr = []
def tracking(i, sums, plus, minus, multiply, divide):
    global arr
    if i == N:
        arr.append(sums)
        return
    
    if plus:
        tracking(i+1, sums+nums[i], plus-1, minus, multiply, divide)
    if minus:
        tracking(i+1, sums-nums[i], plus, minus-1, multiply, divide)
    if multiply:
        tracking(i+1, sums*nums[i], plus, minus, multiply-1, divide)
    if divide:
        tracking(i+1, int(sums/nums[i]), plus, minus, multiply, divide-1)

tracking(1, nums[0], op[0], op[1], op[2], op[3])

print(max(arr))
print(min(arr))
