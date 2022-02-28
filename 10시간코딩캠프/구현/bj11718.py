# 그대로 출력하기
# B3
# 7시 6분 ~ 13분 

while 100:
    try:
        print(input()) # 읽은 즉시 출력
    except EOFError: # 더이상 읽을 수 있는 데이터가 없을 때
        break # while문 끝냄