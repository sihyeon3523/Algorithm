# 연결되어 있는 것들은 다 바이러스 걸림

# 1번 컴퓨터가 웜 바이러스에 걸릴 때,1번 컴퓨터를 통해 웜
# 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오

# 컴퓨터의 수 <= 100
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
# 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는
# 컴퓨터의 번호 쌍이 주어진다

'''
결론적으로는,
dfs 가 bfs 보다 메모리도 덜 차지하고 시간도 덜 걸림
bfs는 덱을 써야 해서 메모리가 좀 더 필요했던 것 같고,
아무래도 .popleft() 와 같은 것들을 해야해서 시간이 오래 걸린 듯 싶다 
'''

# 너비 우선 탐색 풀이 

from collections import deque

def bfs(n):
    cnt = 0
    q = deque()
    q.append(n)
    visit_list[n] = 1
    while q:
        v = q.popleft()
        for i in range(1, cn+1):
            if visit_list[i] == 0 and net[v][i] == 1:
                q.append(i)
                visit_list[i] = 1
                cnt += 1
    return cnt

cn = int(input())
nn = int(input())

net = [[0]*(cn+1) for _ in range(cn+1)]
visit_list = [0]*(cn+1)

for i in range(nn):
    a, b = map(int, input().split())
    net[a][b] = net[b][a] = 1

print(bfs(1))



# 깊이 우선 탐색

def dfs(n):
    global cnt 
    visit_list[n] = 1
    for i in range(1, cn+1):
        if visit_list[i] == 0 and net[n][i] == 1:
            cnt += 1
            dfs(i) 

cn = int(input())
nn = int(input())

cnt = 0 # global variable 
net = [[0]*(cn+1) for _ in range(cn+1)]

visit_list = [0]*(cn+1)

for i in range(nn):
    a, b = map(int, input().split())
    net[a][b] = net[b][a] = 1

dfs(1)
print(cnt)

# 다른 사람 풀이 - dfs

def dfs2(graph, v, visited):
    global cnt
    visited[v]  = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

PC = int(input())
network = int(input())

graph = [[] for _ in range(PC+1)] # 빈칸으로 선언
visited = [False]*(PC+1)
cnt = 0

for i in range(network):
    node1, node2 = map(int, input().split())

    # graph : [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]] 
    graph[node1].append(node2) # 각 노드와 연결된 것을 리스트 형태로 값을 input
    graph[node2].append(node1)

dfs2(graph, 1, visited)
print(cnt)
print(graph)