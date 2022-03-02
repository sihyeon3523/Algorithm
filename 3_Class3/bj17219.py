# 메모장에서 비밀번호를 찾는 프로그램
# 사이트 주소와 비밀번호
# S4
# 7시 30분 ~

n, m = map(int, input().split())

# 딕셔너리 사용 --> 해시적 접근
memo = {}

for i in range(n):
    x, y = input().split()
    memo[x] = y

for j in range(m):
    s = input()
    print(memo[s])
