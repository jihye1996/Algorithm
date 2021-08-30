def solution(t, l=[]):
    for r in t: 
        '''
        가장자리에 0을 추가해 zip으로 만들고 연산 처리
        ex) [0, 10, 15] [10, 15, 0] [8, 1, 0] => [18, 16, 15]
        
        temp = []
        for t,y,z in zip([0]+l,l+[0],r):
            #print(t, ' ', y, ' ', z)
            temp.append(max(t,y)+z)
        l = temp
        print(l)
        '''
        l=[max(t,y)+z for t,y,z in zip([0]+l,l+[0],r)]

    return max(l)
  
'''
def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] = max(triangle[i][j]+triangle[i-1][j-1],
                                triangle[i][j]+triangle[i-1][j])

    return max(triangle[-1])
'''
