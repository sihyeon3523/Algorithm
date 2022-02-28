# 조합 0의 개수
# 1시 35분 ~ 2시 37분 

'''
시간초과 : 단순 팩토리얼을 이용하여 풀면 n, m 이 20억이될 수 있기 때문에 시간초과 또는 메모리 초과
n, m = map(int, input().split())
a = n-m
result = 1
for i in range(n, n-m, -1):
    result *= (i/(i-a))

print(str(int(result)).count('0'))
'''
n, m = map(int, input().split())


def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))