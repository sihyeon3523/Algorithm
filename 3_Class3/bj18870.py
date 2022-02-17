# 좌표 압축 --> S2

# Xi를 좌표 압축한 결과 X'i
# X'i의 값 = Xi > Xj를 만족하는 서로 다른 좌표의 개수
# 압축한 결과 출력 

# 2시 50분 ~ 

# s = {} : dict
# s = set() : set

''' 시간초과 
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i] > a[j]:
            cnt += 1
    print(cnt, end = " ")
'''

# list.index(i) 형태의 시간 복잡도 = O(N)
# index[i] 형태의 시간 복잡도 = O(1)
import sys

n = int(sys.stdin.readline())
a = list(map(int, input().split())) # [2, 4, -10, 4, -9]

a2 = sorted(list(set(a))) # [-10, -9, 2, 4]
dic = {a2[i] : i for i in range(len(a2))} # {-10:0, -9:1, 2:2, 4:3}
for i in a:
    print(dic[i], end = ' ') # dic[--10] = 0, dic[-9] = 1, dic[2] = 2, dic[4]=3
    