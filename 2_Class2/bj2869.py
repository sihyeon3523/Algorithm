'''
a, b, v = map(int, input().split())

d = 0

while v >= 0:

    print('첫번째', v)
    if (v == a) or (-v == b):
        print('두번째', v-a)
        d += 1
        print('세번째',d)
        break

    v -= a
    d += 1
    #print('첫번째',v, d)
    if v <= 0:
        #print('두번째 성공', v,d)
        print(d)
        break
    else:
        v += b
        #print('세번째', v, b, d)
    # 0이 될 때까지 높이 -2, day +1
'''

a,b,v = map(int, input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k) + 1)