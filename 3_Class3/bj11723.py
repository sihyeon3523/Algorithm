# 집합
# S5

'''
중복을 허용하지 않는다 --> 중복 제거에 쓰임
순서가 없다 --> 인덱싱 접근 불가능
교집합 : s1 & s2, s1.intersection(s2)
합집합 : s1 | s2, s1.union(s2)
차집합 : s1 - s2, s1.difference(s2)
값 추가 : .add()
값 여러 개 추가 : .update([])
특정 값 제거하기 : .remove() --> 없는 원소를 제거하려고 하면 에러남
특정 값 제거하기 에러없이 : .discard() --> 없는 원소 제거에도 에러 안남
임의의 원소를 하나 가져온 후 삭제 : .pop()
모든 원소를 비우고 공집합으로 만들기 : .clear()
'''

'''
import sys

n = int(input())
for i in range(n):
    a = sys.stdin.readline()
    print(a) # sys.stdin.readline() : 기본적으로 개행 문자를 포함하고 있다, 문자열 마지막에 개행문자가 포함되어 출력
    print(a.rstrip()) # 오른쪽 공백을 제거 
    
    # .lstrip() 왼쪽 공백을 제거
    # .strip() 왼쪽, 오른쪽 공백을 삭제
'''

import sys
s = set()

n = int(input())

for i in range(n):
    a = list(sys.stdin.readline().split())

    if a[0] == 'add':
        if a[1] in s:
            pass
        else:
            s.add(a[1])

    elif a[0] == 'remove':
        s.discard(a[1])
    
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    
    elif a[0] == 'toggle':
        if a[1] in s:
            s.remove(a[1])
        else:
            s.add(a[1])
    
    elif a[0] == 'all':
        s.clear()
        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}

    elif a[0] == 'empty':
        # 공집합 
        s.clear()

