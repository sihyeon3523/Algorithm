import copy
from itertools import permutations # 순열   

# 연산자 위치 찾기 
def cal_index(cal, plus):
    plus_tmp = []
    for i, j in enumerate(plus[:]):
        if j == cal:
            plus_tmp.append(i)
    return plus_tmp

# 계산하고 리스트 없애기
def cal(cal, plus_tmp, nums_tmp):
    if cal == '*':
        for i in plus_tmp:
            nums_tmp[i+1] = nums_tmp[i] * nums_tmp[i+1]
            #del nums_tmp[i]
            
        cnt = 0
        for i in plus_tmp[:]:
            cnt += 1
            if cnt == 1:
                del nums_tmp[i]
            else:
                del nums_tmp[i-1]
            
    elif cal == '-':
        for i in plus_tmp:
            nums_tmp[i+1] = nums_tmp[i] - nums_tmp[i+1]
            print(nums_tmp[i], nums_tmp[i+1])
        
        cnt = 0
        for i in plus_tmp[:]:
            cnt += 1
            if cnt == 1:
                del nums_tmp[i]
            else:
                del nums_tmp[i-1]

    else:
        for i in plus_tmp:
            nums_tmp[i+1] = nums_tmp[i] + nums_tmp[i+1]
            #del nums_tmp[i] 왜 이렇게 하면 list out of range error 가 뜨지? 
        
        cnt = 0
        for i in plus_tmp[:]:
            cnt += 1
            if cnt == 1:
                del nums_tmp[i]
            else:
                del nums_tmp[i-1]
    return nums_tmp

# 계산하고 계산한 연산자 삭제
def cal_del(plus_, plus_tmp):
    cnt = 0
    for i in plus_tmp:
        cnt += 1
        if cnt == 1:
            del plus_[i]
        else:
            del plus_[i-1]
    return plus_tmp
    
# 전체 남은 계산하기 
def final_cal(cal, nums):
    tmp = nums[0]
    if cal == '*':
        for i in nums[1:]:
            tmp *= i
    elif cal == '+':
        for i in nums[1:]:
            tmp += i
    else:
        for i in nums[1:]:
            tmp -= i
    return tmp     

def solution(expression):
    answer = 0
    nums = []
    plus = []
    cnt = 0

    # 숫자와 문자 분리하기 
    for i in range(len(expression)):
        if expression[i] in ['-', '*','+']:
            nums.append(int(expression[cnt:i]))
            cnt = i+1
            plus.append(expression[i])
    nums.append(int(expression[cnt:]))
    
    a = list(set(plus))
    
    # a의 길이가 1일 때 
    if len(a) == 1:
        answer = nums[0]
        if plus[0] == '+':
            answer = sum(nums)
        elif plus[0] == '-':
            for i in nums[1:]:
                answer -= i         
        else:
            for i in nums:
                answer *= i
    
    elif len(a) == 2:
        tmp_sum = 0
        nums_tmp = copy.deepcopy(nums) # 얕은 복사하면 같은 곳을 참고해서 index out of range 에러 뜬다 
        # 연산자 우선순위: * - 
        plus_tmp = cal_index(a[0], plus)
        nums_tmp = cal(a[0], plus_tmp, nums_tmp)
        tmp_sum = final_cal(a[1], nums_tmp)

        # 연산자 우선순위: - *
        nums_tmp = copy.deepcopy(nums)
        plus_tmp = cal_index(a[1], plus)
        nums_tmp = cal(a[1], plus_tmp, nums_tmp)
        result = max(abs(tmp_sum), abs(final_cal(a[0], nums_tmp)))
        return result

    # a의 길이가 3일 때 
    else:
        answer = 0
        per = list(permutations(a, 3))
        for i in per:
            print(i[0], i[1], i[2])
            tmp_sum = 0
            nums_tmp = copy.deepcopy(nums)
            plus_ = copy.deepcopy(plus)
            
            plus_tmp = cal_index(i[0], plus_)
            nums_tmp = cal(i[0], plus_tmp, nums_tmp)
            plus_tmp = cal_del(plus_ , plus_tmp)
            
            plus_tmp = cal_index(i[1], plus_)
            nums_tmp = cal(i[1], plus_tmp, nums_tmp)
            answer = max(abs(final_cal(i[2], nums_tmp)), answer)

    return answer