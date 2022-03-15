def solution(board, moves):
    answer = 0
    
    # 임시 바스켓 
    basket = []

    # list[행][열]
    
    # 각각 움직임에 대해서
    for move in moves:
        # 0이 아닌 값을 찾는다 
        for i in range(len(board)):
            # 0 일 경우 다음 값을 찾고
            if board[i][move-1] == 0:
                continue
            # 0이 아닐 경우 
            else:
                # basket에 값을 옮긴다  
                basket.append(board[i][move-1])
                # board의 값을 0으로 초기화한다
                board[i][move-1] = 0
                
                ## basket에 값이 하나만 들어갈 경우 비교 대상이 없으므로 for문을 나간다 
                if length == 1: 
                    break
                ## basket에 값이 두개 이상 들어있을 경우
                else:
                    ## 방금 넣은 값과 바로 이전에 넣은 값이 같다면
                    if basket[-2] == basket[-1]:
                        ## answer에 2를 더해주고 
                        answer += 2
                        
                        ## 맨 위의 두 개의 값을 빼준다
                        basket.pop(-1)
                        basket.pop(-1)
                # else문이 끝난 후 다음 move로 가기 위해 두번째 for문을 나간다 
                    break
    return answer

'''
다른 사람 코드 
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
'''