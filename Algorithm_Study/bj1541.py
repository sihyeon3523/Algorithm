'''
n = input()

num = []
pm = []
idx = 0

for i in range(len(n)):
    if n[i] == '-' or n[i] == '+':
        num.append(int(n[idx:i]))
        pm.append(n[i])
        idx = i + 1

num.append(int(n[idx:]))


if '-' in pm and '+' in pm:
    for i in 
    print('둘 다 있음')

elif '-' in pm and '+' not in pm:
    result = num[0]
    for i in range(1,len(num)):
        result -= num[i]
    print(result)

elif '+' in pm and '-' not in pm:
    print(sum(num))
'''

'''
1541번 잃어버린 괄호 S2
주 아이디어 : 최솟값을 구하기 위해서는 '-'를 기준으로 괄호를 치면 된다. 
'''


# 입력 값을 - 를 기준으로 split한다 
a = input().split('-') 
num = []

# 나뉘어진 값 내부의 값을 더해준다 
for i in a:
    cnt = 0
    
    # +를 기준으로 split을 하고 (a1+a2,b1+b2,c1+c2+c3)
    s = i.split('+')
    # 나누어진 값 각각을 더해준다 (a = a1+a2,b=b1+b2,c=c1+c2+c3)
    for j in s:
        cnt += int(j)

    # 더해진 값을 num 리스트에 넣는다 
    num.append(cnt)

# (-기준으로 나누고 나누어진 값 각각을 더한 값들의 모임 = num)의 첫번째 값을 n으로 설정하고
n = num[0]

# - 기준으로 나눈 더한 값을 빼준다 (a-b-c 연산을 의미)
for i in range(1, len(num)):
    n -= num[i]
# 최종 값 출력 
print(n)
