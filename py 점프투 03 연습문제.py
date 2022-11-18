
# 1) 다음코드의 결괏값

#a = "Life is too short, you need python"

#if "wife" in a: print("wife")
#elif "python" in a and "you" not in a: print("python")
#elif "shirt" not in a: print("shirt")
#elif "need" in a: print("need")
#else: print("none")

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")



#>> 다음코드의 결괏값 : shirt





# 2) while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

a=1
tot=0

while  a < 1001 :
    a+=1
    if a%3==0 :
       tot+=a

print(tot)
#<출력> 166833





# 3) while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
#
# *
# **
# ***
# ****
# *****


a = 0
while True:
    a += 1
    if a > 5 :
        break
    print('*' * a)
# *
# **
# ***
# ****
# *****





# 3-1) while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
#
#      *
#     **
#    ***
#   ****
#  *****

a = 0
while True:
    a += 1
    if a > 5 :
        break
    print("{0:>5}".format("*" * a))
#      *
#     **
#    ***
#   ****
#  *****


# 3-2) while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
#
#  *****
#   ****
#    ***
#     **
#      *

a = 6
while True:
    a -= 1
    if  a < -1   :
        break
    print("{0:>5}".format("*" * a))
#  *****
#   ****
#    ***
#     **
#      *

#3-3) while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
#
#   *
#  ***
# *****
#*******


#가운데정렬★ 틀

cnt = -1
tot = 0
while cnt <11 :
    cnt += 2
    tot = '*'*cnt
    print(f'{tot:^11}')
#      *
#     ***
#    *****
#   *******
#  *********
# ***********



# 4) for문을 사용해 1부터 100까지의 숫자를 출력해 보자


for a in range(1,101) :
    print(a)





# 5)
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.


#평균 = 전체 합계 / 갯수

lst = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
tot = 0          #전체합계
b=len(lst)

for a in lst :   # lst a
    tot += a     #전체 합계
print("A학급의 평균 점수 :",tot / b)
# <출력> A학급의 평균 점수 : 79.0








# 6) 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
#
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

# 홀수에만 2를 곱하여 저장하는코드
numbers = [1, 2, 3, 4, 5]
result = []

for n in numbers :
    if n % 2 == 1:
        result.append(n*2)
print(result)

# 홀수에만 2를 곱하여 저장 /
# list comprehension 사용 ; 리스트 명 = [표현식 for 변수 in 반복 가능한 대상]
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1 ]  # 표현식 n*2  / 홀수 = 반복할대상
print(result)
# <출력> [2, 6, 10]
















#