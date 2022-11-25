# 내장클래스



#
lst = [1,3,5]
for i, c in enumerate(lst) :
    print('색인:',i, end=', ')
    print('내용:',c)

# <출력>
# 색인: 0, 내용: 1
# 색인: 1, 내용: 3
# 색인: 2, 내용: 5


dic = {'name':'jain','job':'teacher','age':'25'}
for i, k in enumerate(dit) :
    print('순서:',i, end=', ')
    print('키:',k, end=', ')
    print('값:',dic[k])
# <출력>
# 순서: 0, 키: name, 값: jain
# 순서: 1, 키: job, 값: teacher
# 순서: 2, 키: age, 값: 25


### import 내장클래스
import datetime
from datetime import date, time

# date 클래스

import datetime
from datetime import date, time

today = date (2022,9,6)
print(today)           # <출력> 2022-09-06
print(today.year)      # <출력> 2022
print(today.month)     # <출력> 9
print(today.day)       # <출력> 6

w=today.weekday()
print('요일정보 : ', w)  # <출력> 요일정보 :  1

# time 클래스
currtime = time(11,14,32)
print(currtime)             # <출력> 11:14:32
print(currtime.hour)        # <출력> 11
print(currtime.minute)      # <출력> 14
print(currtime.second)      # <출력> 32

isoTime=currtime.isoformat()
print(isoTime)              # <출력> 11:14:32




# # # 모듈 추가
# # 1. import 패키지명. 모듈명

import mypackage.scaterring
data = [1,3,5,4.5,2,1,2.3]

#산술평균 함수 호출
print('평균:', mypackage.scaterring.Avg(data))

#분산, 표준편차 호출
var,sd = mypackage.scaterring.var_sd(data)
print('분산:',var)          # <출력> 분산: 1.1497959183673467
print('표준편차:',sd)        # <출력> 표준편차: 1.072285371702583



# # 2. from 패키지명.모듈명 import 함수명

from mypackage.scaterring import Avg,var_sd

print('평균:',Avg(data))      # <출력> 평균: 2.6857142857142855

var,sd = var_sd(data)
print('분산:',var)            # <출력> 분산: 1.1497959183673467
print('표준편차',sd)           # <출력> 표준편차 1.072285371702583



# # # 시작점 만들기

# 시작점 있는경우

if __name__=='__main__' :
    data=[1,3,5,7]
    print('평균:',Avg(data))
    var,sd = var_sd(data)
    print('분산:',var)
    print('표준편차:',sd)

# <출력>
# 평균: 4
# 분산: 4.0
# 표준편차: 2.0



# 시작점 없는경우
data=[1,3,5,7]
print('평균:',Avg(data))
var,sd = var_sd(data)
print('분산:',var)
print('표준편차:',sd)

# <출력>
# 평균: 4
# 분산: 4.0
# 표준편차: 2.0















