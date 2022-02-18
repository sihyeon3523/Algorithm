# S3
# 4시 9분 ~ 50분

# 계단을 밟으면 그 점수를 얻는다
# 한 계단 or 두 계단 
# 한 계단 밟는 건 1번까지만 (시작은 포함 안함 )
# 마지막 도착 계단은 반드시 밟아야함 --> 뒤에서부터 시작하며 풀이 시작
# 총점의 최댓값? 

# 마지막 계단을 end라고 한다면 그 전의 계단은 end - 1계단이거나 end -2 계단 일 것
# end - 1일 경우 반드시 end -2를 밟으면 안된다(세개 계단을 연속으로 밟게 된다)
# end - 2일 경우 그 전 계단은 신경 쓰지 않는다 
# dp[i] = max(dp[i-2]+arr[i], dp[i-3] + arr[i-1] + arr[i])

import sys
input = sys.stdin.readline
arr = []
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))

# 첫번째 계단 
dp.append(arr[0])

# 두번째 계단 
dp.append(arr[0]+arr[1]) # 한 계단, 두 계단 

# 세번째 계단 
dp.append(max(arr[0]+arr[2], arr[1]+arr[2])) # 두계단, 한계단 

for i in range(3, l):
    dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i]))

print(dp.pop())

# -->런타임 에러난다 : 최고 한 계단 밖에 없을 경우 아무런 값이 없는 리스트에 접근해야 하기 때문에 에러나는 듯


N = int(input())

stair = [0]
for _  in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    
    print(dp.pop())