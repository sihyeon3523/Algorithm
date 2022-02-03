# 교집합 
# set : 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터역할로 종종 쓰인다
# list로 하면 시간초과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = set()
b = set()

for _ in range(n):
    tmp = input().strip()
    d.add(tmp) # set은 add로 값 추가 

for _ in range(m):
    tmp = input().strip()
    b.add(tmp)

cha = d&b # 교집합 

'''
set 함수 
교집합 
- s1 & s2 
- s1.intersection(s2)
합집합
- s1 | s2
- s1.union(s2)
차집합
- s1 - s2
- s1.difference(s2)
값 추가
- .add(4)
값 여러 개 추가
- .update([4,3,2])
특정 값 제거하기
- .remove(2)
'''

chalist = list(cha) # set to list 
chalist.sort()
# chalist = sorted(list(d&b)) --> 한번에 줄일 수도 있다 

print(len(chalist))
for x in chalist:
    print(x)