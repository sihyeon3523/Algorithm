# S3
# 파도반 수열
# DP
# [N] = [N-5] + [N-1]
# 6시 10분 ~ 

n = int(input()) # 테스트 케이스의 수
arr = [int(input()) for _ in range(n)]

s = [1,1,1,2,2]

for i in range(5, max(arr)):
    s.append(s[i-1]+s[i-5])

for i in arr:
    print(s[i-1])
