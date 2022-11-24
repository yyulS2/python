# 재귀함수

def Counter(n) :
    if n == 0 :                # 0 호출하면 종료
        return 0
    else :
        Counter(n-1)           #재귀
        print(n, end=' ')
Counter(5)
# <출력> 1 2 3 4 5


# 재귀함수 누적합

def Add(n) :
    if n==1 :
        return 1
    else :
        result =  n+Add(n-1)           #재귀
        print(n, end = ' ')
        return result
print ("n=1 : ", Add(1))     # <출력> n=1 :  1
print ("\nn=5 : ", Add(5))
# <출력>
# 2 3 4 5
# n=5 :  15










###              6장 객체지향프로그래밍                    ##

# class 정의

class calc_class :
    x=y=0
    def __init__(self,a,b) :
        self.x = a
        self.y = b

    def plus(self):
        p = self.x  +  self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10,20)
print('plus=',obj.plus())
print('minus=',obj.minus())
# <출력>
# plus= 30
# minus= -10



##
##

class Car :
    cc = 0
    door = 0
    carType = 0
    def __init__ (self,cc,door,carType) :
        self.cc = cc
        self.door = door
        self.carType = carType
    def display(self):                    # return 은 없음
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s" %(self.cc, self.door,self.carType))

car1 = Car(2000,4,"승용차")                #참조변수:car1,car2 // car(실인수)
car2 = Car(3000,6,"suv")

car1.display()                            #메소드도 함수이므로 괄호
car2.display()
#<출력>
#자동차는 2000 cc이고, 문짝은 4개, 타입은 승용차
#자동차는 3000 cc이고, 문짝은 6개, 타입은 suv



class multiply :
    x=y=0
    def __init__ (self,x,y) :
        self.x = x
        self.y = y
    def mul(self):
        return self.x * self.y
obj = multiply(10,20)
print("곱셈 =",obj.mul())
# <출력> 곱셈 = 200



# 생성자 없을경우
class multiply2 :
    x=y=0
    def __init__(self):             # 생성자 없을경우
        pass                        # 생성자 없을경우
    def data(self,x,y):
        self.x = x
        self.y = y
    def mul(self):
        return self.x * self.y

obj = multiply2()                  #기본생성자
obj.data(10,20)                    #동적 변수 생성
print("곱셈 =",obj.mul())
# <출력> 곱셈 = 200




#  init 없이 self 만 사용하여 메소드안에서 result 값 받기
class multiply3 :
    #x=y=0
    #def __init__(self):
        #pass
    def data(self,x,y):
        self.x = x
        self.y = y
    def mul(self):
        result = self.x * self.y
        self.display(result)
    def display(self,result):
        print("곱셈 = %d" %(result))

obj = multiply3()      #기본생성자
obj.data(10,20)        #동적 변수 생성
obj.mul()
# <출력> 곱셈 = 200


# 클래스 맴버  # 클래스 메서드(cls) 사용////객체메서드(self)사용

class datepro :
    content = "날짜처리클래스"
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def display(self):                      # 객체 메서드
        print("%d-%d-%d" % (self.year, self.month,self.day))
    @classmethod                            # 클래스 메서드 -> 함수장식자 필요함!!!!
    def date_string(cls,datestr):           # datestr : date string 에 새로 입력받을 값
        year = datestr[:4]
        month = datestr[4:6]
        day = datestr[6:]
        print(f"{year}년 {month}월 {day}일")

#객체
date=datepro(2022,9,6)           # 생성자
print(date.content)              # <출력> 날짜처리클래스
print(date.year)                 # <출력> 2022
date.display()                   # <출력> 2022-9-6

#클래스
print(datepro.content)              # <출력> 날짜처리클래스
datepro.date_string('20220906')     # <출력> 2022년 09월 06일





#     캡슐화       #

class Account:
    __balance = 0                #잔액
    __accName = None             #예금주
    __accno = None               #계좌번호
    def __init__(self,bal,name,no) :
        self.__balance = bal     #잔액초기화
        self.__accName = name
        self.__accno = no
    #getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accno
    #setter 입금
    def deposit(self , money):
        if money < 0 :
            print('금액확인')
            return
        self.__balance += money
    #setter 출금
    def withdraw(self, money):
        if self.__balance < money :
            print('잔액부족')
            return
        self.__balance -= money
acc = Account ( 10000, 'JANE', '125152412541')

bal = acc.getBalance()
print('계좌정보 : ',bal)
# <출력> 계좌정보 :  (10000, 'JANE', '125152412541')

acc.deposit(3000)
bal = acc.getBalance()
print('계좌정보 : ',bal)
# <출력> 계좌정보 :  (13000, 'JANE', '125152412541')






#                                상속                                  #

class Super :                        # super클래스생성
    def __init__(self,name,age):     # 동적멤버변수 생성
        self.name = name
        self.age = age

    def display(self):              # 동적멤버변수 출력하는 역할
        print('name : %s , age : %d' % (self.name,self.age))
sup = Super('부모',55)
sup.display()                       # ★부모멤버 호출
# <출력> name : 부모 , age : 55

class Sub(Super) :
    gender = None                   # 자식멤버
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print('name : %s , age = %d, gender : %s' %( self.name, self.age,self.gender))
sub = Sub('자식',25,'여')
sub.display()                       # ★자식멤버호출
# <출력> name : 자식 , age = 25, gender : 여


#                     Super 클래스          # super().__init()   >> 부모 클래스 호출

# 1. 부모클래스
class Parent :
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def display(self):
        print('name : %s , job : %s' % (self.name, self.job))
        #print('name : {}, job :{}'.format(self.name, self.job))

p = Parent('철수','회사원')
p.display()
# <출력> name : 철수 , job : 회사원



# 2. 자식클래스
class Children(Parent) :   # 위의 부모클래스에서 상속받음 (Parent)
    gender = None
    def __init__(self,name,job,gender) :
        # 부모 클래스에서 생성자 호출해서 받은 멤버변수 =>  초기화
        super(). __init__(name,job)    # =>  name, job 초기화
        self.gender = gender           # gender 추가
    def display(self):
        print('name : {}, job :{}, gender : {}'.format(self.name, self.job,self.gender))

chil = Children('YUNA','techer','여')
chil.display()
# <출력> name : YUNA, job :techer, gender : 여





#                            메서드 재정                              #
class Employee:
    neme = None
    pay = 0
    def __init__(self,name):
        self.name = name
    def pay_calc(self):               # 부모클래스에서 사용하지않음 => pass
        pass
class Permanent(Employee) :
    def __init__(self,name):
        super().__init__(name)
    def pay_calc(self,base,bonus):    # 정규직
        self.pay = base+bonus
        print('총 수령액:', format(self.pay,'3,d'),'원')        # 3,d 에 공백 있으면 안됨
class Temporary(Employee) :
    def __init__(self,name):
        super().__init__(name)
    def pay_calc(self,tpay,time):
        self.pay = tpay*time
        print('총 수령액:',format(self.pay,'3,d'),'원')

p = Permanent('정규직')
p.pay_calc(3000000,200000)             # <출력> 총 수령액: 3,200,000 원

t = Temporary('임시직')
t.pay_calc(15000,50)                   # <출력> 총 수령액: 750,000 원




#                             다형성                           #
class Flight :
    def fly(self):
        print('날다','fly 원형 메서드')
class Airplane(Flight) :
    def fly(self):
        print('비행기가 날다')
class Bird(Flight):
    def fly(self):
        print('새가 날다')
class Paper(Flight) :
    def fly(self):
        print('종이가 날아가다')

flight=Flight()
air=Airplane()
bird=Bird()
paper=Paper()

flight.fly()
# <출력> 날다 fly 원형 메서드

flight=air
flight.fly()
# <출력> 비행기가 날다

flight=bird
flight.fly()
# <출력> 새가 날다

flight=paper
flight.fly()
# <출력> 종이가 날아가다













