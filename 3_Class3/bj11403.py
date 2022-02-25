# 3시 14분 ~
# 경로 찾기 
# i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램
#  
'''
플로이드 워셜 알고리즘
하나의 정점에서 다ㅡㄴ 하나의 정
다익스트라? 플로이드 워셜? 
'''

#입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
    
#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()