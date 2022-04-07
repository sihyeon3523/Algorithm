# 시험문제: https://programmers.co.kr/learn/courses/30/lessons/81301
# 결과: 시간초과 문제에 걸리지 않고 모든 테스트 통과! (대부분 0.02ms 나옴)
'''
알게된 점 
딕셔너리를 이용 
for 문에서 딕셔너리의 값을 뽑으면 key 값이 뽑힌다 
'''


def solution(s):
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
                'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = ''
    
    # key 가 뽑히네 
    for num in num_dict:
        if num in s:
            s = s.replace(num, num_dict[num])
        else:
            continue
    return int(s)