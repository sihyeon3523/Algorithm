# 그룹 단어 체커
# S5
# 4시 8분 ~
# 그룹 단어: 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우
# 어떻게 하지? 

n = int(input())

group_word = 0
for i in range(n):
    a = input()
    check = 0
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            new_word = a[i+1:]
            if new_word.count(a[i]) > 0:
                check += 1
    if check == 0:
        group_word += 1

print(group_word)