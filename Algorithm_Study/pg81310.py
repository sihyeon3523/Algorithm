def solution(s):
    answer = s
    a = {'zero':'0', 'one':'1','two':'2', 'three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

    for item in a.items(): # (key, value)가 같이 튜플 형태로 뽑힘
        answer = answer.replace(item[0], item[1])
    
    return int(answer)

print(solution('one4seveneight'))