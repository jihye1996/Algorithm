def solution(money):
    dp = [0 for i in range(len(money))]
    
    for i in range(len(money)):
        dp[i] = odd += money[2*i]
        even += money[2*i+1]

    answer = max(odd, even)

    if len(money) % 2 == 1:
        answer  = max(answer, odd - money[0] + money[-1])

    print(answer)
    return answer
