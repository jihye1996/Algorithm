from collections import deque

def solution(bridge_length, weight, truck_weights):
    time, total = 1, truck_weights[0]
    bridge = deque([(1, truck_weights[0], 1)])
    
    while bridge:
        time += 1
        next_i = bridge[-1][2]
        if bridge[0][0] + bridge_length == time:
            total -= bridge.popleft()[1]
        
        if next_i < len(truck_weights) and total + truck_weights[next_i] <= weight:
            bridge.append((time, truck_weights[next_i], next_i + 1))
            total += truck_weights[next_i]

    return time

'''
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    while bridge:
        time += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        
    return time
'''
