n = int(input())
student_lis = []


for i in range(n):
    a, b = map(int, input().split())
    student_lis.append((a,b))

for i in student_lis:
    rank = 1
    for j in student_lis:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
            print(i[0], j[0], rank)
    print(rank, end = " ")

