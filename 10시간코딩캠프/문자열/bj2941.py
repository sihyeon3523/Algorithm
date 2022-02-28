# 크로아티아 알파벳
# S5
# 문자열
# 3시 50분 ~ 4시 6분

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cro_str = input()

# cro에 해당하는 문자를 만나면 -1로 치환 
for i in cro:
    cro_str = cro_str.replace(i, '0')

print(len(cro_str))