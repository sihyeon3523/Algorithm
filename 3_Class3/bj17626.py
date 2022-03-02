# Four Squares
# 7시 55분 ~

# 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램

n = int(input())
d = [0]*(n+1)
d[1] = 1

for i in range(2, n+1):
    minValue = 1e9 # 1*109 = 1000000000
    j = 1
    
    while (j**2) <= i:
        minValue = min(minValue, d[i-(j**2)])
        j += 1
    
    d[i] = minValue + 1

print(d[n])