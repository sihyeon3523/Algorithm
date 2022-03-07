# 효율적인 화폐구성
# 4시 32분 ~
n, m = map(int, input().split()) # 화폐 개수, m원

'''
mininum한 값을 구분하자
'''
# 화폐 정보 입력 받기 
coin = [int(input()) for _ in range(n)]
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화 
array = [10001]*(m+1) # 최솟값을 구할 때는 최댓값을 기본 값으로 넣어준다 

# 다이나믹 프로그래밍 진행 (바텀업)
for i in range(1, m+1):
    for j in coin:
        if i % j == 0:
            array[i] = min(i//j, array[i])
        else:
            pass

# 계산된 결과 출력  
if array[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우 
    print(-1)
else:
    print(array[m])


# 계산량을 줄여주는 코드 
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])