s = input()
stack = []

for v in s:     

    if v in ('(', '['):
        stack.append(v)
    else:
        if stack and v == ')':
            temp = []
            while stack:
                top = stack.pop()
                if str(top).isdigit(): 
                    temp.append(top)
                elif top == '(' and temp:
                    stack.append(2*sum(temp))
                    break
                elif top == '(' and 0 == len(temp):
                    stack.append(2)
                    break
                else:
                    print("0")
                    exit(0)   
        elif stack and v==']':
            temp = []
            while stack:
                top = stack.pop()   
                if str(top).isdigit(): 
                    temp.append(top)
                elif top == '[' and temp:
                    stack.append(3*sum(temp))
                    break
                elif top == '[' and 0 == len(temp):
                    stack.append(3)
                    break
                else:
                    print("0")
                    exit(0)   
    
        else:
            print("0")
            exit(0)   

total = 0
for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        total += i
 
print(total)
