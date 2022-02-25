# 3시 14분 ~
# 경로 찾기 
# i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램
#  

n = int(input())
G = []

for i in range(n):
    G.append(input().split())

# 플로이드-워셜 알고리즘 
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            if G[i][j] == 1 or (G[i][k] == 1 and G[k][j]==1)

#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()