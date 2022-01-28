
'''
target = int(input())
ans = abs(100-target) #++ or -- 로 이동할 경우 --> 최댓값 
M = int(input())

if M:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
        else:
            ans = min(ans, len(str(num))) + abs(num - target)
'''

N = int(input())
M = int(input())
remote_controller = {str(i) for i in range(10)}

if M > 0:
    remote_controller -= set(map(str, input().split()))

min_cnt = abs(100 - N)

for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] not in remote_controller:
            break

        # 마지막 자릿수까지 모두 사용가능한 버튼이라면 
        elif len(str(channel)) - 1 == j:
            # len(str(channel)) : 채널 번호를 누른 횟수 
            # abs(channel - N) : 채널 번호와 희망 채널까지 +-를 눌러야 하는 횟수
            min_cnt = min(min_cnt, abs(channel-N) + len(str(channel)))

print(min_cnt)