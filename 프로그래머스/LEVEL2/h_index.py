def solution(citations):
    answer = 0
    
    # n편 중 h번 이상 인용된 논문이 h편 이상이고 

    # index 기준으로 검색 
    citations.sort(reverse=True) # 기본이 오름차순 
    print(citations)
    # index 사용 --> enumerate 사용 
    for i, v in enumerate(citations):
        if i >= v:
            return i
            
    return len(citations) # 최대값을 출력 
