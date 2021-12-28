# 블랙잭
# B2

N, M  = map(int, input().split())
cards = list(map(int, input().split()))
max_close = []

cards.sort()
#print(cards)
#result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = 0
            tmp = cards[i] + cards[j] + cards[k]
            #print(tmp,cards[i], cards[j], cards[k])
            if tmp <= M:
                max_close.append(tmp)
                #result = max(result, cards[i] + cards[j] + cards[k])

                #print('작거나 같다', tmp)
            else:
                continue
print(max(max_close))
#print(result)

'''
# 순열 조합을 이용한 풀이 
from itertools import combinations # 순열 조합 라이브러리

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
biggest_sum = 0

for cards in combinations(card_list, 3): # 3개 원소로 수열 만들기
    temp_sum = sum(cards)
    if biggest_sum < temp_sum <= target_sum:
        biggest_sum = temp_sum
print(biggest_sum)
'''