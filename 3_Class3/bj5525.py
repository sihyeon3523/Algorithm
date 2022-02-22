# IOIOI 
# S2
# O가 몇 개 ? 
# 4시 ~ 4시 50분 
'''
1번 풀이는 비교 문자열의 길이가 2N+1 이고, 
주어진 문자열은 M이니 비교 연산이 O(N*M) 인데 반해서
2번 풀이는 IOI 단위로 카운트하기 때문에 O(M) 으로 비교를 한다. 
N*M 10^12 이기 때문에 제한시간 내의 처리가 되지 않는다. 
참고로 파이썬은 1초에 2000만번 의 연산이 가능하다 
즉, 1초에 2* 10^8 번 최대 가능한 것 
N의 범위가 1,000,000인 경우 : O(logN)인 알고리즘을 설계 해야 한다.
[Python] 시간복잡도, 공간복잡도
https://yeonstory.tistory.com/3
'''
# 1번 풀이 : 50점 
import sys
input = sys.stdin.readline

n = int(input())
m = int(input()) # 문자열 M 
s = input()

tmp = 'IO'*n+'I'  
le = len(tmp) # 문자열의 길이 2N+1

cnt = 0
for i in range(m-le+1):
    if s[i] == 'I' and s[i:i+le] == tmp: # 비교 연산 O(N*M)
        cnt += 1
print(cnt)

#print(tmp[0:0+le]) # 맨 뒤에 값은 포함 안함

# 2번 풀이 : 100점 
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

answer = 0
count = 0
i = 1

while i < M -1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)