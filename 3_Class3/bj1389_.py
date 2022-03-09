from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# start 노드에서 다른 노드로 갈 수 있을 때 
def bfs(graph, start):
    # num 리스트 안의 각각 인덱스에 맞는 값
    num = [0]*(n+1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                # num의 각각의 값에 이전에 더해진 값들을 더해준다 
                num[i] = num[a] + 1
                q.append(i)
                visited[i] = 1
    return sum(num)

result = []
# 친구들 각각 방문해서
for i in range(1, n+1):
    # 친구들 각각에 대한 방문 리스트를 만들어
    visited = [0 for _ in range(n+1)]
    # 그리고 bfs 를 돌리고 sum 값을 넣어
    result.append(bfs(graph, i))

# min(result)가 있는 index의 값을 가져온다 그리고 +1 해줘야지 (1부터 시작하니깐)
print(result.index(min(result)+1))
