

#_____________________________________________________________ loop

numdata = []

while True :
    num=int(input("숫자입력:"))

    if num % 10 == 0 :
        print("프로그램종료")
        break
    else :
        print(num)
        numdata.append(num)


#_______________________________________________________________ random

## random module
import random
help(random)


# module 함수의 도움말
help(random.random)   #random() method of random.Random instance
                       #random() -> x in the interval [0, 1).



# 0~1 사이의 난수
r=random.random()
print('r=',r)


#ex 난수 0.01 미만이면 종료 후 난수 개수 출력

num=0
while True :
    r=random.random()
    print(random.random())
    if r<0.01 :
        break
    else :
        num+=1
    print('난수갯수=', num)



#이름 list에 전체이름, 특정이름 출력

names=['james','jeny','dan']
print(names)     # <출력> ['james', 'jeny', 'dan']
print(names[2])  # <출력> dan


#__list안에 유무확인하기

names=['james','jeny','dan']

if 'jeny' in names :
    print("jeny in here")
else :
    print ("jeny not here")


#___난수 정수로 이름 선택하기 ★★

idx = random.randint(0,2)
print(names[idx])




################ 8/31 for문 .

#______________________________________________________________ for

# for 반복문
# 문자 열거형
str = "tom"
print (len(str))
for b in str :
    print(b)
#<출력>
#t
#o
#m

# list 열거형
lst=[1,2,3,4,5]
for a in str :
    print("영어 : ",a)

#<출력>
#영어 :  t
#영어 :  o
#영어 :  m


#__________________________________________________________________ range

range(10)      #0에서부터 9까지
range(1,10)    #1에서부터 9까지
range(1,10,3)  #1에서 9까지 3간격

#>>객체활용
for a in range(10) :
    print(a)  #>>>0,1,2,3,4,5,6,7,8,9

for b in range(1,10) :
    print(b)   #>>> 1,2,3,4,5,6,7,8,9

for c in range(1,10,3) :
    print(c) #>> 1,4,7


# list 자료 저장

import random
lst=[]

for a in range(1,10) :
    r = random.randint(1,10)
    lst.append(r)

print('lst:',lst)
# <출력> lst: [10, 5, 3, 2, 2, 9, 6, 4, 6]

# 자료 참조

import random
lst=[]

for b in range(2.10) :
    r = random.randint(2, 10)
    lst.append(r)
print(lst[b])



#___________________________________________________________________중첩반복문

#구구단

for a in range(2,10):
    print("{}단".format(a))
    for b in range(1,10) :
        print(a,b,a*b)































