import heapq
def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    
    while(heap[0] < K and 1 < len(heap)):
        newValue = heapq.heappop(heap) + 2 * heapq.heappop(heap)
        heapq.heappush(heap, newValue)
        answer += 1
    
    if heap[0] < K:
        return -1
    else:
        return answer
