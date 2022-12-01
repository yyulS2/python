# 신유라





# 문1)

import os
os.getcwd()

file = open("ch8_data/data/ftest.txt", mode ='r')
lines = file.readlines()
docs = []
words = []

for a in lines:
    docs.append(a.strip())
    for word in a.split():
        words.append(word)
print('문장내용')
print(docs)
print('문단수 :',len(docs))
print('단어내용')
print(words)
print('단어 수 :',len(words))

#<출력>
# 문장내용 ['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer is input output system']
# 문단수 : 6
# 단어내용 ['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer', 'is', 'input', 'output', 'system']
# 단어 수 : 22


# 문2)

import pandas as pd
from statistics import mean
import os
os.getcwd()
emp = pd.read_csv('ch8_data/data/emp.csv',encoding='utf-8')
#print(emp.info())
#print(emp.head())

name = emp.Name
pay = emp.Pay
print('관측지 길이 :',len(emp))
print('전체 평균 급여 :',format(mean(pay),".1f"))        # 소수점 0 format

max_pay = max(pay)
min_pay = min(pay)

for a in range(len(pay)):
    if  pay[a] == max_pay :
        print('최고 급여 :', max_pay,',','이름 :', name[a])
    if pay[a] == min_pay :
        print('최저 급여 :', min_pay,',','이름 :', name[a])

# <출력>
# 관측지 길이 : 5
# 전체 평균 급여 : 370.0
# 최저 급여 : 150 , 이름 : 홍길동
# 최고 급여 : 500 , 이름 : 강감찬


import pandas
from statistics import mean
import os
os.getcwd()
emp = pandas.read_csv('ch8_data/data/emp.csv', encoding='utf-8')
no = emp.No
name = emp.Name
pay = emp.Pay
print("관측치 길이 :",len(emp))
print("전체 평균 급여 : %.1f"%(mean(pay)))

for j,p in enumerate(pay):
    if p == min(pay):
        print(f"최저 급여 : {p} 이름 : {name[j]}")
    elif p == max(pay):
        print(f"최고 급여 : {p} 이름 : {name[j]}")