# 2xn 타일링 --> 1*2 2*1 --> DP
# 3시 50분 ~ 4시 14분 
# S3

# 재귀로 하면 시간초과 뜸 --> 리스트를 미리 정의해야 함 
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
a = [1, 2, 3]

def sol(e):
    if e == 1:
        return a[0]
    elif e == 2:
        return a[1]
    elif e == 3:
        return a[2]
    else:
        return sol(e-1) + sol(e-2)

print(sol(n)%10007)

# 리스트를 미리 정의
n = int(input())

dp = [0,1,2]

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n]%10007)