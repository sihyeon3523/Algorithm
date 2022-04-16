'''
22.04.16(토) 기준 헷갈리는 거 
리스트 컴프리핸션
iterrows (완료)
enumerate
lambda (완료)
사전 자료형(key 기준 매칭 & 검색)과 집합 자료형(중복제거)의 쓰임 (for문의 range 값으로 넣어줄 수 있음) (완료)

map 함수 쓰임 
순열 조합 
힙
큐(덱 포함)
sort(), sorted()
'''

# 타이타닉 프로젝트 중 잘 쓴 코드 모음 
df = pd.read_csv("titanic.csv")
df.Embared = df.Embarked.fillna('S')
df.Cabin = df.Cabin.apply(lambda x : str[x][:1])
df.Cabin.value_counts() # Cabin의 범주형 값을 기준으로 counting
df['Sex'] = df['Sex'].apply(lambda x: 1 if x == 'female' else 0)
df['Sex'].unique()
pd.get_dummies(df, columns = ['Pclass']) # columns를 더미 변수 변환하여 전체 데이터프레임 변환
df['Appelleation'] = df.Name.apply(lambda x : x.split(',')[1].split('.')[0])
df.Appelleation.apply(lambda x : x.strip())
'''
데이터프레임에서 문자열 치환 
여러 개 문자열 치환 => 딕셔너리 타입 사용 
리스트 타입을 사용해서도 여러 개 문자를 지정할 수 있다. 
리스트 형태로 치환할 대상 문자와 변환 문자를 지정하는 경우 요소수가 일치하지 않으면 에러가 발생
치환 대상 문자열을 리스트로 설정하고 변환 문자를 단일 형태로 지정해서 변환할 수 있음
이렇게 지정한 경우에는 치환 대상 문자열이 모두 단일 형태로 지정한 문자열로 치환
'''
# 여러개 문자열 치환 
df.replace({'CA':'California', 24:100})
df.replace(['CA', 24], ['California', 100])
df.replace(['CA', 24], 'XXX')

# 컬럼명 지정 문자열 치환
df.replace({'age': {24:100}})
df.replace({'age': {24:100, 18:0}, 'point': {24:50}})
df.replace({'age':24, 'point':70}, 100)
df.replace({'age': [24, 18], 'point': 70}, 100)

# 티켓을 같이 구매한 동행 수 구하기 
ticket_count = dict(df.Ticket.value_counts())
df.Ticket.apply(lambda x : ticket_count[x]) -1 

# 동행인들 중 
for ticket, cnt in ticket_count.items():
    if cnt > 1:
        tmp_df = df[df.Ticket == ticket]
        # 동행인들 중 나이가 25 이상 35 이하라면 
        for x in tmp_df.iterrows():
            if 25 <= x[1].Age <= 35: # x[1] : 행 전체 
                df.at[x[0], 'Breadwinner'] = 1 # x[0] : index 

'''
iterrows의 개념
데이터프레임에서 행에 반복적으로 접근하면서 값을 추출하거나
또는 그 값을 조작하는 일이 발생한다. 예를 들면, 특정 컬럼 A의 값에서
대문자 A를 찾아내 소문자 b로 변경한다고 가정해보자. 이런 경우에는
언제나 for-loop를 통한 반복문 코드 작성을 만들어야 한다. 

이럴 때 보다 효율적으로 접근하는 방법 중 하나가 iterrows()를 사용하는 경우이다. 

for i,row in bos_year_df.iterrows():
    print(i) # index 
    print(row) # series 형태의 값 
    print(type(row)) # series 형태로 반환

for row_tuple in bos_year_df.iterrows():
    print(row_tuple) # 
    print(type(row_tuple)) # tuple 형태로 반환 
'''
# 'Appellation_v3' 분류에 따른 나이 결측치 채워넣기
set(df.Appellation_v3) : 중복 제거 
for app in list(set(df.Appellation_v3)):
    tmp_mean = np.round(df[df.Appelation_v3 == app].Age.mean(), 2)
    df.loc[(df.Age.isna()) & (df.Appellation_v3 == app), 'Age'] = tmp_mean # loc : 이름 기반 접근 
