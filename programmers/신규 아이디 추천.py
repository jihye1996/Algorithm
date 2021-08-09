import re
def solution(new_id):
    answer = re.sub(r"[^a-z0-9\.\_\-]", "", new_id.lower()) # 1~2
    answer = re.sub(r"\.{2,}", ".", answer) # 3
    answer = re.sub(r"^\.|\.$", "", answer) # 4
    answer = 'a' if len(answer) == 0 else st[:15] # 5, 6
    answer = re.sub(r"\.$", "", answer) # 6
    
    # 7
    if len(answer) < 3:
        for i in range(3-len(answer)):
            answer += answer[-1:]
        
    return answer
