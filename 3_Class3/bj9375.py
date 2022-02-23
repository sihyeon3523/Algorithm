# 조합
# S3
# 안경, 코트, 상의, 신발
# + 바지 렌즈 
from collections import Counter

n = int(input()) # 테스트 케이스 수

for _ in range(n):
    m = int(input()) # 의상 수
    s = []
    for j in range(m):
        a, b = input().split()
        s.append(b) # 특별히 매칭하는게 아니라 그저 숫자만 구함 

    num = 1
    result = Counter(s) 
    for key in result:
        num *= result[key]+1 # +1의 의미는 그 의상을 착용할 때 안할때
    print(num-1) # -1의 의미 모든 의상을 착용하지 않은 경우

t = int(input())

for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]
    
    cnt = 1 # 각 종목마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)