# 괄호

n = int(input())

for i in range(n):
    a = input()
    stk = []
    temp = True

    for j in a:
        if j == '(':
            stk.append(j)
            print("첫번째", stk)
        if j == ')':
            if not stk: 
                temp = False
                break
            else:
                stk.pop()
                print("두번째", stk)

    if temp == True and not stk:
        print('YES')
    else:
        print('NO')

