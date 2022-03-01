'''
1) 목적 : 문자열 변수 이름 붙이기
 - 예) snake_case = "snake case"

2) 목적 : 문자열 일부 추출하기
- 예) snake_case = "snake case"
- 예) print(snake_case[0:5])   => "snake"
- 예) print(snake_case[::2])    => "saecs"
- [시작하는인덱스(포함) : 끝나는인덱스(포함X): 문자이동하기]
- 예) print(list(snake_case))    => ['s', 'n', 'a', 'k', 'e', ' ', 'c', 'a', 's', 'e']
- 예) snake_case_list = ["snake","case"]

3) 리스트 -> 문자열로 변경 하고 싶을 때, "붙일 떄 사이사이에 넣을 문자".join(리스트) 를 사용한다.
- 예) print(" ".join(snake_case_list))   => "snake case"
- 예) print("".join(snake_case_list))   => "snakecase"

4) 목적: 문자열이 영어인지, 숫자인지 확인하기
- 영어인지 확인할 땐 문자열.isalpha(),  숫자인지 확인할 땐 문자열.isdigit()

- 예) ab12 = "ab12"
- 예) print(ab12[0].isalpha())   => True
- 예) print(ab12[0].isdigit())   => False
- 예) print(ab12[2].isdigit())   => True
- 예) print(ab12[2].isalpha())   => False

5) 목적: 문자열이 소문자인지, 대문자인지 확인하기
- 소문자인지 확인할 떈 문자열.islower(), 대문자인지 확인할 땐 문자열.isupper()
- 예) ab12 = "Ab12"
- 예) print(ab12[0].islower())     => False
- 예) print(ab12[0].isupper())     => True

- 소문자로 변경 할 때는 문자열.lower(), 대문자로 변경할 때는 문자열.upper()
- 예) ab12 = "Ab12"
- 예) ab12[0].lower()     => ab12 = "ab12"
- 예) ab12[1].upper()     => ab12 = "aB12"

6) 목적: 문자열 내에서 특정 문자 찾기
- find() 를 쓴다. 찾으면 (시작하는)해당 위치를, 찾지 못하면 -1을 반환한다.
- 예) ab12 = "Ab12"
- 예) print(ab12.find("A"))    =>  0
- 예) print(ab12.find("Ab1"))  => 0
- 예) print(ab12.find("철수"))    =>  -1

7) 목적: 문자열 내에서 특정한 문자 제거하기
- 문자열.replace(바뀔문자, 바꿀문자)를 쓴다.
- 예) ab12 = "Ab12"
- 예) print(ab12.replace("Ab","철수"))  => "철수12"

- re.sub 정규식을 사용한다. re.sub(바꿀문자규칙, 이렇게바꾼다, 문자열)   import re 를 해줘야한다!
- 예) ab12 = "A-b-1-2!!!_허허"
- 예) ab12 = re.sub('[^a-zA-Z0-9]','',ab12)
- 예) 위의 [ ] 안에서 규칙이 생긴다. ^는 '이것들 빼고', a-z 는 a에서 z까지, A-Z는 A에서Z까지, 0-9는 0에서 9까지 라는 뜻. 총합하면 a에서z까지랑 A에서Z까지랑 0에서9까지랑 제외하고는 죄다 바꿀꺼다! 라는 뜻.
- 예) print(ab12)   => "Ab12"
'''