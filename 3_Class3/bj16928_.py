'''
import sys
from collections import deque

input = sys.stdin.readline

# bfs 로 푸는 문제 즉, 큐 사용! 
def solve(n, m):

    snake = [0 for _ in range(101)]
    ledder = [0 for _ in range(101)]

    visited = [False for _ in range(101)]

    # 사다리 정보 가져왕
    for i in range(n):
        x, y = map(int, input().split())
        ledder[x] = y

    for j in range(m):
        x, y = map(int, input().split())
        snake[x] = y
    
    q = deque()

    # 처음 위치 q에 넣자! (위치, 이동 횟수)
    q.append((1,0))
    visited[1] = True

    ans = float("inf")

    while q:
        front = q.popleft()

        if front[0] == 100:
            # 이동 횟수가 제일 작은 값은 무엇? 
            ans = min(ans, front[1])
            continue

        for i in range(1, 7):
            new = front[0] + i
            # 이미 들린 곳인가? 그럼 다음 위치 이동
            if visited[new] == True:
                continue
            visited[new] = True
            
            # 뱀이 있는 곳인가? 
            if snake[new] != 0:
                # 그럼 뱀 타고 이동해야지
                new = snake[new]
            
            # 사다리를 만났다면? 
            if ledder[new] != 0:
                # 그럼 사다리 타고 이동해야지
                new = ledder[new]
            
            # 이동한 위치, 이동 횟수 q에 넣자
            q.append((new, front[1]+1))
    
    print(ans)


# 인터프리터가 직접 실행했을 경우에만 if문 내의 코드를 돌려라
if __name__ == "__main__":
    n, m = map(int, input().split())
    solve(n, m)
'''

import sys
from collections import deque

input = sys.stdin.readline
   
def solve(n,m) :
    
    snake = [0 for _ in range(101)]
    ledder = [0 for k in range(101)]
    #합쳐서 관리하는게 더 나을 것 같다.
    
    visited = [False for _ in range(101)]

    for i in range(n) :
        x , y = map(int,input().split())
        ledder[x] = y
    
    for j in range(m) :
        x , y = map(int,input().split())
        snake[x] = y

    q = deque()

    q.append((1,0))
    visited[1] = True

    ans = float("inf")

    while q :
        
        front = q.popleft()

        if front[0] == 100 :
            ans = min(ans, front[1])
            continue


        for i in range(1,7) :
            new = front[0]+i
            
            if new > 100 :continue
            
            if visited[new] == True :
                continue
            
            visited[new] = True

            if snake[new] != 0 :
                new = snake[new]
            
            if ledder[new] != 0 :
                new = ledder[new]

            q.append((new,front[1]+1))
    
    print(ans)
        
        
n,m = map(int,input().split())
solve(n,m)