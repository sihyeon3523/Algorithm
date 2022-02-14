# % : 몫이 아닌 나머지
# // : 소수점 이하의 수는 버리고, 정수 부분의 수만 구함
# / : 나누기 (정수가 아닌 형태로 나옴)

# n 이라는 수는 n//3을 연산적으로 돌리면, 즉 +1을 하면 만드 
# 점화식 dp(N) = min(dp(N//3)+1, dp(N//2)+1, dp(N-1)+1)

# 4시 20분 ~

n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    # 1을 뺀 경우
    dp[i] = dp[i-1] + 1

    # 2로 나누어 떨어진다 and (1을 뺀 경우 > 2로 나누는 경우)
    if i%2 == 0 and dp[i] > dp[i//2]+1:
        # 2로 나누는 경우로 변경 
        dp[i] = dp[i//2] +1
    
    # 3으로 나누어 떨어진다 and (1을 뺀 경우 > 3으로 나누는 경우)
    if i%3 == 0 and dp[i] > dp[i//3] + 1:
        # 3으로 나누는 경우로 변경 
        dp[i] = dp[i//3] + 1
print(dp[n])

