# 첫번째 풀이 - 동일 문자 갯수 기준으로 if문 처리 
base2 = ['c=','c-','d-','lj','nj','s=','z=']
word = input() 
cnt = 0
i = 0

# 크로아티아 문자의 갯수 기준으로 if문 처리
while (i < len(word)):
    
    # 동일한 문자가 세 개  
    if word[i:i+3] == 'dz=':
        cnt += 1
        
        #print(word[i:i+3],i, cnt)
        i += 3
        continue

    # 동일한 문자가 두 개  
    elif word[i:i+2] in base2:
        cnt += 1
        #print(word[i:i+2], i, cnt)
        i += 2
        continue

    # 한 개 해당 
    else:
        cnt +=1 
        #print(word[i:i+1], i,cnt)
        i += 1
        continue

print(cnt)


# 두번째 풀이 - replace 함수 사용 
a = ['c=','c-','d-','lj','nj','s=','z=', 'dz=']
alpha = input()

for i in a:
    alpha = alpha.replace(i, "*")

print(len(alpha))
print(alpha) # *e**ak