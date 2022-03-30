def solution(progresses, speeds):
    answer = []
    # 93% 완료 하루에 1% 씩 작업
    days = []
    for i in range(len(progresses)):
        day = (100 - progresses[i])//speeds[i]
        plus = (100 - progresses[i])%speeds[i]
        if plus != 0:
            day += 1
        days.append(day)
    
    for i in range(len(days)-1):
        if days[i] > days[i+1]:
            days[i+1] = days[i]
    
    print(days)
    cnt = 1
    for i in range(len(days)-1):
        if days[i] == days[i+1]:
            cnt += 1
            #print(cnt, days[i], days[i+1])
            if i == len(days) -2:
                answer.append(cnt)
        else:
            #print(cnt, days[i], days[i+1])
            answer.append(cnt)
            cnt = 1
            if i == len(days) -2:
                answer.append(cnt)
            #print(cnt, days[i], days[i+1])

    #print(answer)
    return answer


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer