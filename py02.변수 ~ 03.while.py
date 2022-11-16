##변수를 만드는 방법

[a,b]=['파이썬','삶']

#여러개의 변수에 같은 값 대입
a=b='파이썬'

#두변수의 값을 바꿈
b=5
a,b=b,a  #*




##파이썬 교재 37pg

#type : 자료형을 확인할때 이용하는 내장함수
# >> 문자열;class 'str' 정수형;class 'int' 실수형;class 'float' 논리형;class 'bool'

#문자열
var1 = "Hello python"
print(var1)
print(type (var1))             ## <class 'str'>

#정수형
var1=100
print(var1)
print(type (var1))             ## <class 'int'>

#실수형
var1=10.25
print(var1)
print(type (var1))            ##<class 'float'>

#논리형
var1 = True        #True 첫글자는 대문자여야함
print(type (var1))             ##<class 'bool'>



## 41pg 할당연산자
#같은 줄에 중복 출력
print('출력1', end=' , ')       #end='구분자'
print('출력2')
print('출력3')

#패킹할당
lst = [1,2,3,4,5]
v1 , *v2 =lst       ###맨앞의 숫자만 빼고 뒤의 숫자는 패킹
print(v1,v2)

*v1,v2,v3 =lst
print(v1,v2,v3)    ### [1, 2, 3] 4 5    >>  앞의 세개는 패킹 뒤의 두 숫자는 따로

v1,v2,*v3 = lst
print(v1,v2,v3)    ### 1 2 [3, 4, 5]   >>    앞의 두개는 따로 뒤에세개는 패킹


v1,*v2,v3=lst
print(v1,v2,v3)     ## 1 [2, 3, 4] 5



## input 함수 ; 문자열=str 으로 저장됨  >> 숫자 입력해도 문자열로 저장됨
## 콘솔창에서 num 입력

num = input("숫자입력:")  #>> 콘솔창에  숫자입력
print('num type: ', type(num))   #★★★★★
print(type(num))   # 위와같음
print(num*2)  # 문자이기때문에 숫자여도 곱하기 아니고 숫자가 반복됨

#문자형을 정수로 변환
num1 =int(input("숫자입력: "))
print('num1 type: ', type(num1))   # num1 type:  <class 'int'>


#문자형 실수로 변환
num2=float(input("숫자입력: "))
print('num2 type: ', type(num2))   # num2 type:  <class 'float'>  >> 30.0

# 실수 = 정수+실수
num1+num2          # 70.0


#print
a = 10+20+30+40+50
print("value=",a)


# sep 값을 특수문자로 구분

print("012","3456","7890",sep="-")



# ??? end 인수

print("value=",10 , end= ",")
print("value=",20)


##format
print("금액",format(100000, "5d") )
print("금액",format(100000, "3,d"))
print("원주율",format(3.14159, "5.3f"))
print("8진수",format(101010,"10o"))


#양식문자
name="유라"
age=29
price=123.45
print("이름:%s,나이:%d,data=%.2f"%(name,age,price))


#===================================================#

###string 문자열

string = "python"
print(string[2])     ###대괄호사용
print(string[-1])


#문자열 연산 (문자+숫자합칠때)
print("python-"+str(3.7)+".exe")

#s.find 와 s.index 차이 /
s="python"
s.index(f)
s.find(f)


#글자수반환
oneline="this is one line string"
print('t 글자수:', oneline.count('t'))

#접두어 문자 판단
print(oneline.startswith('that'))
print(oneline.startswith('this'))

#교체
print(oneline.replace('this','that'))

#분리 split(문장>문장)   ___★★★
multiline="""this is
multi line
string"""
sent=multiline.split('\n')   # ['this is', 'multi line', 'string']
print('문장:',sent)         ##  문장: ['this is', 'multi line', 'string']



#분리 split(문장>단어)   ___★★★
oneline="this is one line string"
words=oneline.split(' ')   #['this', 'is', 'one', 'line', 'string']
print('단어:',words)       # 단어: ['this', 'is', 'one', 'line', 'string']


#결합 join (단어>문장)
sent2=','.join(words)  # ['this', 'is', 'one', 'line', 'string']
print(sent2)  #this,is,one,line,string



####   3장   ####

# if 문

#단일조건문
var=10   #조건문에서 사용될 변수
if var>=5 :
    print('var=', var)
    print('var는 5보다 크다')
    print('조건이 참인 경우 실행')    #실행됨

var=4   #조건문에서 사용될 변수
if var>=5 :
    print('var=', var)
    print('var는 5보다 크다')
    print('조건이 참인 경우 실행')     #실행안됨



# if, else
score=int(input('점수입력:'))
if score >=85 and score <=100 :
    print('우수')
else :                  # else 다음엔 조건문 쓰는거 아님
    if score >=80 :     # 콜론 써야함
        print('보통')     #콘솔창에 결과 나타남

## 중첩조건문

score=int(input('점수입력:'))
grad =''

if score>=85 and score <=100 :
    grade='우수'
elif score >=70 :
    grade = '보통'
else :
    grade='저조'         #콘솔창 오른쪽에 결과 나타남




# 삼항조건문

# while문 64pg

cnt=tot=0
while cnt<5 :
    cnt += 1    #cnt=cnt+1
    tot +=cnt    #누적변수 tot ; tot+cnt
    print(cnt,tot)



#3의배수들의 합과 그 수들(원소들)
cnt=tot=0
dataset=[]
while cnt <100 :
    cnt +=1       # cnt=cnt+1
    if cnt %3 ==0 :       # 콜론빠트리지않기
        tot+=cnt
        dataset.append(cnt)

print ('1~100사이 3의배수 합 =%d' % tot)   #1683
print('dataset = ', dataset)











# for문 70pg

























