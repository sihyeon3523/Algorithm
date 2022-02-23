# 카잉 달력
# S1
# m, n 작거나 같은 두 개의 자연수 x,y를 가지고 각 년도를 <x:y>
# 와 같은 형식으로 표현 
# 첫번째 해 <1:1> 두번째 해 <2:2> <x':y'>

def num(m, n, x, y):
    while x <= m*n:
        if (x-y)%n == 0: 
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))