# 바닥공사
# 3시 58분 ~
# 타일 만드는 거 전형적인 DP 문제 
# 큰 문제를 작은 문제로 만들 수 있고, 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다 

n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [0]*1001

# 다이나믹 프로그래밍 진행 (보텀업)
d[1] = 1
d[2] = 3

if n <= 2:
    print(d[n])
else:
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]*2
    print(d[n])