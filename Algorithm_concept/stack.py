# 파이썬에서는 스택 자료구조는 따로 제공하지 않는다
# 다만 기본 클래스인 list를 통해 스택을 흉내낸다

# 스택이란
# 가장 나중에 들어온 자료가 가장 먼저 처리되는 LIFO 자료구조
# 구멍이 하나밖에 없는 병

# 스택 구현

# stack init
stack = []

# stack push 
# append : 리스트의 가장 마지막에 원소를 넣는다
stack.append(4)

# stack pop
# pop 메소드를 이용해 리스트의 가장 마지막 원소를 제거해준다
# pop 메서드에 의해 제거한 원소를 리턴 받을 수 있다 
top = stack.pop()

print(top)
stack

# stack top
# 스택에서 원소를 제거하지 않고 가져오기만 할 때에는 [-1]을 이용하도록 한다
top = stack[-1]