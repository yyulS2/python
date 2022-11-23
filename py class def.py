#신유라

# 1) 현재 잔고를 조회하는 클래스를 정의하세요.
# 조건
# 생성자(현잔고,입금액,출금액)
# method 1개
# 현잔고 : 10,000원 ,  입금액 : 5,000원, 출금액 : 8,000원
# 업데이트된 잔고를 프린트하세요


class account:
    def __init__(self,bal,mon,wit):
        self.bal=bal
        self.mon=mon
        self.wit=wit
    def update_acc(self):
        acc = self.bal+self.mon-self.wit
        return acc

acc=account(10000,5000,8000)
acc2=acc.update_acc()
print("업데이트된 잔고 :",acc2,"원")

# <출력> 업데이트된 잔고 : 7000 원



# 2) 현재 잔고와 SQRT값을 조회하는 클래스를 정의하세요.
# 조건
# 생성자(현잔고,입금액,출금액)
# method 2개
# 현잔고 입금액 출금액을 계산하여 업데이트 된 잔고를 계산
# 업데이트된 잔고에 SQRT값을계산 (from math import sqrt,sqrt() 사용)
# 현잔고 : 10,000원 ,  입금액 : 5,000원, 출금액 : 8,000원
# 업데이트된 잔고를 프린트하세요


from math import sqrt
class account:
    def __init__(self,bal,mon,wit):                   # sqrt는 함수값이니까 변수에 담는것 아님
        self.bal=bal
        self.mon=mon
        self.wit=wit

    def update_acc(self):
        self.acc = self.bal + self.mon - self.wit     # 추가 메서드 할 경우 이 결과값을 self 화 시키면 됨
        return self.acc                               # 항상 return 값으로

    def display(self):
        sqrt2 = sqrt(self.acc)
        return sqrt2

acc=account(10000,5000,8000)
acc2=acc.update_acc()                                  # 메서드 불러오기
print("업데이트된 잔고 :",acc2,"원")

sqrt2=acc.display()
print("sqrt값 :",sqrt2)

# <출력>
# 업데이트된 잔고 : 7000 원
# sqrt값 : 83.66600265340756



# 3) 현재 잔고와 SQRT값을 조회하는 클래스를 정의하세요.
# 조건
# 생성자(현잔고,입금액,출금액,곱하는수)
# method 3개
# 현잔고 입금액 출금액을 계산하여 업데이트 된 잔고를 계산
# 업데이트된 잔고에 SQRT값을계산 (from math import sqrt,sqrt() 사용)
# SQRT 갑에 '곱하는수' 곱하여 결과 산출
# 현잔고 : 10,000원 ,  입금액 : 5,000원, 출금액 : 8,000원
# 업데이트된 잔고를 프린트하세요



from math import sqrt
class account:
    def __init__(self,bal,mon,wit,mul):
        self.bal=bal
        self.mon=mon
        self.wit=wit
        self.mul=mul

    def update_acc(self):
        self.acc = self.bal + self.mon - self.wit
        return self.acc

    def display(self):
        self.sqrt2 = sqrt(self.acc)
        return self.sqrt2

    def multi(self):
        mul2 = sqrt2 * self.mul
        return mul2

acc=account(10000,5000,8000,3)
acc2=acc.update_acc()
print("업데이트된 잔고 :",acc2,"원")

sqrt2=acc.display()
print("sqrt값 :",sqrt2)

mul2=acc.multi()
print("sqrt*곱한수 값 :",mul2)

# <출력>
# 업데이트된 잔고 : 7000 원
# sqrt값 : 83.66600265340756
# sqrt*곱한수 값 : 250.99800796022268












