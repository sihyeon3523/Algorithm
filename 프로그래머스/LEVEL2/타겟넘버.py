from collections import deque

# bfs 풀이 --> queue 이용 
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    # +인 경우의 값과 idx append 
    queue.append([numbers[0], 0])
    # -인 경우의 값과 idx append 
    queue.append([-1*numbers[0], 0])

    # q에 넣어줄 때에는 하나의 값만 넣을 수 있다 두 개의 값을 동시에 넣으려면 [], () 로 묶어줘야 한다

    # queue가 없어질 떄까지 while 문 돌리기 
    while queue:
        # queue 에서 첫번째 꺼 꺼냄 
        temp, idx = queue.popleft()

        # idx 올려줌 ( numbers의 다음 값을 넣어주기 위함 )
        idx += 1
        
        # 만약 idx 가 전체 numbers를 돌지 않았다면 
        if idx < n:
            # 계속 계산을 해준다 --> 양수, 음수 일 때의 값을 queue에 넣어준다 idx 랑 같이
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        
        # 만약 idx 가 전체 len(numbers) 랑 같다면 
        else:
            # target 값과 temp 값 (numbers 를 돌면서 더하거나 뺀 값)과 같다면
            if temp == target:
                # answer 에 1을 더해준다 
                answer += 1

    return answer