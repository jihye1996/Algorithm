def make_table(): # for finding previous index
    table = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = table[j - 1]
        if p[i] == p[j]:
            j += 1
            table[i] = j
    return table

def kmp():
    table = make_table()
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1] # find previous index 
        
        if s[i] == p[j]:
            if j == len(p) - 1:
                return 1
            else:
                j += 1
    return 0

s = input()
p = input()
print(kmp())
