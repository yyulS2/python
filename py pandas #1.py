

import pandas as pd
import numpy as np

#Series, DataFrame 를 로컬 네임스페이스로 import
from pandas import Series, DataFrame

# 설정
import numpy as np
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.set_printoptions(precision=4, suppress=True)
pd.options.display.max_rows = PREVIOUS_MAX_ROWS


# 다중인덱스 사용가능

# 설정안해서 자동적으로 설정됨
# 왼쪽에 있는건 인덱스번호
obj = pd.Series([4,7,-8,3])
obj

# <출력>
# 0    4
# 1    7
# 2   -8
# 3    3
# dtype: int64


# 설정하면
obj2 = pd.Series([4,7,-8,3], index = ['d','b','a','c'])

obj2
# <출력>
# d    4
# b    7
# a   -8
# c    3
# dtype: int64

obj2.index
# <출력> Index(['d', 'b', 'a', 'c'], dtype='object')

# 색인으로 라벨 사용가능
# <obj2>
# d    4
# b    7
# a   -8
# c    3

obj2['a']
# <출력> -8


obj2['d'] = 6          # d를 6으로 변경
obj2[['c','a','d']]    # c,a,d 에 해당하는 데이터 값만 볼 수 있음
# <출력>
# c    3
# a   -8
# d    6
# dtype: int64

# 리스트로 묶어줘야함!!!
obj2['c','a','d']
# <출력> KeyError: 'key of type tuple not found and not a MultiIndex'


# 각각의 요소에 *2
obj2*2
# <출력>
# d    12
# b    14
# a   -16
# c     6
# dtype: int64


# 객체 안에 요소가 있는지 확인
'b' in obj2    # <출력> True
'e' in obj2    # <출력> False

# dic의 key 값이 인덱스 역할
sdata = {'ohio':35000,'texas':71000, 'oregon':16000, 'utah':5000}
obj3 = pd.Series(sdata)
obj3
# <출력>
# ohio      35000
# texas     71000
# oregon    16000
# utah       5000
# dtype: int64




# <obj3>
# ohio      35000
# texas     71000
# oregon    16000
# utah       5000

states = ['california','ohio','oregon','texas']
obj4 = pd.Series(sdata, index=states)            #states 의 인덱스를 사용하겠다

obj4
# <출력>
# obj4
# california        NaN
# ohio          35000.0
# oregon        16000.0
# texas         71000.0

# 'utah'는 states 에 포함되어 있지 않으므로 실행 결과에서 빠짐

# isnull notnull 누락된 데이터 찾기
pd.isnull(obj4)
# <출력>
# california     True
# ohio          False
# oregon        False
# texas         False
# dtype: bool

pd.notnull(obj4)
# <출력>
# california    False
# ohio           True
# oregon         True
# texas          True
# dtype: bool

obj4.isnull()
# <출력>
# california     True
# ohio          False
# oregon        False
# texas         False
# dtype: bool

obj3
# <출력>
# ohio      35000
# texas     71000
# oregon    16000
# utah       5000
# dtype: int64

obj4
# <출력>
# california        NaN
# ohio          35000.0
# oregon        16000.0
# texas         71000.0
# dtype: float64

obj3 + obj4
# <출력>
# california         NaN
# ohio           70000.0
# oregon         32000.0
# texas         142000.0
# utah               NaN
# dtype: float64



# 데이터의 컬럼명,인덱스명 설정
obj4.name = 'population'
obj4.index.name = 'state'

obj4
# <출력>
# state
# california        NaN
# ohio          35000.0
# oregon        16000.0
# texas         71000.0
# Name: population, dtype: float64


# 인덱스 색인을 대입하여 변경가능


# <obj>
# 0    4
# 1    7
# 2   -8
# 3    3

obj.index = ['Bob','Steve','Jeff','Ryan']
obj
# <출력>
# Bob      4
# Steve    7
# Jeff    -8
# Ryan     3
# dtype: int64

#새로운 데이터 들어오면 덮어씌어짐
obj.index = ['B','S','J','R']
obj
# <출력>
# B    4
# S    7
# J   -8
# R    3
# dtype: int64




# DataFrame                                                    DataFrame
# 로우 컬럼에 대한 인덱스를 가짐
# 기본적으로 2차원
# 계층적 색인 == 색인이 여러개이다 라는 뜻


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002, 2003],'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

# head 메서드 => 처음 5개의 로우만 출력함
frame.head()
# <출력>
#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2002  2.9

# 컬럼명 설정
pd.DataFrame(data, columns=['year','stat','pop'])
# <출력>
#    year stat  pop
# 0  2000  NaN  1.5
# 1  2001  NaN  1.7
# 2  2002  NaN  3.6
# 3  2001  NaN  2.4
# 4  2002  NaN  2.9
# 5  2003  NaN  3.2

# 없는 값인 debt에  => NaN 입력됨
frame2 = pd.DataFrame(data, columns = ['year','state','pop','debt'],index=['one','two','three','four','five','six'])

frame2
# <출력>
#        year   state  pop debt
# one    2000    Ohio  1.5  NaN
# two    2001    Ohio  1.7  NaN
# three  2002    Ohio  3.6  NaN
# four   2001  Nevada  2.4  NaN
# five   2002  Nevada  2.9  NaN
# six    2003  Nevada  3.2  NaN

frame2.columns
# <출력> Index(['year', 'state', 'pop', 'debt'], dtype='object')


frame2['state']
# <출력>
# one        Ohio
# two        Ohio
# three      Ohio
# four     Nevada
# five     Nevada
# six      Nevada
# Name: state, dtype: object

frame2.year
# <출력>
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# six      2003
# Name: year, dtype: int64

# 인덱스 three에 해당하는 값을 출력
frame2.loc['three']
# <출력>
# year     2002
# state    Ohio
# pop       3.6
# debt      NaN
# Name: three, dtype: object


# 컬럼명에 데이터 넣으면 컬럼명이 전부다 바뀜
# <frame2>
#        year   state  pop debt
# one    2000    Ohio  1.5  NaN
# two    2001    Ohio  1.7  NaN
# three  2002    Ohio  3.6  NaN
# four   2001  Nevada  2.4  NaN
# five   2002  Nevada  2.9  NaN
# six    2003  Nevada  3.2  NaN

frame2['debt'] = 16.5
frame2
# <출력>
#        year   state  pop  debt
# one    2000    Ohio  1.5  16.5
# two    2001    Ohio  1.7  16.5
# three  2002    Ohio  3.6  16.5
# four   2001  Nevada  2.4  16.5
# five   2002  Nevada  2.9  16.5
# six    2003  Nevada  3.2  16.5

# 컬럼명에 순차적데이터 넣기 => 컬럼에 0부터 5까지 들어감
# <frame2>
#        year   state  pop debt
# one    2000    Ohio  1.5  NaN
# two    2001    Ohio  1.7  NaN
# three  2002    Ohio  3.6  NaN
# four   2001  Nevada  2.4  NaN
# five   2002  Nevada  2.9  NaN
# six    2003  Nevada  3.2  NaN

frame2['debt']=np.arange(6.)
frame2
# <출력>
#        year   state  pop  debt
# one    2000    Ohio  1.5   0.0
# two    2001    Ohio  1.7   1.0
# three  2002    Ohio  3.6   2.0
# four   2001  Nevada  2.4   3.0
# five   2002  Nevada  2.9   4.0
# six    2003  Nevada  3.2   5.0

# 존재하지 않는 색인에 Nan 입력됨
val = pd.Series([-1.2,-1.5,-1.7], index=['two','four','five'])
frame2['debt'] = val
frame2
# <출력>
#        year   state  pop  debt
# one    2000    Ohio  1.5   NaN
# two    2001    Ohio  1.7  -1.2
# three  2002    Ohio  3.6   NaN
# four   2001  Nevada  2.4  -1.5
# five   2002  Nevada  2.9  -1.7
# six    2003  Nevada  3.2   NaN


# 새로운 컬럼명 값에 true false 값을 입력받기
# <frame2>
#        year   state  pop  debt
# one    2000    Ohio  1.5   NaN
# two    2001    Ohio  1.7  -1.2
# three  2002    Ohio  3.6   NaN
# four   2001  Nevada  2.4  -1.5
# five   2002  Nevada  2.9  -1.7
# six    2003  Nevada  3.2   NaN

frame2['eastern']=frame2.state == 'Ohio'
frame2
# <출력>
#        year   state  pop  debt  eastern
# one    2000    Ohio  1.5   NaN     True
# two    2001    Ohio  1.7  -1.2     True
# three  2002    Ohio  3.6   NaN     True
# four   2001  Nevada  2.4  -1.5    False
# five   2002  Nevada  2.9  -1.7    False
# six    2003  Nevada  3.2   NaN    False

# 컬럼삭제 ; del
del frame2['eastern']
frame2.columns
# <출력> Index(['year', 'state', 'pop', 'debt'], dtype='object')



# 딕트 형태에서 컬럼명 이름 지정함

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}


# 바깥키 = 컬럼, 안쪽키 = row
frame3 = pd.DataFrame(pop)
frame3
# <출력>
#       Nevada  Ohio
# 2001     2.4   1.7
# 2002     2.9   3.6
# 2000     NaN   1.5

# 데이터 행,렬 바꾸기
frame3.T
# <출력>
#         2001  2002  2000
# Nevada   2.4   2.9   NaN
# Ohio     1.7   3.6   1.5

# 색인 직접 지정
#frame3 = pd.DataFrame(pop)
#frame3
# <frame3>
#       Nevada  Ohio
# 2001     2.4   1.7
# 2002     2.9   3.6
# 2000     NaN   1.5

pd.DataFrame(pop,index=[2001,2002,2003])
# <출력>
#       Nevada  Ohio
# 2001     2.4   1.7
# 2002     2.9   3.6
# 2003     NaN   NaN

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
pd.DataFrame(pdata)
# <출력>
#       Ohio  Nevada
# 2001   1.7     2.4
# 2002   3.6     2.9



# 판다스 세미콜론 (;) => 코드와 코드를 줄단위말고 한줄에 작성하고싶을때 사용
frame3.index.name = 'year'; frame3.columns.name = 'state'
frame3
# <출력>
# state  Nevada  Ohio
# year
# 2001      2.4   1.7
# 2002      2.9   3.6
# 2000      NaN   1.5


frame3.values
# <출력>
# array([[2.4, 1.7],
#        [2.9, 3.6],
#        [nan, 1.5]])

frame2.values
# <출력>
# array([[2000, 'Ohio', 1.5, nan],
#        [2001, 'Ohio', 1.7, -1.2],
#        [2002, 'Ohio', 3.6, nan],
#        [2001, 'Nevada', 2.4, -1.5],
#        [2002, 'Nevada', 2.9, -1.7],
#        [2003, 'Nevada', 3.2, nan]], dtype=object)


import pandas as pd
import numpy as np



# index                                                   index

obj = pd.Series(range(3),index=['a','b','c'])
index = obj.index

index
# <출력> Index(['a', 'b', 'c'], dtype='object')
index[1:]
# <출력> Index(['b', 'c'], dtype='object')

# index안의 index변경은 불가
index[1] = 'd'
# <출력>
# TypeError: Index does not support mutable operationserror


# 인덱스 컬럼명을 범위값으로 지정하고 index가 있는지확인 is & in
labels = pd.Index(np.arange(3))
labels
# <출력> Int64Index([0, 1, 2], dtype='int64')

obj2 = pd.Series([1.5,-2.5,0], index = labels)
obj2
# <출력>
# 0    1.5
# 1   -2.5
# 2    0.0
# dtype: float64

obj2.index is labels
# <출력> True



frame3
# <출력>
# state  Nevada  Ohio
# year
# 2001      2.4   1.7
# 2002      2.9   3.6
# 2000      NaN   1.5

frame3.columns
# <출력>
# Index(['Nevada', 'Ohio'], dtype='object', name='state')

'Ohio' in frame3.columns
# <출력> True

2003 in frame3.index
# <출력> False


# 판다스 index 중복값 허용
dup_labels = pd.index(['foo','foo','bar','bar'])
dup_labels
# <출력> index(['foo','foo','bar','bar']),dtype='object'

# reindex ;  새로운 index 추가
obj = pd.Series([4.5,7.0,-5.3,3.6], index = ['d','b','a','c'])
obj
# <출력>
# d    4.5
# b    7.0
# a   -5.3
# c    3.6
# dtype: float64

# 색인값을 새로 추가 했을때 값이 없으면 NaN
obj2 = obj.reindex(['a','b','c','d','e'])
obj2
# <출력>
# a   -5.3
# b    7.0
# c    3.6
# d    4.5
# e    NaN
# dtype: float64

obj3 = pd.Series(['blue','purple','yellow'], index = [0,2,4])
obj3
# <출력>
# 0      blue
# 2    purple
# 4    yellow
# dtype: object

obj3.reindex(range(6),method = 'ffill')
# <출력>
# 0      blue
# 1      blue
# 2    purple
# 3    purple
# 4    yellow
# 5    yellow
# dtype: object

# reindex 컬럼도 변경 가능
frame = pd.DataFrame(np.arange(9).reshape((3,3)),
                     index = ['a','c','d'],columns=['Ohio', 'Texas', 'California'])
frame
# <출력>
#    Ohio  Texas  California
# a     0      1           2
# c     3      4           5
# d     6      7           8

frame2 = frame.reindex(['a','b','c','d'])
frame2
# <출력>
#    Ohio  Texas  California
# a   0.0    1.0         2.0
# b   NaN    NaN         NaN
# c   3.0    4.0         5.0
# d   6.0    7.0         8.0


states = ['Texas','Utah','California']
frame.reindex(columns=states)
# <출력>
#    Texas  Utah  California
# a      1   NaN           2
# c      4   NaN           5
# d      7   NaN           8

#추가한건 사용이 안됨 => error
frame.loc[['a','c','d'],states]
# <출력> KeyError: "['Utah'] not in index"


# 맞는것. 재 색인 하고 .loc 해야함
states2 = ['Texas','California','Ohio']
frame2.loc[['a','d','c'],states2]
# <출력>
#    Texas  California  Ohio
# a    1.0         2.0   0.0
# d    7.0         8.0   6.0
# c    4.0         5.0   3.0


# drop                                                  drop

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])

obj
# <출력>
# a    0.0
# b    1.0
# c    2.0
# d    3.0
# e    4.0
# dtype: float64

new_obj = obj.drop('c')
new_obj
# <출력>
# a    0.0
# b    1.0
# d    3.0
# e    4.0
# dtype: float64

obj.drop(['d', 'c'])
# <출력>
# a    0.0
# b    1.0
# e    4.0
# dtype: float64



data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index =['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])

data
# <출력>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15


#<data>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15


data.drop(['Colorado','Ohio'])
# <출력>
#           one  two  three  four
# Utah        8    9     10    11
# New York   12   13     14    15
# 인덱스 로우값 삭제 ; drop



# 인덱스 컬럼 값 삭제 ; drop
#<data>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15


data.drop('two',axis = 1)
# <출력>
#           one  three  four
# Ohio        0      2     3
# Colorado    4      6     7
# Utah        8     10    11
# New York   12     14    15


data.drop(['two','four'],axis = 'columns')
# <출력>
#           one  three
# Ohio        0      2
# Colorado    4      6
# Utah        8     10
# New York   12     14
# axi = 1 == axis = 'colums



# 버려지는,없는값 삭제  ; inplace=True

# <obj>
# a    0.0
# b    1.0
# c    2.0
# d    3.0
# e    4.0

obj.drop('c',inplace=True)
obj
# <출력>
# a    0.0
# b    1.0
# d    3.0
# e    4.0
# dtype: float64



# indexing                                              indexing
# numpy 는 정수여야만 했지만 판다스는 정수외에 실수도 사용가능
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj
# <출력>
# a    0.0
# b    1.0
# c    2.0
# d    3.0
# dtype: float64

obj['b']
# <출력> 1.0

obj[1]
# <출력> 1.0

obj[2:4]
# <출력>
# c    2.0
# d    3.0
# dtype: float64

obj[['b', 'a', 'd']]
# <출력>
# b    1.0
# a    0.0
# d    3.0
# dtype: float64

obj[[1, 3]]
# <출력>
# b    1.0
# d    3.0
# dtype: float64

obj[obj < 2]
# <출력>
# a    0.0
# b    1.0
# dtype: float64

obj['b':'c']
# <출력>
# b    1.0
# c    2.0
# dtype: float64

obj['b':'c'] =5   # b,c 값을 5로 대체하라
obj
# <출력>
# a    0.0
# b    5.0
# c    5.0
# d    3.0
# dtype: float64



# 하나 이상의 컬럼값 가져오기
data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index =['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])

data
# <출력>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

data['two']
# <출력>
# Ohio         1
# Colorado     5
# Utah         9
# New York    13
# Name: two, dtype: int32



data['three','one']
# <출력> KeyError: ('three', 'one')
data[['three','one']]
# <출력>
# three  one
# Ohio          2    0
# Colorado      6    4
# Utah         10    8
# New York     14   12


# 슬라이싱, 불리언 배열로 로우 선택가능

# <data>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15
data[:2]
# <출력>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# 로우 선택
data[data['three']>5]
# <출력>
#           one  two  three  four
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

# true false 값 추출하기
data<5
# <출력>
#             one    two  three   four
# Ohio       True   True   True   True
# Colorado   True  False  False  False
# Utah      False  False  False  False
# New York  False  False  False  False

# 데이터 값이 5이하인 데이터는 0으로 대체
data[data<5]=0
data
# <출력>
#           one  two  three  four
# Ohio        0    0      0     0
# Colorado    0    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15



#
# <data>
#           one  two  three  four
# Ohio        0    0      0     0
# Colorado    0    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

data.loc['Colorado',['two','three']]
# <출력>
# two      5
# three    6
# Name: Colorado, dtype: int32

data.iloc[2,[3,0,1]]
# <출력>
# four    11
# one      8
# two      9
# Name: Utah, dtype: int32

data.iloc[2]
# <출력>
# one       8
# two       9
# three    10
# four     11
# Name: Utah, dtype: int32

data.iloc[[1,2],[3,0,1]]
# <출력>
#           four  one  two
# Colorado     7    0    5
# Utah        11    8    9



# 문자쓸땐 문자까지 포함/ 숫자쓰면 숫자 전까지
data
#utah까지
data.loc[:'Utah','two']
# <출력>
# Ohio        0
# Colorado    5
# Utah        9
# Name: two, dtype: int32

data.iloc[:,:3][data.three >5]
# <출력>
#           one  two  three
# Colorado    0    5      6
# Utah        8    9     10
# New York   12   13     14
# 0부터2 까지, three가 5이상인 애들 ; data.three!!!




# ser                                                                               ser


ser = pd.Series(np.arange(3.))
ser
# <출력>
# 0    0.0
# 1    1.0
# 2    2.0
# dtype: float64

# 정수 기반의 색인을 사용하지 않는 경우 이런 모호함은 사라짐.
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]
# <출력> 2.0


# 일관성 유지를 위해 정수값을 담고 있는 축 색인이 있다면 우선적으로 라벨을 먼저 찾아보도록 구현되어 있음.
# 라벨 컬럼 => loc 을 사용 / 정수 색인 row =>iloc 을 사용
ser[:1]
# <출력>
# 0    0.0
# dtype: float64

ser.loc[:1]
# <출력>
# 0    0.0
# 1    1.0
# dtype: float64

ser.iloc[:1]
# <출력>
# 0    0.0
# dtype: float64



# 다른 색인을 가지고 있는 객체간의 연산이 가능하다
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

s1
# <출력>
# a    7.3
# c   -2.5
# d    3.4
# e    1.5
# dtype: float64

s2
# <출력>
# a   -2.1
# c    3.6
# e   -1.5
# f    4.0
# g    3.1
# dtype: float64


# 서로 겹치는 색인이 없는 경우 데이터는 NA 값
s1 + s2
# <출력>
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# g    NaN
# dtype: float64



# DataFrame 의 경우 정렬은 로우와 컬럼 모두에 적용됨.
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)),
                   columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                   columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

df1
# <출력>
#             b    c    d
# Ohio      0.0  1.0  2.0
# Texas     3.0  4.0  5.0
# Colorado  6.0  7.0  8.0

df2
# <출력>
#           b     d     e
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0

df1 + df2
# <출력>
#             b   c     d   e
# Colorado  NaN NaN   NaN NaN
# Ohio      3.0 NaN   6.0 NaN
# Oregon    NaN NaN   NaN NaN
# Texas     9.0 NaN  12.0 NaN
# Utah      NaN NaN   NaN NaN


# 공통되는 컬럼 로우 없는 DataFrame 는 결과에 아무것도 안 나타남.
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})

df1
# <출력>
#    A
# 0  1
# 1  2

df2
# <출력>
#    B
# 0  3
# 1  4

df1 - df2
# <출력>
#     A   B
# 0 NaN NaN
# 1 NaN NaN




# 서로 다른 색인을 가지는 객체 간의 산술연산에서 존재하지 않는 축의 값을 특수한 값(예, 0)으로지정 시
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
df2.loc[1, 'b'] = np.nan

df1
# <출력>
#      a    b     c     d
# 0  0.0  1.0   2.0   3.0
# 1  4.0  5.0   6.0   7.0
# 2  8.0  9.0  10.0  11.0

df2
# <출력>
#       a     b     c     d     e
# 0   0.0   1.0   2.0   3.0   4.0
# 1   5.0   NaN   7.0   8.0   9.0
# 2  10.0  11.0  12.0  13.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0

df1+df2
# <출력>
#       a     b     c     d   e
# 0   0.0   2.0   4.0   6.0 NaN
# 1   9.0   NaN  13.0  15.0 NaN
# 2  18.0  20.0  22.0  24.0 NaN
# 3   NaN   NaN   NaN   NaN NaN

df1.add(df2, fill_value = 0)
# <출력>
#       a     b     c     d     e
# 0   0.0   2.0   4.0   6.0   4.0
# 1   9.0   5.0  13.0  15.0   9.0
# 2  18.0  20.0  22.0  24.0  14.0
# 3  15.0  16.0  17.0  18.0  19.0

# df1을 1로 나눈다
1/df1
df1.rdiv(1)
# <출력>
#        a         b         c         d
# 0    inf  1.000000  0.500000  0.333333
# 1  0.250  0.200000  0.166667  0.142857
# 2  0.125  0.111111  0.100000  0.090909

# 재색인
df1.reindex(columns=df2.columns,fill_value=0)
# <출력>
#      a    b     c     d  e
# 0  0.0  1.0   2.0   3.0  0
# 1  4.0  5.0   6.0   7.0  0
# 2  8.0  9.0  10.0  11.0  0



# arr                              arr
arr = np.arange(12.).reshape((3,4))

arr
# <출력>
# array([[ 0.,  1.,  2.,  3.],
#        [ 4.,  5.,  6.,  7.],
#        [ 8.,  9., 10., 11.]])
arr[0]
# <출력>
# array([0., 1., 2., 3.])

arr-arr[0]
# <출력>
# array([[0., 0., 0., 0.],
#        [4., 4., 4., 4.],
#        [8., 8., 8., 8.]])

frame = pd.DataFrame(np.arange(12.).reshape((4,3)),
                     columns=list('bda'), index=['Utah','Ohio','Texas','Oregon'])
series = frame.iloc[0]
frame
# <출력>
#           b     d     a
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0

series
# <출력>
# b    0.0
# d    1.0
# a    2.0
# Name: Utah, dtype: float64


# frame series 산술연산
frame-series
# <출력>
#           b    d    a
# Utah    0.0  0.0  0.0
# Ohio    3.0  3.0  3.0
# Texas   6.0  6.0  6.0
# Oregon  9.0  9.0  9.0




#객체는 형식을 맞추기 위해 재색인된다.
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
series2
# <출력>
# b    0
# e    1
# f    2
# dtype: int64

# <frame>
#           b     d     a
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0
frame + series2
# <출력>
#          a    b   d   e   f
# Utah   NaN  0.0 NaN NaN NaN
# Ohio   NaN  3.0 NaN NaN NaN
# Texas  NaN  6.0 NaN NaN NaN
# Oregon NaN  9.0 NaN NaN NaN

series3 = frame['d']
frame
# <출력>
#           b     d     a
# Utah    0.0   1.0   2.0
# Ohio    3.0   4.0   5.0
# Texas   6.0   7.0   8.0
# Oregon  9.0  10.0  11.0

series3
# <출력>
# Utah       1.0
# Ohio       4.0
# Texas      7.0
# Oregon    10.0
# Name: d, dtype: float64

frame.sub(series3, axis = 'index')
# <출력>
#           b    d    a
# Utah   -1.0  0.0  1.0
# Ohio   -1.0  0.0  1.0
# Texas  -1.0  0.0  1.0
# Oregon -1.0  0.0  1.0













