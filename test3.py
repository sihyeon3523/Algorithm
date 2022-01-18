#코테 링크:https://programmers.co.kr/learn/courses/30/lessons/42747#
#질문 목록: https://programmers.co.kr/learn/courses/30/lessons/42747/questions
#결과: 실패 (1~10, 12~15)


list1 = [3,0,6,1,5]
def count_fn(citations, k):
    bins = 0
    for i in range(len(citations)):
        if citations[i] >= k:
            bins += 1
    return bins

def solution(citations):
    answer = []
    bins = []

    for i in citations:
        a = count_fn(citations, i)
        bins.append(a)

    # 리스트 필터링
    for j in range(len(citations)):
        if citations[j] <= bins[j]:
            answer.append(citations[j])

    # 그 중 최대값 추출
    answer = max(answer)

    return answer

print(solution(list1))