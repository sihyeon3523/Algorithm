# 리스트로 하면 시간 초과 --> dict로 풀어야 함
import sys 
n , m  = map(int, sys.stdin.readline().split())

dogam = []

for i in range(n):
    dogam.append(sys.stdin.readline().strip()) # strip() : 개행 문자 제거 

# print(dogam)

for j in range(m):
    tmp = sys.stdin.readline().strip()

    if tmp.isdigit():
        print(dogam[int(tmp)-1])

    elif tmp.isalpha():
        print(dogam.index(tmp)+1) # .index(tmp) : tmp 가 있는 index 반환 --> 시간초과  

# dictionary 가 list보다 검색 속도가 빠르다
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])