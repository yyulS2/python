# 신유라


#[문항1]  다음의 조건에 따라 난수를 발생시키는 python code를 작성하시오.
#(난이도 : 3 / 배점 : 10점)
#(1) 1과 5 사이의 실수 난수를 한개 산출하시오.
#(2) 1과 5 사이의 정수 난수를 한개 산출하시오.


#(1)
import random
x = random.uniform(1,6)
print(x)



#(2)
import random
x = random.randint(1, 5)
print(x)

# 1,6 하면 6도 포함되어 1,5 해야함





#[문항2]  아래의 조건에 맞게 파이썬 클래스를 정의하고 업데이트된 은행잔고와 월이자액을 출력하시오.
#(난이도 : 3 / 배점 : 30점)
#[조건]
#1.    은행 잔고, 입금액, 출금액, 이자액을 기반한 현재 잔액 조회를 위한 파이썬 클래스 제작
#2.    생성자 포함
#3.    클래스 내 메서드 2개만 정의
#4.    현 은행 잔고, 입금액, 출금액을 기반하여 잔고 업데이트를 위한 메서드 1개 포함
#5.    업데이트된 현 잔고를 기반한 이자액 계산 메서드 1개 포함
#6.    현 은행 잔고: 20,000원, 입금액: 15,000원, 출금액: 13,000원
#7.    이자율은 월 0.1%  >>*0.001




class account:
    def __init__(self,bal,mon,wit,d):
        self.bal=bal
        self.mon=mon
        self.wit=wit
        self.d=d
    def update_acc(self):
        self.acc = self.bal + self.mon - self.wit
        return self.acc
    def display(self):
        self.r = self.acc* self.d
        return self.r

acc=account(20000,15000,13000,0.001)
acc2=acc.update_acc()
r=acc.display()
print("업데이트된 잔고 :",acc2,"원")
print("월이자액 :",r)

# <출력>
# 업데이트된 잔고 : 22000 원
# 월이자액 : 22.0








#[문항3]  아래의 조건에 맞게 파이썬 클래스를 정의하고 업데이트된 은행잔고, 월이자액, 세금액을 출력하시오.
#(난이도 : 4 / 배점 : 40점)
#[조건]
#1.    은행 잔고, 입금액, 출금액, 이자액을 기반한 현재 잔액, 이자액, 세금액 조회를 위한 파이썬 클래스 제작
#2.    생성자 포함
#3.    부모클래스와 자식클래스 제작
#4.    부모클래스에서는 현 은행 잔고, 입금액, 출금액을 기반하여 잔고 업데이트를 위한 메서드 1개 포함
#5.    자식클래스에서는 업데이트된 현 잔고를 기반한 이자액 계산 메서드 와 이자액에 기반한 세금액 산출 메서드, 총 2개의 메서드 포함
#6.    현 은행 잔고: 20,000원, 입금액: 15,000원, 출금액: 13,000원
#7.    이자율은 월 0.1% >>0.001
#8.    세율은 10%   >>0.1


class account:
    def __init__(self,bal,mon,wit,d,mul):
        self.bal=bal
        self.mon=mon
        self.wit=wit
        self.d=d
        self.mul=mul
    def update_acc(self):
        self.acc = self.bal + self.mon - self.wit
        return self.acc
    def display(self):
        self.r = self.acc* self.d
        return self.r
    def multi(self):
        mul2 = r * self.mul
        return mul2

acc=account(20000,15000,13000,0.001,0.1)
acc2=acc.update_acc()
r=acc.display()
mul2=acc.multi()
print("업데이트된 잔고 :",acc2,"원")
print("월이자액 :",r)
print("세금액 :",mul2)

# <출력>
# 업데이트된 잔고 : 22000 원
# 월이자액 : 22.0
# 세금액 : 2.2




#[문항4]  예외 처리를 위하여 try, except문을 사용할 때, except문에는 예상되는 예외를 명시해야 하는데,
# try문에서 어떤 오류가 발생할지 몰라 예외 클래스의 최상위 클래스를 사용하여 예외 처리를 하려고 한다. 여기서 지칭하는 최상위 클래스는 무엇인가?


Exception




#[문항5]  문자열 “autoexec.bat”에 다음 정규식을 이용하여 search 메서드를 사용한다면 결과는 어떻게 나올 것인지 기술하시오.
#(난이도 : 3 / 배점 : 10점)
#정규식:  .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)


import re
p = re.compile('.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)')
m = p.search("autoexec.bat")
print(m)

# <출력>
# <re.Match object; span=(0, 11), match='autoexec.ba'>

# 기술하라 하였으므로 코딩말고 결과만
# #<re.Match object; span=(0, 11), match='autoexec.ba'>














