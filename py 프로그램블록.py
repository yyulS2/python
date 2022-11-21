#======================== 5장 프로그램블록
import random

#
# 중위수 중간값 median

# ______________________________builtins 함수 ; builtins 안에 포함되어있는 함수
help(len)
#도움말 확인하면 'in module builtins:' 문장에서 모듈에 의해 제공되는 함수임을 알 수 있다
dataset = list(range(1,7))
print(dataset)
# <출력> [1, 2, 3, 4, 5, 6]

print('len=',len(dataset))  # <출력> len= 6
print('sum=',sum(dataset))  # <출력> sum= 21
print('max=',max(dataset))  # <출력> max= 6
print('min=',min(dataset))  # <출력> min= 1






# _______________________________import 함수 ; 외부 모듈을 포함시켜야 사용 할 수 있는 함수

#방법1 ; 모듈명.함수()
#수학/통계 함수 statistics모듈을 import 해야한다
# 평균,중위수는 내장함수가 아니기 때문에 모듈을 impor해야한다
dataset = list(range(1,7))
print(dataset)
# <출력> [1, 2, 3, 4, 5, 6]
import statistics
print('평균=',statistics.mean(dataset))      # <출력> 평균= 3.5
print('중위수=',statistics.median(dataset))  # <출력> 중위수= 3.5


#방법2 ; .함수()
#statistics 중에서 variance,stdev 함수만 가져온다는뜻
#분산:variance, 표준편차:stdev
dataset = list(range(1,7))
print(dataset)
# <출력> [1, 2, 3, 4, 5, 6]
from statistics import variance, stdev
print('표본 분산=',variance(dataset))      # <출력> 표본 분산= 3.5
print('표본 표준편차', stdev(dataset))      # <출력> 표본 표준편차 1.8708286933869707



#builtins 모듈 내장함수와 내장클래스

import builtins
dir(builtins)  #dir 내장함수를 통해 builtins 내장함수 목록보기

abs(-36)     # 절댓값 함수 36
all()        # 모든 요소가 True 일때 True 반환
any()        # 하나 이상의 요소가 True 일때 True 반환
dict()       # 사전형 자료구조형으로 반환
dir()        #변수,내장함수,내장클래스 목록반환
enumerate()  # 열거형 자료 -> index 와 값을 같이 반환함 -> for문에서 많이쓰임
eval()       # 문자열 수식을 계산 가능한 수식으로 반환
float()      # 실수형으로 변환하여 반환
id()         #객체의 주소반환
input([])    # 키보드로 입력한 문자열을 반환
int()        # 정수형으로 반환
len()        # 전체 원소의 길이 반환
list()       # 자료형으로 반환
str()        #문자형으로 변환
tuple()      #튜플형으로 변환
open()       # 파일읽기 쓰기
pow(x,y)     # x를 y 제곱
range(n)     # 0 ~ n-1까지의 정수 반환
sorted()     # 반복가능한 원소들을 대상으로 정렬   # .sort : 오름차순 정렬 / .sort(reverse=true) : 내림차순정렬
zip()        #원소를 묶어서 반환 > tuple로 반환
bin()        # 10진수 -> 2진수
hex()        # 10진수 -> 16진수
oct()        # 10진수 -> 8진수
round(2.5)     # 반올림
# bankers rounding
# 소수점 앞자리 홀수 -> x=1,3,5,7,9 ... -> x.5~x.9 까지 반올림
# 소수점 앞자리 짝수 -> y=2,4,6,8,10... -> y.6~y.9 까지 반올림




# ________________________사용자정의함수 def

def userfun1() :
    print('인수가 없는함수')
    print('userfun1')
userfun1()
# <출력>
# 인수가 없는함수
# userfun1

def userfun2(x,y):
    print('userfun2')
    z = y-x
    print('z=',z)
userfun2(49,55)
# <출력> z= 6


# ★★ __________________return 있는 함수 ★★
def userfun3(x,y) :
    print('userfun3')
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a,b,c,d
x=int(input("x 입력 :"))
y=int(input("y 입력 :"))

a,b,c,d = userfun3(x,y)
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)








#_________________________________________________________________
from statistics import mean, variance
from math import sqrt
dataset = [2,4,5,6,1,8]
# mean, variance 를 불러오다
# 루트 sqrt



# 산술평균_________________________________________________________산술평균
def Avg(data) :               #dataset의 산술평균(Avg)
    return Avg
print("산술평균=",Avg)
#<출력> 산술평균= <function Avg at 0x00000281FFE09160>






# 분산/표준편차 __________________________________________________________분산/표준편차
# 분산(var) ; 관측값(d)에서 평균(avg)을 뺀 값을 제곱(**2)하고, 그것을 모두 더한 후 전체 수로 나눠서 구한다.
# 표준편차(sd) ; 분산(var)을 제곱근(sqrt)한 것
def Avg(data) :
    avg = mean(data)                     # 표준편차 공식에 쓰이기위해
    return avg
print("산술평균=",Avg(dataset))           # 평균=avg
# <출력> 산술평균= 4.333333333333333

def var_sd(data):                        # sd=표준편차, sqrt=루트, var=분산
    avg=Avg(data)                        # 위에서 구한 평균(산술평균) 가져옴
    diff = [(d-avg)**2 for d in data]    # 관측값에서 평균을 뺀 값을 제곱
    var = sum(diff)/ (len(data)-1)       # 분산 = 제곱하고, 그것을 모두 더한(sum(diff)) 후 전체 수로 나눠서 구한다. 분산 = /n-1
    sd=sqrt(var)                         # 표준편차(sd) ; 분산(var)을 제곱근(sqrt)한 것
    return var,sd

v,s=var_sd(dataset)
print('분산=',v)
print('표준편차=',s)
# <출력>
# 분산= 6.666666666666666
# 표준편차= 2.581988897471611



# 피타고라스 불러오기  (a밑변)**2 * (b높이)**2 = c빗변**2
def pytha(s,t) :
    a = s**2 - t**2
    b = 2*s*t
    c = s**2 + t**2
    print(" ", a,b,c)
pytha(2,1)     # <출력> 3 4 5



# 난수의 확률 분포 기대확률

# 방법1 앞 뒤 난수 확률 분포 함수 정의
import random
def coin(n) :                     # coin(수)
    result = []                   # result 는 리스트
    for i in range(n) :           # 난수 n 범위안에 있는수 i에
        r = random.randint(0,1)   # 0,1를 random으로 뽑는다= r로 정의
        if(r==1) :
            result.append(1)      # r=1 이면 result 에 1 넣어라
        else :
            result.append(0)      # 그게 아니면 0을 result에 담아라
    return result
print(coin(10))
# <출력> [1, 0, 0, 1, 1, 0, 1, 1, 0, 0]


# 방법2 몬테카를로 시뮬레이션 함수 정의
def monCoin(n) :             # monCoin 으로 정의
    cnt = 0
    for i in range(n) :
        cnt += coin(1)[0]    # 위에서 불렸던 coin 리스트에서 1하나씩 첫번째 수를 cnt변수에 누적
    result = cnt /n          # 누적결과를 시행횟수 n으로 나눠서 result 변수에 저장
    return result

print(monCoin(1000000))

# <출력> 0.500135






# 가변함수                                                     # 가변함수


def test(*arg) :
    print(type(arg))
test(1,2)   #<class 'tuple'>


# 튜플형
def Func1 (name, *names) :
    print(name)
    print(*names)
Func1("가","나","다")

# <출력>
# 가
# 나다

#Func1(a,b,c)    #오류


# 튜플형 _ 한줄에 나오게
def Func1 (name, *names) :
    print(name,end=' ')
    print(*names)
Func1("가","나","다")
# <출력>
# 가 나 다



# 딕트형
def emp_func(name,age,**other) :
    print(name)
    print(age)
    print(other)

emp_func("JAIN", 25 ,addr='la', height = 160, weight=50)
# <출력>
# JAIN
# 25
# {'addr': 'la', 'height': 160, 'weight': 50}




# 통계량 구하는 함수






# 일반함수

def adder(x,y) :
    add = x+y
    return add
print('add=',adder(20,30))
# <출력> add= 50


# 람다함수    한줄함수                                # 람다함수
print("add=",(lambda x,y:x+y)(20,30))
# <출력> add= 50
# lambda x,y : x+y -> 람다함수








#스코프                                                 #스코프

#지역변수
x=50
def local_fuc(x) :
    x+=50
local_fuc(x)
print('x=',x)
# <출력> x= 50

gun=10
def check (soldiers) :
    gun = 8    # 전역함수내 gun 값
    gun = gun-soldiers
    print({"[함수내]남은총:{0}". format(gun)})
    return gun  # 지역함수의 gun 값으로 배출

print ("전체총:{0}".format(gun))
print("남은총:{0}".format(gun))



#전역변수

x=50
def global_fuc() :
    global x
    x+=50
global_fuc()
print('x=',x)
# <출력> x= 100



# 일급함수 외부함수     _________________________________________________      일급함수 외부함수

# 일급함수 ; 함수를 객체로 만들어서 사용
def a() :                # 외부
    print('a 함수')
    def b():             #내부
        print('b 함수')
    return b             # 내부함수의 b 값을 외부함수로 호출
b= a()                   # <출력> a 함수
b()                      # <출력> b 함수
# 외부함수 호출 a() 함수  ;  함수 a()를 호출하면 내부함수 b()가 호출된다
#내부함수 호출


# 함수 클로저 ; 반환된 tot, avg 함수는 외부함수가 종료되어도 객체로 만들어지기 때문에 합계와 평균을 만들수있다

data = list(range(1,11))
def outer_func(data) :
    dataset=data                # data 값인 1~10까지의 list
    def tot():                  # 내부함수
        tot_val = sum(dataset)
        return sum(dataset)
    def avg(tot_val) :          # 구한 합계 tot_val 을 avg로 명칭
        avg_val = tot_val / len(dataset)   #전체합계를 dataset의 len로 나누면 평균값
        return avg_val
    return tot,avg              # 내부반환
tot,avg = outer_func(data)      # ★★★외부함수호출

tot_val=tot ()                  # tot_val 은 내부함수 def tot() 에서 return sum(dataset) 한 값
avg_val=avg (tot_val)           # avg_val 은 def avg(tot_val) 에서 return avg_val 한 값
print('tot=',tot_val)
print('avg=',avg_val)
# <출력>
# tot= 55
# avg= 5.5




# 산포도 중첩함수__________________________________________________________산포도 중첩함수
from statistics import mean                     #import
from math import sqrt

data=[1,2,3.5,4.5,5,6,7]
def func1(data) :
    dataset=data
    def avg_func():                             # 평균
        avg_val = mean(dataset)
        return avg_val
    def var_func(avg):                          # 분산 (변량-평균)**2
        diff=[(data-avg)**2 for data in dataset]
        print(sum(diff))
        var_val = sum(diff)/(len(dataset)-1)
        return var_val
    def sd_func(var):                           #표준편차 sd_func(var) () 안에 넣어줘야함
        sd_val=sqrt(var)
        return sd_val
    return avg_func,var_func,sd_func            #inner 변환

avg,var,sd = func1(data)                        # ★★외부함수호출

avg_val = avg()
var_val = var(avg_val)
sd_val = sd(var_val)

print('평균=',avg_val)
print('분산=',var_val)
print('표준편차=',sd_val)
# <출력>
# 27.357142857142858
# 평균= 4.142857142857143
# 분산= 4.559523809523809
# 표준편차= 2.1353041491843285





## 획득자 지정자____________________________________________________________획득자 지정자 getter setter

def m_func(n) :
    n_val = n             #내부함수에 영향을 미침
    def getter() :
        return n_val
    def setter(val) :     #setter(val) >> val 은 함수안의 새로운 결과값으로 정의
        nonlocal n_val    # nonlocal 은 항상 실행문 위에 먼저 내부함수마다 써줘야함
        n_val =val
    return getter,setter
getter, setter = m_func(100)
print('n=',getter())       # <출력> n=100
setter(200)                # setter 200으로 수정 후 getter값도 바뀜
print('n=',getter())       # <출력> n=200

"getter(획득자) 값 setter(지정자) 공유 = nonlocal 함수"




# 래퍼 함수                                                               래퍼함수 wrap
def wrap(func) :
    def decorated() :
        print('안녕하세요')    # 시작
        func()               # @wrap def hello 으로 지정한 인수 넘어올 것
        print('반갑습니다')    # 종료
    return decorated
@wrap
def hello() :
    print('여러분')
hello()                      # 함수호출

# <출력>
# 안녕하세요
# 여러분
# 반갑습니다











