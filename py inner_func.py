# 신유라


# 1.
# 현재잔고를 조회하는 사용자정의 함수를 정의하세요.
# 조건:
# 1) 외부함수 1개 (현잔고, 입금액, 출금액)
# 2) 내부함수 1개 현잔고,입금액, 출금액을 계산하여 업데이트된 잔고를 계산
# 3) 현잔고 : 10,000원 ,  입금액 : 5,000원, 출금액 : 8,000원
# 4) 업데이트된 잔고를 프린트하세요


# 현잔고:balance  입금액:money, 출금액:withdraw
a=balance = 10000
b=money = 5000
c=withdraw = 8000


def x(a,b,c) :                   # 임의변수를만들어야함
    bal = a                      # 외부함수에는 자료생성
    mon = b
    wit = c
    def y() :                     # 출금
        sum = bal+mon-wit         # 외부함수에서 만든 자료를 연산함
                                  # 결과값 = 현잔고 + 입금액 - 출금액
        return sum
    return y                      # 리턴할땐 함수는 괄호치면안댐

y2=x(10000,5000,8000)
print("업데이트된 잔고:",y2(),"원")
#<출력> 업데이트된 잔고: 7000 원
#print(y2())                      # 프린트할땐 함수는 열고닫고를 해야함










# 2.
# 현재잔고를 조회하는 사용자정의 함수를 정의하세요.
# 조건:
# 1) 외부함수 1개 (현잔고, 입금액, 출금액)
# 2) 내부함수 2개
# 2-1) 현잔고,입금액, 출금액을 계산하여 업데이트된 잔고를 계산
# 2-2) 업데이트된 잔고에 SQRT값을 계산(from math import sqrt, sqrt() 사용)
# 3) 현잔고 : 10,000원 ,  입금액 : 5,000원, 출금액 : 8,000원
# 4) 업데이트된 잔고에 SQRT값을 프린트하세요
#


# 현잔고:balance  입금액:money, 출금액:withdraw)
# 결과값 = 현잔고 + 입금액 - 출금액


a=balance = 10000
b=money = 5000
c=withdraw = 8000

from math import sqrt          # 예약어는 지정값 넣으면 안됌!!! from import 꼭 해주기
def x(a,b,c) :                 # 임의변수를만들어야함
    bal = a                    # 외부함수에는 자료생성
    mon = b
    wit = c
    def y() :
        sum = bal+mon-wit      # 외부함수에서 만든 자료를 연산
        return sum
    def sqrt2(sum) :
        sqrt_val = sqrt(sum)
        return sqrt_val
    return y, sqrt2

y,sqrt2 = x(10000,5000,8000)
sum=y()
sqrt_val=sqrt2(sum)

print("SQRT값:",sqrt_val)
#<출력> SQRT값: 83.66600265340756


# 3.
# 현재잔고를 조회하는 사용자정의 함수를 정의하세요.
# 조건:
# 1) 외부함수 1개 (현잔고, 입금액, 출금액)
# 2) 내부함수 2개
# 2-1) 현잔고,입금액, 출금액을 계산하여 업데이트된 잔고를 계산
# 2-2) 업데이트된 잔고에 SQRT값을 계산(from math import sqrt, sqrt() 사용)
# 2-3) SQRT 값에 '곱하는수' 를 곱하여 결과를 산출
# 3) 업데이트된 잔고액, SQRT값, 3번째 내부함수에서 결과된 결과를 프린트하세요
# 4) 현잔고 : 10,000원 ,  입금액 : 5,000원, 출금액 : 8,000원
# 5) 곱하는 수 : 3

# nonlocal 은 항상 실행문 위에 먼저 내부함수마다 써줘야함
# 현잔고:balance  입금액:money, 출금액:withdraw)
# 결과값 = 현잔고 + 입금액 - 출금액

a=balance = 10000
b=money = 5000
c=withdraw = 8000

from math import sqrt
def x(a,b,c,d) :                  # 임의변수를만들어야함
    bal = a                       # 외부함수에는 자료생성
    mon = b
    wit = c
    def y() :
        sum = bal+mon-wit         # 외부함수에서 만든 자료를 연산
        return sum
    def sqrt2(sum) :
        sqrt_val = sqrt(sum)
        return sqrt_val
    def sqrt3(sqrt_val) :
        sqrt_val2 = sqrt_val*d
        return sqrt_val2
    return y, sqrt2 , sqrt3
y,sqrt2,sqrt3 = x(10000,5000,8000,3)

sum=y()
sqrt_val=sqrt2(sum)
sqrt_val2=sqrt_val*3

print("업데이트된 잔고 : ", y() ,"원" )
print("SQRT값:", sqrt_val )
print("곱하는수:", sqrt_val2  )
#<출력>
#업데이트된 잔고 :  7000 원
#SQRT값: 83.66600265340756
#곱하는수: 250.99800796022268








