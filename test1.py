# 시험문제: https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
# 결과: 시간초과 문제에 걸리지 않고 모든 테스트 통과! (대부분 0.15~0.24ms 나옴)
# 참고 기술블로그들 (re.sub, 정규식 사용법)
# https://ponyozzang.tistory.com/335
# https://cosmosproject.tistory.com/180

import re
new_id = 'z-+.^.'
#step 1
new_id = new_id.lower()
#step 2
new_id = re.sub(r'[^a-z-_.0-9]','',new_id)
#step 3
new_id = re.sub(r'[.]+', '.', new_id)
#step 4
if new_id.endswith('.'):
    new_id = new_id[:-1]
if new_id.startswith('.'):
    new_id = new_id[1:]

#step 5
if new_id =="": new_id = 'a'

#step 6, 7
if len(new_id) == 1:
    new_id = new_id*3
elif len(new_id) == 2:
    new_id = new_id + new_id[-1]
elif len(new_id) > 15:
    new_id=new_id[0:15]
    if new_id[-1] ==".": new_id=new_id[:-1]

print(new_id)


# 다른 사람의 풀이 NO.1
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) ==0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range (3-len(st))])
    return st

# 다른 사람의 풀이 NO.2

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer