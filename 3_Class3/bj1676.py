n = int(input())

tmp = 1
for i in range(1, n+1):
    tmp = tmp*i

cnt = 0
for i in range(-1, -n, -1):
    if str(tmp)[i] == '0':
        cnt += 1
    else:
        break
print(cnt)

# 더 정갈한 풀이
from math import factorial
n = int(input())
cnt = 0

for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
print(cnt)

# 더 효율적인 풀이 --> 5로 나눠 떨어지는 수가 몇 개인지 알아야 한다
n = int(input())
def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt 
    
print(five_count(n))
