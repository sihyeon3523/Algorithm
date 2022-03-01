# 순열 구현하기 (1) - itertools 모듈 사용하기
# 순열 : 서로 다른 n개의 원소에서 r개를 중복없이 순서에 상관있게 선택하는 혹은 나열하는 것을 순열(permutation)
'''
import itertools
# 코딩테스트에서 가장 효율적인 방법이다 (간단하고 빠르다)

# 한 개의 리스트에서 모든 순열을 구하기
l = ['a','b','c']

print(list(map(list, itertools.permutations(l))))
# 결과값: [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]

# 순열 구현하기 (2) - DFS 사용하기
# itertools를 사용하지 못할 때 구현할 수 있다

# DFS로 모든 경우의 수를 하나씩 구하되, 각 경우의 수에 같은 요소가 없도록 함으로써 순열을 구현한다
l = ['a', 'b', 'c']
visited = [0 for _ in range(len(l))]
answer = []

def dfs(cnt, list):
    if cnt == len(l):
        answer.append(list[:])
        return
    
    for i, val in enumerate(l): # index, value
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            continue
        
        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1

        dfs(cnt+1, list)

        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        visited[i] = 0

dfs(0, [])
print(answer)
        
# 조합 구현하기 (1) - itertools 사용하기
# 빠르고 효율적이다

# 목적: 한 개의 리스트에서 r개의 조합 구하기
import itertools

l = ['a','b','c','d']
print(list(map(list, itertools.combinations(l, 2))))
'''
# 조합 구현하기 (2) - DFS 사용하기
# itertools 를 사용 못할 때, 효율화 시키기

# 목적: 한 개의 리스트에서 r개의 조합 구하기
# DFS를 사용하여 r개를 초과하는 가지는 구하지 않도록 하였다

l = ['a','b','c','d']
n = len(l)
r = 2
answer = []

def dfs(idx, list):
    if len(list) == r:
        answer.append(list[:])
        return
    
    for i in range(idx, n):
        dfs(i+1, list+[l[i]])
        print(list)

dfs(0, [])
print(answer)