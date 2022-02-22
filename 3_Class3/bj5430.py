# AC
# G5
# R(배열에 있는 수의 순서를 뒤집는 함수), D(첫번째 수를 버리는 함수)
# 함수를 조합해서 한번에 사용
# RDD : 배열을 뒤집고 처음 두 수를 버리는 함수
# 규칙 기반에 .popleft <-- deque

'''
중요 포인트 
Reverse를 매번 실행하지 않고, 뒤집는 횟수를 기억해두었다가

뒤집는 횟수가 홀수 번 일때만 뒤집도록 수정

특정 값 확인을 위해서는 변수를 이용
'''

# 2시 ~ 3시 46분 다른 사람 풀이 봤으며, 이해는 함 

# 시간초과 
from collections import deque
import sys

t = int(sys.stdin.readline()) # 테스트케이스의 개수 

for i in range(t):
    p = sys.stdin.readline() # 수행할 함수 
    n = int(sys.stdin.readline()) # 배열에 들어있는 수의 개수
    if n == 0:
        tmp = input()
        print('error')
        continue # 다음 순번의 loop로 돌도록 강제하는 것을 의미 
    
    q = deque(map(int, sys.stdin.readline().strip()[1:-1].split(','))) # deque 형태로 넣는다 

    try:

        for i in range(len(p)):
            if p[i] == 'R':
                q.reverse()
            elif p[i] == 'D':
                q.popleft()

        li = []
        for i in q:
            li.append(i)
        print(li)
    
    except:
        print('error')


from collections import deque
import sys

T = int(sys.stdin.readline()) # 테스트케이스 수

errFlag = False
for _ in range(T):
    p = sys.stdin.readline() # 함수
    n = int(sys.stdin.readline()) # 배열 속 수의 개수
    arr = sys.stdin.readline()[1:-2].split(',')

    # n= 0 일 때 처리 
    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()

    direction_Flag = True # R이 짝수개
    for i in p:
        if i == 'R':
            if direction_Flag == True: # 짝수개 있을 경우 
                direction_Flag = False
            elif direction_Flag == False: # 홀수 개 있을 경우
                direction_Flag = True
        
        elif i == 'D':
            if len(arr) == 0:
                print('error')
                errFlag = True
                break
            
            if direction_Flag == True: # 배열 안 뒤집는데(R이 짝수), 삭제할 경우
                arr.popleft()
            elif direction_Flag == False:
                arr.pop()
    
    if p.count('R') % 2 != 0: # R이 홀수 개 있음 즉, 뒤집어야 함 
        arr.reverse()

    if errFlag== False:
        print("[", end ="")
        for i in range(len(arr)):
            print(arr[i], end="")
            if i != len(arr)-1: # 배열의 길이만큼 돌아가..
                print(",", end ="")
        print("]")
    errFlag = False
