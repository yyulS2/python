

#> 대용량 데이터 배열을 효율적으로 다룰 수 있도록 설계

import numpy as np
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)



# 100 만개의 정수를 저장하는 Numpy 배열과 파이썬 리스트 비교

import numpy as np
my_arr = np.arange(1000000)
my_list = list(range(1000000))

from datetime import datetime
start1 = datetime.now()
for _ in range(10): my_arr2 = my_arr * 2
print(datetime.now() - start1)

from datetime import datetime
start2 = datetime.now()
for _ in range(10): my_list2 = [x * 2 for x in my_list]
print(datetime.now() - start2)


# 0:00:00.031231
# 0:00:00.680139



# 배치 계산 처리 방법

import numpy as np

data = np.random.randn(2, 3)

data * 10
data + data
#array([[  3.86551394,  -4.01066326,  -7.30719639],
#       [ -2.7284584 , -10.72289149,  -6.51082055]])
data + data
#array([[ 0.77310279, -0.80213265, -1.46143928],
#       [-0.54569168, -2.1445783 , -1.30216411]])

# 각 차원의 크기를 알려주는 shape 이라는 튜플
data.shape                               # <출력> (2, 3)

# 배열에 저장된 자료형을 알려주는 dtype
data.dtype                               # <출력> dtype('float64')


# 배열을 생성방법 : array()함수를 이용
data1 = [6,7.5,8,0,1]
arr1=np.array(data1)
arr1

# <출력> array ([6. , 7.5, 8. , 0. , 1. ])


# 같은 길이를 가지는 리스트를 내포
data2 =[[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr2

# <arr2>
# array([[1, 2, 3, 4],
#       [5, 6, 7, 8]])

# 차원
arr2.ndim    # <출력> 2

# 차원
arr2.shape   # <출력> (2, 4)

# 전체 원소 수
arr2.size    # <출력> 8

# 첫번째 차원의 갯수
len(arr2)    # <출력> 2

arr1.dtype   # <출력> dtype('float64')
arr2.dtype   # <출력> dtype('int32')

np.zeros(10)
# <출력>
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])


np.zeros((3,6))
# <출력>
# array([[0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0.]])

np.zeros((2,3,2))
# <출력>
# array([[[0., 0.],
#         [0., 0.],
#         [0., 0.]],
#        [[0., 0.],
#         [0., 0.],
#         [0., 0.]]])


np.empty((2, 3, 2))
# <출력>
# array([[[4., 0.],
#         [4., 0.],
#         [4., 0.]],
#        [[4., 0.],
#         [4., 0.],
#         [4., 0.]]])


np.arange(15)
# <출력>
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])



# 8 바이트 또는 64 비트로 이루어지는데 NumPy 에서 float64 로 표현

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr1.dtype      # <출력> dtype('float64')
arr2.dtype      # <출력> dtype('int32')
arr1            # <출력> array([1., 2., 3.])
arr2            # <출력> array([1, 2, 3])




# astype 사용 > dtype 변환(캐스팅)
arr = np.array([1, 2, 3, 4, 5])
arr.dtype           # <출력> dtype('int32')

float_arr = arr.astype(np.float64)
float_arr.dtype     # <출력> dtype('float64')


# 부동소수점수 > 정수형 dtype변환 ; 소수점 아래 버림
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr                            # <출력> array([ 3.7, -1.2, -2.6,  0.5, 12.9, 10.1])
arr.astype(np.int32)           # <출력> array([ 3, -1, -2,  0, 12, 10])


# astype사용 > 숫자 형식의 문자열을 담고 있는 배열을 숫자로 변환
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)    # <출력> array([ 1.25, -9.6 , 42.  ])



# 다른 배열의 dtype 속성 이용
int_array = np.arange(10)
int_array
# <출력> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
calibers.dtype
# <출력> dtype('float64')

int_array.astype(calibers.dtype)
# <출력> array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])


# 축약코드 사용
empty_uint32 = np.empty(8, dtype='u4')       # 부호가 없는 32 비트 정수형
empty_uint32

# <출력> array([1, 0, 4, 0, 4, 0, 4, 0], dtype=uint32)


# * astype 을 호출하면 새로운 dtype 이 이전 dtype 과 동일해도
# 항상 새로운 배열을 생성(데이터를 복사)

# '벡터화' : 같은 크기의 배열 간의 산술 연산은 배열의 각 원소 단위로 적용
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr
# <출력>
# array([[1., 2., 3.],
#        [4., 5., 6.]])

arr * arr
# <출력>
# array([[ 1.,  4.,  9.],
#        [16., 25., 36.]])

arr - arr
# <출력>
# array([[0., 0., 0.],
#        [0., 0., 0.]])


# 스칼라 인자가 포함된 산술 연산의 경우 배열 내의 모든 원소에 스칼라 인자가 적용된다.
1 / arr
# <출력>
# array([[1.    , 0.5   , 0.3333],
#        [0.25  , 0.2   , 0.1667]])

arr ** 0.5
# <출력>
# array([[1.    , 1.4142, 1.7321],
#        [2.    , 2.2361, 2.4495]])


# 같은 크기를 가지는 배열 간의 비교 연산은 불리언 배열을 반환
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr2
# <출력>
# array([[ 0.,  4.,  1.],
#        [ 7.,  2., 12.]])

arr2 > arr
# <출력>
# array([[False,  True, False],
#        [ True, False,  True]])






