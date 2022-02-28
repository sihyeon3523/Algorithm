# 7시 39분 ~ 35분(다른 사람 코드 봄)
# G5
# 빈 칸, 치킨집, 집
# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리 
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# 거리는 유클라디안 거리로 구함
# 절댓값 함수 : abs() absolute() 절댓값 

'''
도시에 있는 치킨집 중에서 최대 M개를 고르고,
나머지 치킨집은 모두 폐업
도시의 치킨 거리가 가장 작게 될지 구하는 프로그램
0 빈 칸, 1 집, 2 치킨 집
'''
# 조합으로 푸는 거였따 = 결론

from itertools import combinations

# 맵 크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split()))for _ range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            chicken.append((i, j))

minv = float('inf') # 최대값

# 뽑힐 치킨의 조합 각각에 대해서 돌려봐 
# 최대 M개의 치킨집을 고를 수 있는데, 선택된 치킨집이 많으면
# 많을수록 거리가 최소가 될 가능성이 크다 그러므로 전체 치킨집 중에서 M개를 선택한다
for ch in combinations(chicken, M):
    sumv = 0
    
    # 각각의 조합에 있는 치킨집과 일반 집과의 거리 중 가장 작은 값 = 치킨 거리를 구해
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv:
            break
    
    # 치킨집 조합을 돌면서 가장 작은 값을 minv로 하고, 모든 조합의 치킨집을 돌면 최종 가장 작은 값이 minv로 들어감
    if sumv < minv:
        minv = sumv

# 모든 치킨집 조합 중 가장 작은 값을 출력 
print(minv)