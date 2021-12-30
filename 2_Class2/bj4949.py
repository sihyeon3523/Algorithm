'''
s = list(input())

for i in range(len(s)):
    top = s.pop()
    if top == '[':
        for j in range(i, len(s)):
            if s[j] == ']':
                s.pop(j)
            else:
                print('no')
            
    elif top == '(':
        for j in range(i, len(s)):
            if s[j] == ')':
                s.pop(j)
            else:
                print('no')
    elif top == ']' or top == ')':
        print('no')
    print(s)
'''

# 스택은 임의로 무언가를 담아두고 다른 것과 비교할 때 사용한다
while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = True

    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()
    
    if temp == True and not stk:
        print('yes')
    else:
        print('no')