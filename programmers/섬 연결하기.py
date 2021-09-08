def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    route = set({costs[0][0]})
    
    # 비용순으로 정렬했기 때문에 route에 못 들어가는 경우 발생
    # ex) [0, 1, 1], [3, 4, 1] 
    while len(route) != n:
        for i, cost in enumerate(costs):
            if cost[0] in route and cost[1] in route:
                continue
            if cost[0] in route or cost[1] in route:
                route.update([cost[0], cost[1]])
                #costs[i] = [-1, -1, -1]
                costs.pop(i)
                answer += cost[2]
                # 스킵한 것 중 연결할 수 있는 최소 비용이 있을 수 있으므로 다시 체크 필요
                break 
    return answer
