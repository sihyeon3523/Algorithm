def solution(numbers, hand):
    answer = []
    #keypad = [[1,2,3],[4,5,6],[7,8,9], ['*',0,'#']]
    keypad = {1: (0,0), 2: (0,1), 3: (0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), "*":(3,0), 0:(3,1), "#":(3,2)}
    left_num = '*'
    right_num = '#'

    for num in numbers:
        if num % 3 == 0 and num != 0 :
            answer.append('R')
            right_num = num

        elif num % 3 == 1:
            answer.append('L')
            left_num = num
        
        else:
            left_count = abs(keypad[left_num][0] - keypad[num][0]) + abs(keypad[left_num][1] - keypad[num][1])
            right_count = abs(keypad[right_num][0] - keypad[num][0]) + abs(keypad[right_num][1] - keypad[num][1])
            
            if left_count > right_count:
                answer.append('R')
                right_num = num
            elif left_count < right_count:
                answer.append('L')
                left_num = num
            else:
                if hand == 'right':
                    answer.append('R')
                    right_num = num
                else:
                    answer.append('L')
                    left_num = num       
            
    answer = "".join(answer)
                    
    return answer