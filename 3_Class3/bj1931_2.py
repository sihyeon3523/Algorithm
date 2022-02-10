# 빨리 끝나는 순서대로 정렬
# 종료 시간이 같다면 시작시간이 빠른 순으로 정렬
n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a,b])

#room.sort(key = lambda x: (x[1], x[0]))
room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end: # 시작시간 
        cnt += 1
        end = room[i][1] # 끝나는 시간 

print(cnt)