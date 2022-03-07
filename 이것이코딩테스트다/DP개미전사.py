# 정수 N 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*100

# 다이나믹 프로그래밍 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2,n):
    d[i] = max(array[i-1], array[i] + d[i-2])

# 지금 위치의 값을 선택하지 않아도 최선의 값이 그 위치에 저장된다 그렇기 때문에.. 가장 마지막 값을 출력하는 것
print(d[n-1])