
'''
def solution(s):
    result = []
    if len(s) == 1:
        return 1
    
    # 쪼개기 s가 짝수(8)이면 최대 4개씩까지 쪼갤 수 있음
    for i in range(1, (len(s)//2)+1): 
        
        b = '' 
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s), i):
            if tmp == s[j: i+j]:
                cnt += 1
                print("여기", cnt, tmp)
            else:
                # 다음으로 넘어갔는데 cnt가 1이 아니야? 
                if cnt != 1:
                    b = b + str(cnt) + tmp
                    print("저기", cnt, b)
                # 다음으로 넘어갔지만 cnt가 1이야? 
                else:
                    b = b + tmp
                    print("거기", b)
                # tmp 업데이트 
                tmp = s[j:j+i]
                cnt = 1
        
        if cnt != 1:
            b = b + str(cnt) + tmp
            print("조기", b, cnt)
        else:
            b = b + tmp
            print("굴비", b)

        result.append(len(b))
    
    return min(result)

s= input()

a = solution(s)
print(a)
'''

# 문자열 압축
def solution(s):
    answer = len(s) # 최소 길이 

    #1개 단위 step부터 압축 단위를 늘려가며 확인 
    for step in range(1,len(s)// 2 + 1): #1 부터 문자열의 절반까지 자르며 비교해야하기때문에
        compressed = "" # 압축된 문자열 
        prev = s[0:step] # 앞에사부터 step 만큼의 문자열 추출
        count = 1 #반복되는 횟수 
        # 단위(step) 크기 만큼 증가시키며 이전 문자열과 비교
        
        print(step, '처음 for문')

        for j in range(step,len(s),step): 1 2 3 4 5 6 7 8
            #이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count += 1
                
                print(prev, j, j+step, count, '두번째 for문 - if문')
            #다른 문자열이 나왔다면(더이상 압축하지 못하는 경우)
            
            else:
                compressed += str(count) + prev if count >= 2 else prev
                '''
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    prev
                '''
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
                
                print(prev, j, j+step, 'else문')


        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        
        print(compressed, count, '남아있는 것들')

        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer,len(compressed))


    return answer


a = input()
print(solution(a))