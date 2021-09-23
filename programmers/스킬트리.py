import re
def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        tree = re.sub('[^'+skill+']', '', tree)
        if skill[0:len(tree)] == tree[0:len(tree)]:
            answer += 1
    return answer
