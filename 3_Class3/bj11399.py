# ATM --> 소요시간이 작은 수부터 배열 (그리디)
# S3 / 그리디 알고리즘 / 정렬 
# 3시 25분 ~ 37분

n = int(input())
t = list(map(int, input().split()))
t.sort() # 오름차순 
#print(t)

Sum = 0
for i in range(1, n+1):
    #print(t[0:i])
    Sum += sum(t[:i])

print(Sum)