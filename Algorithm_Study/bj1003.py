# 피보나치 함수 -> 다이나믹 프로그래밍 
# 0이 출력되는 횟수, 1이 출력되는 횟수 공백으로 구분 

# 첫번째 풀이 
zero = [1,0,1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    
    print("{} {}".format(zero[num], one[num]))

T = int(input())

for _ in range(T):
    fibonacci(int(input()))

# 두번째 풀이

t = int(input())

for _ in range(t):
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    n = int(input())
    if n > 1:
        for i in range(n-1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-1]+cnt_1[-1])
    
    print(cnt_0[n], cnt_1[n])