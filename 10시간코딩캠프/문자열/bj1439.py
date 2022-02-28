# 뒤집기
# S5
# 그리디
# 6시 4분 ~ 6시 36분 

# 틀렸습니다. 
S = input()

num_0 = 0
num_1 = 0

temp = True
tmp = S[0]

for i in S:
    if i == tmp:
        continue
    
    elif i != tmp:
        if tmp == '1':
            num_1 += 1
        elif tmp == '0':
            num_0 += 1
        tmp = i

if num_0 == 0 and num_1 == 0:
    print(0)
elif num_0 == 0 and num_1 != 0:
    print(num_1)
elif num_0 != 0 and num_1 == 0:
    print(num_0)
else:
    print(min(num_0, num_1))

'''
S = 0001100 은 010으로 봐도 무방하다. 길이에 관계없이 문자가 바뀌는지만 보기 때문이다

0과 1 --> 0번 길이 1
01 --> 1번 길이 2
010 --> 1번 길이 3
0101 --> 2번 길이 4
01010 --> 2번 길이 5
010101 --> 3번 길이 6
0101010 --> 3번 길이 7

규칙을 찾는 게 ... 중요했네
하나하나 따져보는게 
간소화 시키는 게 필요

문제가 요구하는 규칙성을 찾아내고 
이를 기준으로 숫자를 간소화 시키는게 필요하다 
'''

S = input()
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

print((count+1)//2)