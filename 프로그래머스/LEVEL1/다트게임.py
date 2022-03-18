def solution(dartResult):
    answer = 0
    
    b = ''
    result = ['S','D','T']
    score = ['0','1','2','3','4','5','6','7','8','9','10']
    option = ['*','#']
    tmp = []
    
    for i in range(len(dartResult)):
        if dartResult[i] in result:
            tmp.append(int(b))
            b = ''
            if dartResult[i] == 'S':
                continue
            elif dartResult[i] == 'D':
                tmp[-1] = tmp[-1]**2
            elif dartResult[i] == 'T':
                tmp[-1] = tmp[-1]**3         
                
        elif dartResult[i] in score:
            b += dartResult[i]
        
        elif dartResult[i] in option:
            if dartResult[i] == '*':
                a = len(tmp)
                if a == 1:
                    tmp[0] = tmp[0]*2
                else:
                    tmp[-1] = tmp[-1]*2
                    tmp[-2] = tmp[-2]*2
            elif dartResult[i] == '#':
                tmp[-1] = tmp[-1]*(-1)  
    
    answer = sum(tmp)
    return answer