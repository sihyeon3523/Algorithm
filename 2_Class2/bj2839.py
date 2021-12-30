'''
sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1 #5의 배수가 될 때까지 설탕 -3, 봉지 +1
else:
    print(-1)
'''
# 설탕 배달 문제를 DP로 풀어보자

n = int(input())

# (n+5) : n 값이 5보다 작은 경우 Index Out of Range 오류를 잡기 위해 
d = [5001] * (n+1) 
d[3] = 1
d[5] = 1

# 6 부터는 해당 위치보다 -3, -5의 위치 중 작은 값을 갖고와서
# 1을 더하면 해당 위치에서 가장 적은 양의 봉지를 구할 수 있다
# 배열이 5와 같거나 보다 작은 경우는 이미 결과가 저장되어 있기 
# 때문에 for문의 range는 6부터 시작한다. 

for i in range(6, n+1):
    d[i] = min(d[i-3], d[i-5]) +1

print(d[n] if d[n] < 5001 else -1)
