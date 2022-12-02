


#브로드캐스팅(broadcasting)                                                브로드캐스팅(broadcasting)



import numpy as np
arr = np.arange(10)

arr
# <출력> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[5]
# <출력> 5

arr[5:8]
# <출력> array([5, 6, 7])

arr[5:8] = 12                   # 5,6,7 자리에 12를 넣어라
arr
# <출력> array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])


#arr 슬라이스 생성
# <arr>
# array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])

arr_slice = arr [5:8]
arr_slice
# <출력> array([12, 12, 12])

# arr_slice 값 변경하면 원래 배열의 값도 바뀌어있음
arr_slice[1] = 123456
arr
# <출력>
# array([     0,      1,      2,      3,      4,     12, 123456,     12,       8,      9])

# [:] => 배열의 모든 값을 할당
arr_slice[:] = 64
arr
# <출력> array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])

# copy
arr[5:8].copy()
arr
# <출력> array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])

# 다차원 배열 ; 2차원배열(대괄호2개) -> 1차원배열
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2]
# <출력> array([7, 8, 9])

# 색인: 콤마로도 가능
arr2d[0][2]         # <출력> 3
arr2d[0,2]          # <출력> 3


# 3차원배열(대괄호3개)
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d
# <출력>
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],
#        [[ 7,  8,  9],
#         [10, 11, 12]]])

arr3d[0]
# <출력>
# array([[1, 2, 3],
#        [4, 5, 6]])



# copy 로 백업 하고 , 다시 원본으로 백업 시킬수있다
#copy 로 백업
old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d
# <출력>
# array([[[42, 42, 42],
#         [42, 42, 42]],
#        [[ 7,  8,  9],
#         [10, 11, 12]]])


#다시 원본으로 백업
arr3d = old_values
arr3d
# <출력>
# array([[1, 2, 3],
#        [4, 5, 6]])1



# 1차원 배열의 값 반환
arr3d[1,0]
# <출력> 4

x=arr3d[1]
x
# <출력> array([4, 5, 6])
x[0]
# <출력> 4

arr3d[1][0]
# <출력> 4


# 인덱싱 슬라이싱
arr
# <출력> array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
arr[1:6]
# <출력> array([ 1,  2,  3,  4, 64])

#2차원 슬라이싱
arr2d
# <출력>
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

arr2d[:2]            # 시작부터 두번째 로우까지의 선택
# <출력>
# array([[1, 2, 3],
#        [4, 5, 6]])


arr2d[:2,1:]
# <출력>
# array([[2, 3],
#        [5, 6]])

# 정수색인과 슬라이스 같이 사용 -> 한차원낮은 슬라이스 선택
# 두번째 low 에서 처음 두 컬럼만
arr2d[1,:2]
# <출력>
# array([4, 5])


# 처음 두 low 에서 세번째 컬럼만
arr2d[:2,2]
# <출력>
# array([3, 6])



# 콜론만 쓰면 low는 전부다
arr2d[:,:1]
# <출력>
# array([[1],
#        [4],
#        [7]])


# 슬라이싱 선택 영역에 값 대입가능
arr2d[:2,1:] =0
arr2d
# <출력>
# array([[1, 0, 0],
#        [4, 0, 0],
#        [7, 8, 9]])





# boolean 인덱싱                                                       boolean 인덱싱

import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4)   # 7x4 array
# randn 함수 이용 -> 표준정규분포 데이터 생성


names
# <출력> array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'], dtype='<U4')

data
# 7x4 랜덤array 생성

data [names=='BOb']
# true(조건에 맞는) 인 부분만 인덱스 결과 나옴
# index0, index3 에 해당



# '!=' == '~' 사용

names != 'Bob'
# <출력> array([False,  True,  True, False,  True,  True,  True])

data[~(names == 'Bob')]
# <출력> 랜덤array 생성


cond = names=='Bob'   # cond에 names=='Bob' 담기
data[~cond]
# <출력> 같은 값으로 출력 data[~cond] = data[~(names == 'Bob')]




# &(AND) 조건 과 |(OR)조건 => and 와 or 를 사용할 수 없고 & 과 | 을 사용
mask = (names == 'Bob') | (names == 'Will')
mask
# <출력> array([ True, False,  True,  True,  True, False, False])
data[mask]
# <출력> 랜덤array 생성



# data 에 저장된 모든 음수를 0 으로 대입
data[data < 0] = 0
data
# <출력> 랜덤array 중에서 "<0" 인 값만 0으로 처리되어 출력

# 1 차원 불리언 배열을 사용해서 전체 로우나 컬럼을 선택하는 것은 쉽게 할 수 있다.
data[names != 'Joe'] = 7
data
# <출력>


























