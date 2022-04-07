
# 내풀이
# 통과 (1.28ms, 10.4MB) 
def solution(phone_book):
    answer = True
    ## 문자열 순서대로 sort
    phone_book = sorted(phone_book)
    
    cnt = 0
    # 두번째 문자열로 시작해 비교 
    for i in range(1, len(phone_book)):
        # cnt는 첫번째 문자열부터 시작해서 다음값과 비교 
        # 둘의 값이 같으면 
        if phone_book[cnt] == phone_book[i][:len(phone_book[cnt])]:
            # False 하고 break 하면서 for문 나감 
            answer = False
            break 
        # 비교 값을 이동시켜줌 
        cnt += 1
    return answer



# 다른 사람 풀이 1

'''
https://www.daleseo.com/python-zip/
zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
zip() 함수를 사용하면 마치 옷의 지퍼를 올리는 것 처럼 양 측에 있는 데이터를 하나씩 차례로 짝을 지어줍니다.
'''

# (1.39ms, 10.4MB)
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    # zip 함수로 list 에 있는 값을 하나씩 꺼내줌 
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        # 문자열 시작되는 값 조회 = .startswith()
        if p2.startswith(p1):
            return False
    return True


# 다른 사람 풀이 2
# 통과 (1.37ms, 10.4MB)
def solution(phone_book):
    answer = True
    # 문자열 순서대로 sort --> 이게 핵심 
    phone_book = sorted(phone_book)
    
    # 한 바퀴 돌면서 시행 
    for i in range(len(phone_book)-1):
        # 같은 전화번호는 중복되지 않기 때문에 "="은 사용 안함 
        if len(phone_book[i]) < len(phone_book[i+1]):
            # 앞 문자와 같은지 조회 
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break              
    return answer

# 첫번째 풀이
# --> 시간초과 뜸 

def solution(phone_book):
    answer = True
    ## 길이 순서대로 sort
    phone_book = sorted(phone_book, key=lambda x : len(x))
    
    # 1,000,000 * 1,000,000 = 1조 
    # phone_book이 없어질 때까지 돌면서 
    while phone_book:
        # 첫번째 값을 pop
        tmp = phone_book.pop(0)
        
        # 문자열의 첫번째 값이 같은지 확인 
        for i in range(len(phone_book)):
            if tmp == phone_book[i][:len(tmp)]:
                # 같다면 바로 return 
                answer = False
                return answer               
    # 아니라면 true return 
    return answer

