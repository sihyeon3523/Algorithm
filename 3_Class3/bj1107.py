n = int(input()) # 찾고자 하는 값 
m = int(input())
remote_controller = {str(i) for i in range(10)}

if m > 0:
    # set 교집합으로 빼줌 --> 리스트의 값 중 여러 개를 한 번에 제거 해줘야 할 때 사용
    remote_controller -= set(map(str, input().split()))

min_cnt = abs(100-n)

# 왜 100만 까지 순회하느냐? 
# 50만까지만 순회한다면 작은 채널부터 큰 채널로 + 버튼을 눌렀을 때의 횟수만 구할 수 있다 
# 큰 채널에서 작은 채널로 -를 했을 때 최저 횟수인 경우에 대해선 알 수 없다 
# 채널 수는 무한대임 
for i in range(1000001):
    for j in range(len(str(i))):
        # 리모콘에 없는 값이 나오면 for문을 나오자
        if str(i)[j] not in remote_controller:
            break

        # 마지막 자릿수까지 모두 사용 가능한 버튼이라면 
        elif len(str(i)) - 1 == j:
            # 채널 번호 누른 횟수 len(str(i)) 와
            # 채널 번호에서 희망 채널까지 +-를 눌러야 하는 횟수를 더해서
            # 이전에 구한 최저횟수보다 적으면 최저횟수로 지정한다. 
            min_cnt = min(min_cnt, abs(i-n) + len(str(i)))

print(min_cnt)