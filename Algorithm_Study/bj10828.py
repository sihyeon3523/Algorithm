# 4시 40분 ~
'''
리스트 관련 함수들 기억하자 
.append() 리스트에 요소 추가
.sort() 리스트 정렬
.reverse() 리스트 뒤집기 
.index(x) x의 위치 반환 
.insert(a, b) a번째 위치에 b를 삽입
.remove(x) 첫번째에 나오는 x 삭제
.pop() 리스트의 맨 마지막 요소 돌려주고 삭제
.count(x) 리스트 안에 x가 몇 개 있는지 조사하여 그 개수 돌려줌 
.extend(x) x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더함 
'''
import sys
input = sys.stdin.readline
n = int(input())
queue = []

for i in range(n):
    cont = list(input().split())
    if cont[0] == "push":
        queue.append(int(cont[1]))
       # print(queue)
    
    elif cont[0] == "top":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    
    elif cont[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif cont[0] == "size":
        print(len(queue))

    elif cont[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
