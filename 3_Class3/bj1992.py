# 흰점 0 검은점 1
# 쿼드트리: 분할 정복, 재귀
# 3시 ~ 

'''
분할 정복 알고리즘의 설계 전략
분할 --> 해결할 문제를 여러 개의 작은 부분 문제들로 분할
정복 --> 나눈 작은 문제를 각각 해결
통합 --> 필요 시 해결된 해답을 모음

분할정복 예시 C^n
def Recursive_Power(C, n):
    if n == 1:
        return C
    
    if n % 2 == 0:
        y = Recursive_Power(C, n/2)
        return y*y
    else:
        y = Recursive_Power(C, (n-1)/2)
        return y*y*C
'''

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dnc(x, y, n):
    check = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 리스트[세로인덱스][가로인덱스] 
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        dnc(x, y, n) # 왼쪽 위
        dnc(x, y+n, n) # 오른쪽 위
        dnc(x+n, y, n) # 왼쪽 아래 
        dnc(x+n, y+n, n) # 오른쪽 아래 
        print(")", end = '')
    
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')

dnc(0,0,n)