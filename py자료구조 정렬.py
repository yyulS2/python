#

# 객제 주소 복사
## ______________________________________얕은 복사 : 주소 내용 동일 #주소 id()
name = ["a","b","c"]
print ('name address=',id(name))

name2 = name
print('name2 address=',id(name2))

# 주소동일
#name address= 2382027955072
#name2 address= 2382027955072

# 내용동일
print(name)  #>['a', 'b', 'c']
print(name2) #>['a', 'b', 'c']


###____________________________________얕은복사__원본수정
name2[0] = "d" #name2의 첫번째자리 a 를 d로 수정
print(name)    # <출력>['d', 'b', 'c']
print(name2)   # <출력>['d', 'b', 'c']



####________________________________________깊은복사 : 내용동일 주소다름
import copy                   #copy 모듈 넣어야함
name3 = copy.deepcopy(name)
# 내용동일
print(name)  #<출력>['d', 'b', 'c']
print(name3) #<출력>['d', 'b', 'c']

# 주소다름
print (id(name))
print (id(name3))
# name address ≠ name2 address



###___________________________________깊은복사__원본수정
name[1] = "f"
print(name)   #<출력> ['d', 'f', 'c']
print(name3)  #<출력> ['d', 'b', 'c']



가= [1, 2, 3]
나= 가[:]      ##리스트 전체를 가리키다 [:]
가[1] = 4
print(가)      #<출력> [1, 4, 3]
print(나)      #<출력> [1, 2, 3]




#                                         알고리즘 최댓값최솟값 vmax vmin

import random                #랜덤모듈
dataset =[]
for a in range(20) :         #a는 변수
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)               #랜덤이므로 결과는 계속바뀜

# 위의 결과에서 변수초기화먼저 >> 첫번째원소를 먼저 데려옴
vmax = vmin = dataset[0]
print(vmax)      # dataset의 첫번째원소
print(vmin)      # dataset의 첫번째원소

# 최댓값 최솟값
for a in dataset :
    if vmax < a :
        vmax = a
    if vmin > a :
        vmin = b

print ("vmax:",vmax ,"vmin:",vmin)  # #랜덤이므로 계속바뀜





#____________________________________________________정렬 sort


#선택정렬 ; 특정원소 기준으로(가장 작은 아이템의 위치를 변수에 먼저 저장) 나머지 원소를 비교해가면서 정렬함
#       ; 최솟값을 찾아서 맨 앞으로 이동하는 방식

# 선택정렬 오름차순
dataset = [1,3,2,6,7]
n = len(dataset)                     #원소개수   #n-1 비교대상은 list에서 맨마지막빼고 비교하면 되기때문에 -1 해줘야함
for i in range(n-1) :                #바깥반복문에서 기준변수 만들기 =i ;
    for j in range(i+1,n) :          #비교변수(j)는 기준변수(i)보다 +1칸위치에서 시작에서 n칸씩이동
        if dataset[i]>dataset[j] :   #기존변수보다 비교변수가 작으면 #비교변수 i+1칸 위치 인 3을 도출
            print(dataset)
            dataset[i], dataset[j] = dataset[j], dataset[i] #자리교환계속일어남
    print(dataset)

print("선택정렬 오름차순 결과 :",dataset)
# <출력> 선택정렬 오름차순 결과 : [1, 2, 3, 6, 7]



# 선택정렬 내림차순
dataset = [1,3,2,6,7]
n = len(dataset)
for c in range(n) :
    for d in range(c+1,n) :
        if dataset[c]<dataset[d] :
            print(dataset)
            dataset[c], dataset[d] = dataset[d], dataset[c]  #자리교환계속일어남
    print(dataset)
print("선택정렬 내림차순 결과 :",dataset)
# <출력> 선택정렬 내림차순 결과 : [7, 6, 3, 2, 1]




#버블정렬 ; 인접한 원소끼리 비교하여 교환하는 방식 바로오른쪽꺼 비교 이기 때문에 n-1-i
#버블정렬 오름차순
data = [5,8,1,4,9]
n=len(data)
for i in range(n) :
    for j in range(n-1-i) :
        if data[j] > data[j+1] :
          print(data)
          data[j],data[j+1] = data[j+1],data[j]   #자리교환계속일어남
print("버블정렬 오름차순 결과 :",data)
# <출력> 버블정렬 오름차순 결과 : [1, 4, 5, 8, 9]
# i(기준변수) 전체범위 회전   range n : data{list}의 선택반복문
# j(비교변수) = range(n-1-i) 에서 도출
# ex)첫번재로 ))  j의 첫번째수(data[1]=5)가 j의 두번째 수 (data[1+1=2]=8) 보다 크면 ...
# 자리교환계속일어남

dataset=[5,2,4,3,1]
l=len(dataset)
for i in range(l-1):
    for j in range(l-i-1):
      if dataset[j]>dataset[j+1]:
        print(dataset)
        dataset[j],dataset[j+1] =dataset[j+1],dataset[j]
print(dataset)



#버블정렬 내림차순
data = [5,8,1,4,9]
n=len(data)
for i in range(n) :                            #전체범위 회전 i(기준변수)
    for j in range(n-1-i) :
        if data[j] < data[j+1] :
          print(data)
          data[j],data[j+1] = data[j+1],data[j]
print("버블정렬 내림차순 결과 :", data)
# <출력> 버블정렬 내림차순 결과 : [9, 8, 5, 4, 1]

dataset=[3,5,7,8,11,42]
l=len(dataset)
for i in range(l-1):
    for j in range(l-i-1):
      if dataset[j]<dataset[j+1]:
        print(dataset)
        dataset[j],dataset[j+1] =dataset[j+1],dataset[j]
print(dataset)



#________________________________________검색(search)

#이진검색 알고리즘
#중앙값보다 값이 크면 오른쪽버림 end=mid-1
#중앙값보다 값이 작으면 왼쪽 버림 start=mid+1


data=[5,12,17,25,34,47,56]
value = int(input("검색할 값 입력:"))


low=0               # 1.start 위치 정하기
high=len(data)-1    # 2.end 위치 정하기
loc = 0             # mid 값을 찾으면 넣어줄것
state = False       # 3. 상태변수 정하기


while (low<=high) :               # 4. while문
    mid = (low+high)//2           # 5. 중앙값구하기
    if data[mid] > value :        # 6. 만약if) 중앙값이 입력한 값보다 클경우
       high=mid-1                 # > 오른쪽 버림
    elif data[mid] < value :      # 7. 만약if) 중앙값이 입력한 값보다 작을경우
        low=mid+1                 # > 왼쪽 버림
    else :                        # 8. 외) 값을 찾게 되면
        loc = mid                 # 9. mid 를 찾은값을 loc으로 색인해주기
        state = True              # 10. false -> true 상태로 바꾸기
        break                     # mid값 찾으면 종료 후 while문으로 나옴

if state :                        # 반복문에서 찾은 값이 있는경우
    print("찾은위치 : %d번째 " %(loc+1))
else :
    print ("찾는 값은 없습니다.")

    # "%d"사용하기 // %(loc+1)/// loc+1 이 리스트안에서 찾은 위치 자리수는 0부터 시작하므로






