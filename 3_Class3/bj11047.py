# S3
# 그리디 --> 동전 개수의 최솟값
# 가장 큰 거부터 넣으면 ? 되잖아 
# 동전은 서로 배수
# 4시 20분 ~ 

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dong = []
for i in range(n):
    dong.append(int(input()))

don = 0
for i in range(n-1, -1, -1): # min(start) max(end) grap 
    if k == 0:
        break
    if dong[i] > k:
        continue
    don += k // dong[i] # 나눈 몫
    k %= dong[i] # 나눈 나머지

print(don)