n, m = map(int, input().split()) # 나무의 수, 길이

namu = list(map(int, input().split())) # 나무의 높이들 

left = 0 
right = max(namu)

while left <= right:
    
    mid = (left + right)//2
    
    sum = 0
    for i in namu:
        if i >= mid:
            sum += (i - mid)

    if sum >= m: # 원하는 나무 높이보다 더 많이 잘렸으면 
        left = mid + 1

    elif sum < m: # 원하는 나무 높이보다 덜 잘렸으면 
        right = mid -1 

print(right)