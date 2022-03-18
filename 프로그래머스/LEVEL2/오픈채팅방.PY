# 내 풀이 
def solution(record):
    answer = []
    user_info = {}
    
    # 이전에 있는 값들도 바뀌어야 함 
    
    # 아이디 바꾸기 
    for i in record:
        a = list(i.split())
        if a[0] == 'Enter':
            user_info[a[1]] = a[2]
        elif a[0] == 'Change':
            user_info[a[1]] = a[2]
        elif a[0] == 'Leave':
            continue
    
    for i in record:
        a = list(i.split())
        if a[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(user_info[a[1]]))
        elif a[0] == 'Change':
            continue
        elif a[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(user_info[a[1]]))
    return answer

# 다른 사람 풀이 
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer