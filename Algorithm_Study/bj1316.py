# 25분 ~ 
# 각 단어가 그룹 단어 인지 아닌지를 구분하는 것 
'''
첫번째 풀이
문제에서 체크해야 할 부분은 변수로 따로 지정
'''
n = int(input())

cnt = 0

for i in range(n):
    a = input()
    length = len(a)
    # 그룹 단어가 아닐경우 +1
    error = 0
    for i in range(length-1):
        # 달라 떨어져서 나타난다 
        if a[i] != a[i+1]: 
            for j in range(i+1,length):
                if a[i] == a[j]:
                    error += 1
                    #print(a)
    if error == 0:
        cnt += 1
print(cnt)


'''
두번째 풀이 (다른 사람 풀이)
.count(self, x, __start, __end)
- self는 무시
- x는 찾을 문자열/문자
- __start, __end 문자열 검색 범위 (__start는 포함, __end는 미포함)
출처: https://blockdmask.tistory.com/410 [개발자 지망생]
'''
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0:
                error += 1
    if error == 0:
        group_word += 1
print(group_word)


