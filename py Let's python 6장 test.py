# 신유라


# Q1)
# 멤버변수 : 가로(width) 세로(height)
# 멤버변수 초기화
# 메서드(area_clac) : 사각형 넓이 함수 / 넓이 = 가로*세로
# 메서드(circum_clac) : 사각형 둘레 함수 / 둘레 = (가로+세로)*2

print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))

class calculate :
    wid=hei=0
    def __init__(self,wid,hei) :
        self.wid = wid
        self.hei = hei
    def area_clac (self) :
        area = self.wid * self.hei
        return area
    def circum_clac(self):
        circum = (self.wid + self.hei) *2
        return circum

cal=calculate(w,h)
print('-'*40)
area=cal.area_clac()
print('사각형의 넓이 :',area)
circum=cal.circum_clac()
print('사각형의 둘레:',circum)
print('-'*40)



# Q2) 산포도 구하는 클래스 정의
from statistics import mean
from math import sqrt

x = [5,9,1,7,4,6]
class Scattering:
    def __init__(self,x):
        self.x = x
    def var_func(self):
        avg = mean(self.x)
        diff = [ (d - avg) ** 2 for d in self.x]
        self.var = sum(diff) / (len(self.x) - 1)
        return self.var
    def std_func(self):
        sd = sqrt(self.var)
        return sd

Scat=Scattering(x)

var2=Scat.var_func()        # 메서드 불러오기
print("분산 :",var2)         # <출력> 분산 : 7.466666666666666

sd=Scat.std_func()          # 메서드 불러오기
print("표준편차 :",sd)       # <출력> 표준편차 : 2.7325202042558927


#Q3) Person 클래스 정의


name = input('이름:')
age = int(input('나이:'))
gender = input('성별(male/female : ')

class Person :
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
        print("=" * 30)
    def display(self):
        if self.gender == "female" :
            print("이름 : {}, 성별 : {}\n나이 : {}".format(self.name,"여자",self.age))
        else :
            print("이름 : {}, 성별 : {}\n나이 : {}".format(self.name, "남자", self.age))
        print("=" * 30)

p=Person(name,gender,age)         #객체멤버
p.display()



# Q4) Employee 클래스를 상속받아서 Permanent와 Temporary클래스 구현

class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
    def pay_calc(self):
        pass

# 자식클래스 정규직    
class Permanednt(Employee) :
    base = 0
    bouns =0
    def __init__(self,name,base,bouns):
        super().__init__(name)          #부모 생성자 호출
        self.pay = base + bouns

# 자식클래스 임시직
class Temporary(Employee): 
    def __init__(self,name, time, tpay):
        super().__init__(name)
        self.pay = time * tpay

        
empType=input("고용형태 선택(정규직<P>, 임시직<T> : ")
if empType == 'P' or empType == 'p' :         #정규직
    name = input('이름 : ')
    base = int(input('기본급 : '))
    bonus = int(input('상여금 : '))

    print('='*30)

    p = Permanednt(name, base, bonus)
    print('고용형태 : 정규직')
    print('이름:', p.name)
    print('급여:', format(p.pay, '3,d'))

elif empType == 'T' or empType == 't' :       #임시직
    name = input('이름 : ')
    time = int(input('작업시간 : '))
    tpay = int(input('시급 : '))

    print('='*30)

    t = Temporary (name, time, tpay)
    print('고용형태 : 임시직')
    print('이름:', t.name)
    print('급여 : ', format(t.pay, '3,d'))

else :
    print('='*30)
    print('입력오류')



    # Q5) 사칙연산 관련 패키지와 모듈 작성, 다른 모듈에서 import 결과를 확인

from myCalcpackage.calcModule import Add,Sub,Mul,Div

x=10
y=5
print('Add =',Add(x,y))
print('Sub =',Sub(x,y))
print('Mul =',Mul(x,y))
print('Div =',Div(x,y))

# <출력>
# Add = 15
# Sub = 5
# Mul = 50
# Div = 2.0



