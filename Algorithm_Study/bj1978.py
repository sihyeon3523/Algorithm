'''
풀이 1 : 함수를 이용하지 않고 푸는 방법 

※주의할 점※
- 소수는 자신과 1만을 약수로 갖는 수를 의미, 1은 1만 약수로 갖기 때문에 소수가 아님.
- range(2,2)는 아무 값이 출력되지 않음(2는 소수)
'''

# 정수형으로 값 받기 
n = int(input())
# input().split()으로 값을 나누고 정수값으로 변환 후, list 형태로 반환 
num = list(map(int, input().split()))

# 총 소수의 갯수
cnt = 0


for i in num:
    tmp = 0
    for j in range(2, i):
        
        # i와 [2, i-1] 범위의 숫자를 나누었을 때, 나누어 떨어지면 그때의 j값은 i의 약수
        if i % j == 0:
            # 약수가 있을 경우, tmp에 1 더해줌 
            tmp += 1 

    # tmp가 0일 때(=[2, i-1]범위에 나누어 떨어지는 값이 없을 때), 해당 i는 소수
    if tmp == 0:
        # 소수이면 총 소수의 갯수에 1 더해줌 
        cnt += 1

# num의 모든 값을 확인 후, 총 소수의 갯수 출력    
print(cnt)

'''
풀이 2 : 함수를 이용해 푸는 방법 (소수인지 확인하는 부분 함수화)
- 계산량이 준다는 이점을 가짐.
- 소수가 아닐 경우(나누어 떨어질 경우) 다음 수를 고려하지 않고 바로 반환하므로 계산량을 줄여줌 
'''

# 정수형으로 값 받기 
n = int(input())
# input().split()으로 값을 나누고 정수값으로 변환 후, list 형태로 반환 
sosu = list(map(int, input().split()))

# 소수인지 확인하는 함수 정의
def prime(num):
    # 1이면 False 반환 (소수 아님)
    if num == 1:
        return False
    
    # num을 [2, num-1] 사이의 값으로 나누었을 때, 하나라도 나누어 떨어지면 소수임. False 반환
    for i in range(2, num): 
        if num % i == 0:
            return False
    
    # 위 조건에 걸리지 않았다면 소수임. True 반환 
    return True

# 총 소수의 갯수
cnt = 0

for i in sosu:
    # 소수 확인 함수 호출해서 True이면(소수이면) cnt에 1 더함
    if prime(i):
        cnt += 1

# 총 소수의 갯수 출력 
print(cnt)
