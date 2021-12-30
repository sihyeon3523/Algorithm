# pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 실행합니다
# continue : 다음 순번의 loop를 수행합니다. 
# break : 반복문을 멈추고 loop 밖으로 나가도록 합니다. 

# pass 예시
# pass 가 사용되는 경우 
# - 조건문에서 넣어줄 조건이 딱히 없는 경우
# - class를 선언할 때, 초기에 넣어줄 값이 없을 때 정도로 생각
# - 코드를 작성한 후 동작 확인을 위해 실행할 때, 해당 부분에서 오류가 발생하지 않도록 하기 위해 많이 사용
for i in range(10):
    if i % 2 == 0:
        pass
        print("pass", i)
    else:
        print(i)

print("Done")

# continue 예시
# continue가 실행되면 해당 순번의 loop를 넘어가
# 다음번 loop로 들어가게 된다. 
for i in range(10):
    if i % 2 == 0:
        continue
        print(i)
    print(i)
print("Done")

# break 예시
for i in range(10):
    if i % 2 ==0:
        break
        print(i)
    else:
        print(i)

print('Done')