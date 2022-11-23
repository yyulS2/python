# 신유라


#문1)
# 다음 height 변수에 별(star)의 층수를 입력하면 각 층 마다 별의 개수가 한 개씩 증가하여 출력되고,
# 마지막 줄에 별의 개수가 출력되도록 함수의 빈칸을 채우시오.

#<출력결과>
#
#height : 3       #<-키보드 입력햇을때
#*
#**
#***
#start 개수 : 6

#함수정의
def StarCount(height2) :
    star = height = 0
    while height < height2 :
        height += 1
        print("*"*height)
        star += height
    return star

height2 = int(input('height2:'))
print('star 개수 : %d'% StarCount(height2))






#문2) 중첩함수를 적용하여 <조건>에 맞게 은행계좌 함수의 빈칸을 채우시오.
#
#<조건1> 외부함수 : bank_account() : 잔액(balance) outer변수
#<조건2> 내부함수 : getBalance() : 잔액확인 / deposit(money) :입금하기 / withdraw(money) : 출금하기
#<조건3> 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력

#<출력결과>
#최초 계좌의 잔액을 입력하세요 : 1000
#현재 계좌 잔액은 1000원 입니다.
#입금액을 입력하세요 :
#15000원 입금후 잔액은 16000입니다.
#출금액을 입력하세요 : 3000
#3000원 입금후 잔액은 13000입니다.
#
#

def bank_account(bal) :
    balance= bal #잔액초기화
    def getBalance(): #잔액확인 getter
        return balance
    def deposit(money) : #입금하기 setter

        nonlocal balance
        balance+=money
        print('입금 후 잔액은', getBalance(), "원 입니다.")

    def withdraw(money) : #출금하기 setter

        nonlocal balance
        if  balance >= money :
            balance -= money
            print('출금 후 잔액은', getBalance(),"원 입니다.")
        else :
            print("잔액이 부족합니다.")


    return getBalance, deposit, withdraw #클로저 함수리턴

getBalance, deposit, withdraw = bank_account(1000)

print('최초 계좌의 잔액을 입력하세요:',getBalance())
print('현재계좌잔액은', getBalance(),"원 입니다.")

a=int(input('입금액을 입력하세요:'))
deposit(a)


b=int(input('출금액을 입력하세요:'))
withdraw(b)








#문3)
#패토리얼 을 계산하는 재귀함수의 빈칸을 채우시오.


def Factorial(n) :
    if n==1 :
        return 1
    else :
        result = n * Factorial(n-1)
        return result

result_fact = Factorial(5)
print('패토리얼 결과:', result_fact)
# <출력> 2 3 4 5 패토리얼 결과: 120















