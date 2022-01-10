# S3

# fibonacci(n-1)의 0과 1 호출 횟수 + fibonacci(n-2)의 0과 1 호출 횟수와 동일
# 미리 정의해놓으면 된다 
zero = [1,0,1]
one = [0,1,1]

def fibonacci(num):
    length = len(zero)
    
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print('{} {}'.format(zero[num], one[num]))

T = int(input())

for _ in range(T):
    fibonacci(int(input()))