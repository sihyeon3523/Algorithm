'''
실패율
= 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수/ 스테이지에 도달한 플레이어 수
N 전체 스테이지의 개수
stages 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
'''
# 다른 사람 풀이 
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse = True)


# 내 풀이 

def solution(N, stages):
    # 스테이지 번호별로 실패율 담을 dict 필요
    result = {}
    stages.sort()

    tmp = len(stages)
    for i in range(N):
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 (분자)
        a  = stages.count(i+1)
         
        if a != 0:
            # 스테이지에 도달한 플레이어 수 (분모)
            b = tmp - stages.index(i+1) 
            # 스테이지의 실패율
            result[i] = a/b
        else:
            result[i] = 0
    result = [key+1 for (key, value) in sorted(result.items(), key= lambda item: (item[1], -item[0]), reverse=True)]

    return result