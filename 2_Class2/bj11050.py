'''
n, k = map(int, input().split())

a = 1
b = 1
# 내 풀이 
c = 1

for i in range(1, n+1):
    a *= i

for i in range(1, k+1):
    b *= i


for i in range(1, n-k+1):
    c *= i

print(int(a/(b*c)))
'''
# 함수 이용
from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k)*factorial(n-k))
print(b)