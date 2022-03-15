def solution(new_id):
    
    # 1단계 모든 대문자를 소문자로
    new_id = new_id.lower()
    
    # 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    
    # 3단계
    while '..' in answer:
        answer = answer.replace("..", ".")

    # 4단계
    if answer[0] == "." and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == ".":
        answer = answer[:-1]
    
    # 5단계
    if answer == '':
        answer = "a"
    else:
        answer = answer
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
        
    # 7단계
    '''
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]    
    '''
    
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))    

    return answer

'''
정규표현식 익히기 
import re

def solution(new_id):
    st = new_id

    # 소문자 .lower()
    st = st.lower()

    # re.sub('[^a-z0-9\-_.]', '', st) 
    st = re.sub('[^a-z0-9\-_.]', '', st) 

    # re.sub('\.+', '.', st)
    st = re.sub('\.+', '.', st)

    # re.sub('^[.][.]$','', st)
    st = re.sub('^[.]|[.]$', '', st)

    st = 'a' if len(st) == 0 else st[:15]

    # re.sub('^[.][,]$','', st)
    st = re.sub('^[.]|[.]$', '', st)

    # st = st + "".join([st[-1] for i in range(3-len(st))]) "".join(리스트형 태도)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''