maxs = 0						
def tracking(c_i, K, bits_array, start, text_set, text_bit, bit):	
    if c_i == K:
        global maxs	
        total, tmp = 0, 0
        for b in bits_array:
            tmp += b
        for t in text_bit:
            if tmp & t == t:
                total += 1
        maxs = max(maxs, total)
        return				
    				
    for i in range(start, len(text_set)):	
        bits_array.append(bit[text_set[i]])
        tracking(c_i+1, K, bits_array, i+1, text_set, text_bit, bit)	
        bits_array.pop()		
# end def tracking()					
    						
N, K = map(int, input().split())						
must = set(['a', 'c','i', 'n', 't'])
	
bit = {chr(ord('a') + i): 1 << i for i in range(26)}
K, text_set, input_bit = K-len(must), set(), []					
						
for _ in range(N):	
    text = set(input().rstrip()) - must
    text_set |= text
    bit_sum = 0
    for t in text:
        bit_sum += bit[t]
    input_bit.append(bit_sum)
    
    
if len(text_set) <= K:
    # 모든 단어 학습 가능
    print(N)
elif 0 < K:	
    tracking(0, K, [], 0, list(text_set), input_bit, bit)		
    print(maxs)
else:
    # 학습불가능
    print(0)
