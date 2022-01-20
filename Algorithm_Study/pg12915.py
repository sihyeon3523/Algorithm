
def solution(strings, n):
    strings.sort(key=lambda x : (x[n],x))
    print(strings)

strings = []
for i in range(4):
    strings.append(input())
n = int(input())

solution(strings, n)