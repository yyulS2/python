##신유라

# 문1) 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오
# lst = [10,1,5,2]
# 단계1 : lst 원소를 2배 생성하여 result 변수에 저장 및 출력하기
# 단계2 : lst의 첫번째 원소에 2를 곱하여 result 변수에 저장 및 출력하기
# 단계3 : result의 홀수 번째 원소만 result2 변수에 추가 및 출력하기

#단계1
lst = [10,1,5,2]
result = lst*2
print("단계1:",result)        # <출력> 단계1 : [10, 1, 5, 2, 10, 1, 5, 2]

#단계2
lst2 = result[0]*2            # lst 첫번째 원소에 2 곱하기
result.append(lst2)           # result 확장
print("단계2:",result)         # [10, 1, 5, 2, 10, 1, 5, 2, 20]

#단계3

#result 홀수번째 원소
result2 = result[1::2]        #[1, 2, 1, 2]   # 자릿값 1에서부터 2씩증가 하는 자리값
print("단계3:",result2 )



# ex)홀수번째 자리에 있는 #[10,5,10,5,20] 찾으려면
# result3 = result[::2] >>자릿값 0에서부터 2씩 증가하는 자릿값 찾으면됨




# 문2) list 원소 추가 및 요소검사

# 문2-1)
# list 크기를 키보드로 입력받은 후 입력받은 크기만큼 임의 숫자를 list에 추가, list크기 출력
#
# [출력결과]
# vector 수 : 3
# 4
# 2
# 5
# vector 크기 : 3
#
# >>>>   입력받은 lst 개수 3개 통하여 크기,숫자 만들기


lst = [ ]                              # 1. 빈리스트생성

#크기 = b
b = int(input("vector 수:"))           # 2. input을 이용하여 값을 입력하고 이를 b라는 변수에 저장한다

for a in range(b) :                    # 3. 범위 b값을 불러올것
    lst.append(int(input()))           # 4. append이용 ; input(입력)값을 lst에 넣는다 >> range(b)에 충족되기전까지 계속 반복, 충족되면 for 문 나오기
                                       # 5. lst 출력
print ("vector 크기:",len(lst))




# 문2-2) list 크기를 키보드로 입력받은 후 입력받은 크기만큼 임의 숫자를 list에 추가,
# 이후 list에서 찾을 값을 키보드로 입력한 후 해당 값이 list에 있으면 "YES", 없으면 "NO" 출력
#
#
# [출력결과]
# vector 수 : 5
# 1
# 2
# 3
# 4
# 5
# 3
# YES
#
##### >> IF문 활용하기  1,2,3,4,5를 먼저 키보드로 입력받고 3 입력 하였을때 yes

lst=[]
b = int(input("vector 수:"))

for a in range(b) :
    lst.append(int(input()))    # input(입력)값을 lst에 넣는다


### 다 써놓고 따로 쓰고 같이 돌리면됨.....이걸두시간 생각

if int(input()) in lst  :                   # lst에서 찾을 값을 키보드로 입력한 해당 값이 list에 있으면
    print("YES")             # "YES"
else :                       # 없으면
    print("NO")             # "NO" 출력





# 문3) list내포 이용 문자열 처리 >> 실행문 for 변수 in 열거

# 문3-1)
# message 변수를 대상으로 'spam' 원소는 1, 'ham' 원소는 0으로 dummy변수를 생성하시오
# <조건> list + for 형식 적용
# [출력]=[1,0,1,0,1]



message = ["spam","ham","spam","ham","spam"]
dummy = [1 if a=="spam" else 0 for a in message]
print(dummy)
# <출력> [1, 0, 1, 0, 1]
#변수=a

#dummy = [ spam 이면 1 ham이면 0 messge에서 ]   #spam=[1] ,ham=[0]
#dummy = [1 if a=="spam" for a in message]   >> 1을실행. 만약 a가 "spam"이면 for message안에 있는 변수 a
# if함수 사용 했으니 else 사용




# 문3-2)
# message 변수를 대상으로 'spam' 원소만 추출하여 spam_list에 추가
# <조건> list+for+if 형식 적용             >>for a in list if조건식
# [출력]=['spam','spam','spam']

message=['spam','ham','spam','ham','spam']
spam_lst = [a for a in message if a=="spam"]
print(spam_lst)
# <출력> ['spam', 'spam', 'spam']




# 문4)
# position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수를 출력하시오.
# position = ['과장','부장','대리','사장','대리','과장']
# [출력결과]
# 중복되지않은 직위 : ['사장','과장','대리','부장']
# 각 직위별 빈도수 : {'과장':2, '부장':1, '대리':2, '사장':1}

#중복되지 않은 직위   >>    중복원소제거   >> set 함수이용
position = ['과장','부장','대리','사장','대리','과장']
sp = set(position)           # list -> set
lp = list(sp)                # set -> list  >> ['부장', '과장', '대리', '사장']
print("중복되지않은 직위:",lp)
# <출력> 중복되지않은 직위: ['부장', '과장', '사장', '대리']


# 각직위별 빈도수
position = ['과장','부장','대리','사장','대리','과장']
wc = {}                       #dic함수
for a in position :
    wc[a] = wc.get(a,0) + 1
print("각 직위별 빈도수:", wc)
# <출력> 각 직위별 빈도수: {'과장': 2, '부장': 1, '대리': 2, '사장': 1}















