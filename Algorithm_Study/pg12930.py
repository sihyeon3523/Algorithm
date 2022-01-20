def solution(s):
    a = s.split(" ") # 각 단어는 하나 이상의 공백 문자로 구분되어 있습니다 
    answer = []
    for i in a:
        w = ''
        for j in range(len(i)):
            if j % 2 == 0:
                w += i[j].upper()
            else:
                w += i[j].lower()
        answer.append(w)
        
    return ' '.join(answer)