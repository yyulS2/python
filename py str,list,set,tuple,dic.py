
#_____________리스트내포; list 안에 for , if 사용하는 문법

# 형식1) 변수=[실행문 for 변수 in 열거형객체]

x=[1,2,3,4,5]
print (x**2)
# <출력> TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

lst = [y**2 for y in x]
print(lst)
# <출력> [1, 4, 9, 16, 25]

#>> 직접 곱하면 error
####
lst = [y**2 for y in x]
print(lst)
# <출력> [1, 4, 9, 16, 25]
# x객체의 원소를 하나씩 y변수에 넣어서 **2 해준다



# 형식2) 변수=[실행문 for 변수 in 열거형객체 if 조건문]  >> 조건문이 true 일때

#1~10까지의 수에서 2의 배수 추출 > i*2 > lst에 저장

#############       ???           ###
lst = list(range(1,11))             # 1~10까지의 수
lst2=[i*2 for i in lst if i%2==0]   # 2의 배수 추출 > 조건문 i%2==0 / 변수=i
print(lst2)
# <출력> [4, 8, 12, 16, 20]







# 형식3) 변수=[값1 if 조건 else 값2 for 변수 in 열거형 객체]   >> 조건문이 false 일때





#                                             tuple ; 콤마 이용하여 값 생성

# 1) 원소 한개
t1=(1,0)
print(t1)
# <출력> {tuple:2} (1, 0)

# 2) 원소 여러개
t2 = (1,2,3,4)
print(t2)
# <출력> {tuple:4} (1, 2, 3, 4)

# 3) 튜플 색인
t3 =(t2[0],t2[1:3],t2[-1])
print(t3)
# <출력> {tuple:3} (1, (2, 3), 4)

# 4) 요소반복
for a in t2 :
    print(a,end='')     # 행으로 나열
# <출력> 1234

for a in t2:
    print(a)            # 열로 나열
# <출력>
# 1
# 2
# 3
# 4


    # //행으로 나열 end = '' : x에 대한 값을 행으로 나열

    print(a) # <출력>답이 1열로 나열

# 5) 요소검사
if 5 in t2 :
    print ("5 있음")
else :
    print("5 없음")
# <출력> 5 없음



# 6) 관련함수
# 6-1) 자료형 변환
lst = list(range(1,6))
t4 = tuple(lst)
print(t4)
# <출력> (1, 2, 3, 4, 5)



# 6-2) count, index

#t4=(1, 2, 3, 4, 5)

t4=(1, 2, 3, 4, 5)
print(len(t4),type(t4))     # <출력> 5 class 'tuple'
print(t4.count(2))          # <출력> 1
print(t4.count(3))          # <출력> 1

t5 = (1,2,3,3,5,6)
print(t5.count(3))          # <출력> 2

# .count ; 원소 숫자 3의 갯수 값

t4=(1, 2, 3, 4, 5)
print(t4.index(3))     #<출력> 2

t6 = (1,2,(3,4),5,6)
print(t6.index(5))     # <출력> 3
print(t6.index(3))     # <출력> ValueError: tuple.index(x): x not in tuple
print(t6.index(3,4))   # <출력> ValueError: tuple.index(x): x not in tuple



# ________________________________________________set
# 중복값 x, 중괄호 {}, 비순서형
# 1) 요소 중복
s = {1,2,3,2,3,5,6}

for a in s :
    print (a, end='')
    # <출력> 12356

# 2) 집합관련

s1 = {0,1,3,5,7,9}
s2 = {0,2,4,6,8}

# 2-1) 합 .union
print(s1.union(s2))
# <출력> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# 2-2) 차 .difference
print(s1.difference(s2))
# <출력> {1, 3, 5, 7, 9}
print(s2.difference(s1))
# <출력> {8, 2, 4, 6}


# 2-3) 교 .intersection
print(s1.intersection(s2))
# <출력> {0}


# 3) 추가 .add
s3={11,12}
print(s3.add(s2))
# <출력> TypeError: unhashable type: 'set'
#>> 오류 > .add 값 뒤에는 원소값이 들어가야함

print(s3.add(13))
# <출력> None
#>> 형식 잘못되어 none 값 나옴

s3.add(13)
print(s3)
# <출력> {11, 12, 13}

# 4) 삭제 .discard   >>> add 와 같은 원리로

s4 = {14,15}
s4.discard(15)
print(s4)
# <출력> {14}





# __________________________________________ dic
# 단어 빈도수(word count=wc) 구하기

data = ['1','2',',3','4'',2','2','3']
wc={} #빈셋

for key in data :             # for 요소반복 문으로 data 값을 순차적으로 key라는 변수로 넘겨 받음
    wc[key] = wc.get(key,0)+1
print(wc)
# <출력> {'1': 1, '2': 2, ',3': 1, '4,2': 1, '3': 1}

    # 받은 key 값을 wc로 지정 / get()함수로 키 값을 하나씩 빼온다.
    # get(x, '디폴트 값') Key 값이 없을 경우 미리 정해 둔 디폴트 값(=0)을 가져옴
    # data 1 값을 가져왔을때 key 값인 wc는 빈셋으로 값이 없으므로 디폴드값(=0) 을 가져와 we[key]=0+1=>>1 이되고 wc={1}
    # data 2 값을 가져왔을때 key 값인 wc는 wc={1} 으로 2가 없어 디폴드값(=0) 을 가져와 we[key]=0+1=>>1 이되고 wc={1,2}
    # data 3 값을 가져왔을때 key 값인 wc는 wc={1,2}이므로 3이 없어 디폴드값(=0) 을 가져와 we[key]=0+1=>>1 이되고 wc={1,2,3}
    # data 4 값을 가져왔을때 key 값인 wc는 wc={1,2,3} 이므로 4가 없어 디폴드값(=0) 을 가져와 we[key]=0+1=>>1 이되고 wc={1,2,3,4}
    # data 2 값을 가져왔을때 key 값인 wc는 wc={1,2,3,4} 이므로 2가 있어 디폴드값(=0)이 아닌 we[key]=1+1 >>  이되고

print(wc)
# <출력> {'1': 1, '2': 2, ',3': 1, '4,2': 1, '3': 1}































