# 신유라
#
# Q1) [문항1]  List내포를 이용하여 다음 문자열을 처리하시오.
# message2 = [ ‘ham’, ‘ham’, ‘spam’, ‘ham’, ‘spam’, ‘spam’, ‘ham’]
# message2변수를 대상으로 ‘ham’원소만 추출하여 ham_list를 추가하시오.
#[‘ham’, ‘ham’, ‘ham’, ‘ham’]

message2 = [ 'ham','ham','spam','ham','spam', 'spam','ham']
ham_list = [a for a in message2 if a=="ham"]
print(ham_list)
# <출력> ['ham', 'ham', 'ham', 'ham']


# Q2) 2, -4, 6, -8, 10 ~ -200 까지의 합을 구하는 python code를 작성하시오.

cnt = cnt2 = cnt3 = tot = 0
dataset = []
while cnt < 201:
    cnt += 1
    if (cnt % 2) == 0:
        cnt2 += 1
        if (cnt2 % 2) == 0:
            cnt3 = cnt*(-1)
            tot += cnt3
            dataset.append(cnt3)
        else:
            tot += cnt
            dataset.append(cnt)

print(' 2, -4, 6, -8, 10 ~ -200 까지의 합 = %d' % tot)
# <출력>  2, -4, 6, -8, 10 ~ -200 까지의 합 = -100







# Q3)  while문을 사용하여 아래 그림과 같이 별(*)을 표시한 100층의 별 피라미드를 구성하였다.
#(1) 100층의 별피라미드를 구성하는 프로그램을 작성하시오.
#(2) 프로그램을 이용하여 50층에서 별(*)의 개수를 구하시오
#(3) 프로그램을 이용하여 50층에서의 왼쪽 공백 수를 구하시오.


cnt = -1
tot = 0
while cnt <201 :
    cnt += 2
    tot = '*'*cnt
    print(f'{tot:^201}')


star = 0
blank = 0

for i in range(1,100):
    if i == 50:
        blank += 1
    for j in range(i):
        if i == 50:
            star += 1
print('50층에서의 별(*)의 개수:', star * 2 - 1)
print('50층에서의 왼쪽 공백 수 :', blank)



i = 0
while True:
    if i >= 100: break
    print("{0:^199}".format("*"*(i*2+1)))
    i += 1

star = 0
blank = 0
for i in range(1, 100):
    for j in range(100-i):
        if i == 50:         # 50번째 줄일 때
            blank += 1     # 왼쪽 공백 카운트
    for j in range(i):
        if i == 50:         # 50번째 줄일 때
            star += 1     # 왼쪽 + 가운데 별 카운트

print('50층에서 별 개수 :', star * 2 - 1)
print('50층에서 왼쪽 공백 수 :', blank)

# <출력>
# 50층에서 별 개수 : 99
# 50층에서 왼쪽 공백 수 : 50









totno=0
def count_star(n):  #n층에 별 개수 세는 함수
    cntstar=0
    cntstar = 2*n-1  #1,3,5,7 으로 증가하는 수열이기 때문에 별 개수는 2n-1개
    return cntstar

def count_space(n):  #n층에 왼쪽 공백 개수 세는 함수
    cntspace=0
    cntspace=((2*totno-1)-(count_star(n)))//2  #공백 개수는 (마지막 층수의 별 개수)-(현재 층수 별 개수)을 해주면 공백 개수가 나오는데
    return cntspace                            #공백 수는 좌우 같으므로 2로 나눠주면 한쪽 공백 개수만 구할 수 있다

def star_tri(n):
    global totno
    totno=n
    i = 0
    while i < n:   #총 층수(n)까지 별 삼각형 찍는 while문
        i += 1
        print(f'{"*" * (2 * i - 1):^{(2*n-1)}}') #별 개수를 2n-1씩 증가하게 출력해주고 총 자리수는 마지막층 별 개수로 가운데정렬

star_tri(100)  #총 층수 100까지 별 삼각형
print('50층에서 별 개수 :',count_star(50))
print('50층에 왼쪽 공백 개수 :',count_space(50))









# Q4)1.   은행 잔고, 입금액, 출금액, 이자액을 기반한 현재 잔액 조회를 위한 사용자 정의 함수 제작
# 2.    사용자 정의함수(외부함수) 1개와 내부함수 2개만 정의
# 3.    현 은행 잔고, 입금액, 출금액을 기반하여 잔고 업데이트를 위한 내부함수 1개 포함
# 4.    업데이트된 현 잔고를 기반한 이자액 계산 내부함수 1개 포함
# 5.    현 은행 잔고: 200원, 입금액: 50원, 출금액: 190원
# 6.    이자율은 월 0.13%, 이자액은 소수점 2자리까지 표기  # 0.13% 은 곱할때 0.0013


def x(balance,deposit,withdraw,d) :
    bal = balance
    depo = deposit
    wit = withdraw
    def get() :
        update = bal+depo-wit             # 업데이트된 현 잔고
        return update
    def tot(update) :                      # 이자율 월 0.13%
        total = update*d
        return total
    return get, tot
get,tot = x(200,50,190,0.0013)

update=get()
r=update*0.0013

print("업데이트된 잔고 :", get() ,"원" )
print("이자액 :", round(r,2) )

# <출력>
# 업데이트된 잔고 : 60 원
# 이자액 : 0.08





