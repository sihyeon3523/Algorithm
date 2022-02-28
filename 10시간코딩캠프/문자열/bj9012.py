# 괄호
# S4
# 5시 38분 ~ 56분
# 주어진 괄호 문자열이 VPS 인지 아닌지를 판단

'''
문제 풀이 방법
- 체크 해야 할 게 있다면? 새로운 변수로 설정해서 체크해도 된다 
'''
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    s = input().rstrip()
    visited = [0]*len(s)

    for j in range(len(s)):
        if s[j] == "(" and visited[j] == 0:
            for k in range(j+1, len(s)):
                if s[k] == ")" and visited[k] == 0:
                    visited[k] = 1
                    visited[j] = 1
                    break
        else:
            continue
    if 0 in visited:
        print("NO")
    else:
        print("YES")

# 스택을 이용한 풀이
n = int(input())

for i in range(n):
    a = input()
    stk = []
    temp = True 

    # "("인 위치를 스택에 넣어주고, ")"를 만날 때마다 스택에 값이 있는지 확인
    # 없다면? VPS가 아니므로 temp값을 False로 바꿔준다. 
    for j in a:
        if j == "(":
            stk.append(j)
        if j == ")":
            if not stk:
                temp = False
                break
            else:
                stk.pop()
    
    # 스택에도 값이 없어야 하고, temp 값도 True여만 VPS 
    if temp == True and not stk:
        print("YES")
    else:
        print("NO")