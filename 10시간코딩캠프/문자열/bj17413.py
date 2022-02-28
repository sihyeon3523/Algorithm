# 4시 27분  ~ 59분 (혼자 못 풀었다..)
# 태그는 단어가 아니며, 단어만 뒤집는다 
# 구현

# isalnum(): 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열

import sys
word = list(sys.stdin.readline().rstrip()) # 중간에 있는 공백까지 리스트로 저장
# 문자열 =  바로 리스트 전환 가능 
print(word)

i = 0
start = 0

while i < len(word):
    if word[i] == "<":  # 열린 괄호를 만나면 
        i += 1
        while word[i] != ">": # 닫힌 괄호를 만날 때까지
            i += 1
        i += 1 # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i] # 숫자, 알파벳 범위에 있는 것들을
        tmp.reverse()
        word[start:i] = tmp
    else: # 괄호도 아니고 알파, 숫자도 아닌 것 = 공백 
        i += 1

print("".join(word))

'''
큐와 스택을 이용한 풀이
- 순서가 바뀌지 않는 것을 deque에 넣고, 바뀌지 않는 것을 stack에 넣는다. 
- 상태변수를 하나 선언해서


- <> 안에 있는 문자는 deque에 넣고, 꺼낼 때 popleft() 를 이용해
순서대로 나오게 해 순서를 유지시킨다. 
- 단어는 stack에 넣어 출력시 순서를 뒤집어 나올 수 있게 해준다. 
- 상태변수를 만들어 "<"를 만나면 그 전까지 스택에 저장되어 있던 단어들을 결과값에 거꾸로 저장해준다. 
- 그리고 "태그 안"이라는 뜻으로 False로 바꾸어준다. 
- ">"를 만나면 태그가 끝났으므로, 상태를 True로 바꾸어준다. 
- 문자들은 현재 상태가 False 상태이면 큐에 넣어주고, True이면 스택에 넣어준다. 
- 문자들을 끝까지 다 살펴보고 나면 스택에 남아있는 문자가 없는지 조사하고 있으면 모두 
'''

'''
스택? LIFO : 넣어준 것과 반대의 결과를 pop 할 수 있다
'''

import sys
from collections import deque
q = deque()     # <> 안에 있는 문자 (q.popleft() 사용해서 뒤집지 않고 출력)
stack = []      # 뒤집어야 할 단어 넣기 
result = ''     # 최종 문자 결과 담기 위함 
state = True    # 상태 체크를 위한 변수

word = list(sys.stdin.readline().strip())
for i in word:
    if i == "<":                  # "<" 입력 받으면  
        while stack:
            result += stack.pop() # 원래 순서와 거꾸로 저장
        q.append(i)               # "<" 큐에 저장
        state = False             # <, > 안의 문자들은 큐에 저장해야 하므로 상태변수 False로 변경
    
    elif i == ">":                # ">"을 입력 받으면
        q.append(i)               # 큐에 저장
        state = True              # <, > 괄호가 끝났으므로 상태변수 True
        while q:                  # 괄호 안에 있던 문자 모두 결과 값에 저장 
            result += q.popleft()       # 순서 그대로 나와야 하므로 deque에서 popleft()
    
    elif i == " ":                # 공백 입력 받았는데
        if state:                 # 괄호 밖의 상태라면 
            while stack:          # stack에 저장되어 있는 것들 다 결과 값에 저장
                result += stack.pop()
            result += " "
        else:
            q.append(i)
            while q:
                result += q.popleft()
    else:
        if state:
            stack.append(i)
        else:
            q.append(i)

while stack:
    result += stack.pop()

print(result)
