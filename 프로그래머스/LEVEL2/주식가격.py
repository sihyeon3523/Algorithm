from collections import deque
'''
Queue로 쓰이는 경우에만 deque가 list보다 빠릅니다. 일단 deque는 list처럼 [i]와 같이 index에 따른 접근이 불가하기 때문에, 중간에 있는 값에 접근하려면 list를 사용하는 것이 훨씬 효율적이죠. Stack으로 쓰이는 경우에는 별 차이 없습니다.

stack vs queue
stack LIFO
Queue FIFO
Deque 둘 다 가능 --> push, pop 이 빈번하면 list 보다 압도적 성능 
'''

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        price = q.popleft()
        sec = 0
        
        # q가 비어 있어도 for문을 돈다? 
        for x in q:
            sec += 1
            if price > x:
                break 
        answer.append(sec)
    
    return answer