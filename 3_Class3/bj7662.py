# 이중 우선순위 큐
# 큐 --> FIFO
# 삽입
# 삭제(우선순위가 가장 높은 것 삭제 or 우선순위가 낮은 거 삭제)
# 정수의 값 자체를 우선순위 
# 3시 45분 ~ 5시 40분 

''' 이걸로 푸는 거 아님 ㅠㅠ 
from collections import deque

t = int(input()) # 테스트 데이터 개수

for j in range(t):
    k = int(input()) # 연산의 개수
    q = deque()
    for i in range(k):
        a, b = input().split() # D, n
        if a == "I":
            q.append(int(b))
            print(q, int(b))
        elif a == "D" and not q:
            pass
        elif a == "D" and b == '1':
            
            print("최댓값", q.pop()) # 최대값 : 오른쪽에서 출력
        elif a == "D" and b == '-1':
            print("최소값", q.popleft()) # 최소값 : 왼쪽에서 출력 
    print("정렬", sorted(q))
    if not q:
        print('EMPTY')
    else:
        print(max(q), ' ', min(q))
'''

# 최소힙과 최대힙 2개를 두고 동기화 필요
import sys
read = sys.stdin.readline
import heapq

result = []
for T in range(int(read())):
    visited = [False]*1000001 # id별로 활성상태를 확인하기 위한 플래그 리스트  False 삭제된 상태이자 입력되지 않은 상태 
    minH, maxH = [], [] # 최소힙과 최대힙 따로 생성

    for i in range(int(read())):
        s = read().split()
        if s[0] == 'I':
            heapq.heappush(minH, (int(s[1]), i)) # 튜플은 첫번째 값 기준으로 비교 연산 
            heapq.heappush(maxH, (-int(s[1]), i)) # 튜플은 첫번째 값 기준으로 비교 연산
            visited[i] = True # True이면 어떤 힙에서도 아직 삭제되지 않은 상태 

        elif s[1] =='1': # 최대값을 삭제하는 연산, 삭제 연산 시 key 값을 기준으로 해당 노드가 다른 힙에서 삭제된 노드인가를 먼저 판단한다
            # 이미 상대힙에 의해 삭제된 노드인 경우 삭제되지 않은 노드가 나올때까지 계속 버리다가(pop으로 꺼내서 없앤다) 이후 삭제대상 노드가 나오면 삭제한다 
            while maxH and not visited[maxH[0][1]]: # visited이 False일 때 --> 해당 노드가 삭제된 상태 (max갑 자체를 검색을 했는데 해당 노드가 삭제되었다면)
                heapq.heappop(maxH) # 버림 (상대 힙에서 이미 삭제된 노드이므로) print 자체를 안하기 때문에 heap에서 버린다.. 그 값을! 버린다 이미 다른 노드에서 삭제했으니깐 
            
            if maxH:  # 삭제 대상 노드가 나왔으므로 삭제 즉, visited가 True인 값이 나왔으므로 삭제 
                visited[maxH[0][1]] = False # visit이 True였으므로 False로 바꾼다 즉, 내가 삭제함
                heapq.heappop(maxH) # 삭제대상 노드를 삭제하자 즉, 최대값을 삭제하자 

        else:
            while minH and not visited[minH[0][1]]: # 이미 삭제된 노드인 경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                heapq.heappop(minH)
            
            if minH:
                visited[minH[0][1]] = False #  visit이 True였으므로 False로 바꾼다 즉, 내가 삭제함 
                heapq.heappop(minH) 
    
    # 모든 연산이 끝난 후에도 쓰레기 노드가 들어갈 수 있으므로, 결과를 내기전에 모두 비우고 나서 각 힙의 첫번째 원소값을 출력한다 
    while minH and not visited[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    
    result.append(f'{-maxH[0][0]} {minH[0][0]}' if maxH and minH else 'EMPTY' )

print('\n'.join(result))



'''
삭제 연산할 때 동기화가 필요
최대힙과 최소힙을 따로 만들기 때문에, 삭제하려는 값이 최대힙에서 삭제된건지 아닌지 판단하기 위한
즉, id별로 활성상태를 기록하는 플래그 리스트인 visited를 사용해야 하기 때문입니다. 
삭제 연산 시, 먼저 이 ID 를 기준으로 해당 노드가 다른 힙에서 삭제한 노드인가를 판단합니다. 
이미 삭제된 노드일 경우 삭제되지 않은 노드가 나올때까지 모두 버립니다. 
이후 삭제 대상 노드가 등장하면 삭제합니다. 
이를 위해 각 ID별로 활성상태를 기록하는 플래그 리스트인 visited를 사용합니다. 
'''