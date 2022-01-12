'''
BFS : 너비 우선 탐색 
시작점인 루트 노드와 같은 거리에 있는 노드를 우선으로 방문 
2차원 배열에서 상, 하, 좌, 우 한 칸씩부터 우선으로 탐색하는 것을 의미함
큐(queue) 자료구조 : 노드를 방문하면서 인접한 노드 중 방문하지 않았던
노드의 정보만 큐에 넣고 먼저 큐에 들어있던 노드부터 방문하면 되는것이죠 
list.pop(0)의 시간복잡도 O(N)
collections 라이브러리의 deque 사용 
인접 노드 중 방문하지 않았던 노드를 큐에 넣을 때는 파이썬 데이터 타입 중 set을 사용하면 아주 쉽게 구현 가능
'''
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        # print("방문완료", visit)
        # print("미방문", queue)
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node]) 

    return visit

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        print('이미 넣음', visit)
        print('넣을 예정', stack )
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))
