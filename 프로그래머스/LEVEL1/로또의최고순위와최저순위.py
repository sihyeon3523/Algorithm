# 시험문제: https://programmers.co.kr/learn/courses/30/lessons/77484
# 결과: 시간초과 문제에 걸리지 않고 모든 테스트 통과! 통과 (0.00ms, 10MB)
'''
로또의 순위를 정하는 방식을 딕셔너리 형태로 매칭해줬으나,
연속된 숫자 값에 대한 매칭이기 때문에 딕셔너리의 key 가 아닌
리스트의 index를 이용해도 된다는 점을 알게 되었다. 
'''

def solution(lottos, win_nums):
    answer = []
    # score = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    score = [6, 6, 5, 4, 3, 2, 1]
    
    same = 0
    cnt = lottos.count(0)
    
    for x in lottos:
        if x in win_nums:
            same += 1

    answer = [score[same+cnt], score[same]]
    return answer