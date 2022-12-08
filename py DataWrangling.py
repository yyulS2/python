

import numpy as np
import pandas as pd
pd.options.display.max_rows = 20
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)



data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
data
# <출력>
# a  1   -0.204708
#    2    0.478943
#    3   -0.519439
# b  1   -0.555730
#    3    1.965781
# c  1    1.393406
#    2    0.092908
# d  2    0.281746
#    3    0.769023
# dtype: float64



data.index
# <출력>
# MultiIndex([('a', 1),
#             ('a', 2),
#             ('a', 3),
#             ('b', 1),
#             ('b', 3),
#             ('c', 1),
#             ('c', 2),
#             ('d', 2),
#             ('d', 3)],
#            )


data['b']
# <출력>
# 1   -0.555730
# 3    1.965781
# dtype: float64


data['b':'c']
# <출력>
# b  1   -0.555730
#    3    1.965781
# c  1    1.393406
#    2    0.092908
# dtype: float64


data.loc[['b','d']]
# <출력>
# b  1   -0.555730
#    3    1.965781
# d  2    0.281746
#    3    0.769023
# dtype: float64


data.loc[:,2]
# <출력>
# a    0.478943
# c    0.092908
# d    0.281746
# dtype: float64

# 첫번째 색인 상관없이

#########
data.unstack()
# <출력>
#           1         2         3
# a -0.204708  0.478943 -0.519439
# b -0.555730       NaN  1.965781
# c  1.393406  0.092908       NaN
# d       NaN  0.281746  0.769023

# unstack 의 반대 작업은 stack 메서드로 수행
data.unstack().stack()
# <출력>
# a  1   -0.204708
#    2    0.478943
#    3   -0.519439
# b  1   -0.555730
#    3    1.965781
# c  1    1.393406
#    2    0.092908
# d  2    0.281746
#    3    0.769023
# dtype: float64


# DataFrame 에서는 두 축 모두 계층적 색인을 가질 수 있다.
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame
# <출력>
#      Ohio     Colorado
#     Green Red    Green
# a 1     0   1        2
#   2     3   4        5
# b 1     6   7        8
#   2     9  10       11


frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame
# <출력>
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11

# 컬럼의 부분집합을 부분적인 색인으로 접근하는 것도 컬럼에 대한 부분적 색인과 비슷하게 사용 가능
frame['Ohio']
# <출력>
# color      Green  Red
# key1 key2
# a    1         0    1
#      2         3    4
# b    1         6    7
#      2         9   10

# MultiIndex 는 따로 생성한 다음에 재사용이 가능
MultiIndex = data.index
# <출력>

# 위에서 살펴본 DataFrame 의 컬럼 계층이름은 다음처럼 생성할 수 있다
MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])
# <출력>
# MultiIndex([(    'Ohio', 'Green'),
#             (    'Ohio',   'Red'),
#             ('Colorado', 'Green')],
#            names=['state', 'color'])






# swaplevel 은 넘겨받은 두 개의 계층 번호나 이름이 뒤바뀐 새로운 객체를 반환(데이터는 불변)
frame.swaplevel('key1', 'key2')
# <출력>
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
# 2    a        3   4        5
# 1    b        6   7        8
# 2    b        9  10       11

# level=1 은 위에서 바라보는것
frame.sort_index(level=1)
# <출력>
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
# b    1        6   7        8
# a    2        3   4        5
# b    2        9  10       11

# 왼쪽에서 오른쪽으로 바라보는것
frame.swaplevel(0, 1).sort_index(level=0)
# <출력>
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
#      b        6   7        8
# 2    a        3   4        5
#      b        9  10       11





## sum

frame.sum(level='key2')
# <출력>
# state  Ohio     Colorado
# color Green Red    Green
# key2
# 1         6   8       10
# 2        12  14       16

frame.sum(level='color', axis=1)
# <출력>
# color      Green  Red
# key1 key2
# a    1         2    1
#      2         8    4
# b    1        14    7
#      2        20   10

# index ##

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
frame
# <출력>
#    a  b    c  d
# 0  0  7  one  0
# 1  1  6  one  1
# 2  2  5  one  2
# 3  3  4  two  0
# 4  4  3  two  1
# 5  5  2  two  2
# 6  6  1  two  3

# DataFrame 의 set_index()함수는 하나 이상의 컬럼을 색인으로 하는 새로운 DataFrame 을 생성
frame2 = frame.set_index(['c', 'd'])
frame2
# <출력>
#        a  b
# c   d
# one 0  0  7
#     1  1  6
#     2  2  5
# two 0  3  4
#     1  4  3
#     2  5  2
#     3  6  1

# 컬럼을 명시적으로 남겨두지 않으면 DataFrame 에서 삭제된다.
frame.set_index(['c', 'd'], drop=False)
# <출력>
#        a  b    c  d
# c   d
# one 0  0  7  one  0
#     1  1  6  one  1
#     2  2  5  one  2
# two 0  3  4  two  0
#     1  4  3  two  1
#     2  5  2  two  2
#     3  6  1  two  3


# reset_index()함수는 set_index()와 반대되는 개념
# 계층적 색인 단계가 컬럼으로 이동
frame2.reset_index()
# <출력>
#      c  d  a  b
# 0  one  0  0  7
# 1  one  1  1  6
# 2  one  2  2  5
# 3  two  0  3  4
# 4  two  1  4  3
# 5  two  2  5  2
# 6  two  3  6  1



# combining ###
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df1
# <출력>
#   key  data1
# 0   b      0
# 1   b      1
# 2   a      2
# 3   c      3
# 4   a      4
# 5   a      5
# 6   b      6

df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
df2
# <출력>
#   key  data2
# 0   a      0
# 1   b      1
# 2   d      2

# merge()함수 사용
pd.merge(df1, df2)
# <출력>
#   key  data1  data2
# 0   b      0      1
# 1   b      1      1
# 2   b      6      1
# 3   a      2      0
# 4   a      4      0
# 5   a      5      0


# merge()함수는 중복된 컬럼을 키로 사용('key'컬럼)
pd.merge(df1, df2, on='key')
# <출력>
#   key  data1  data2
# 0   b      0      1
# 1   b      1      1
# 2   b      6      1
# 3   a      2      0
# 4   a      4      0
# 5   a      5      0


# 중복된 컬럼이 없는 경우 따로 지정
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df3
# <출력>
#   lkey  data1
# 0    b      0
# 1    b      1
# 2    a      2
# 3    c      3
# 4    a      4
# 5    a      5
# 6    b      6

df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
df4
# <출력>
#   rkey  data2
# 0    a      0
# 1    b      1
# 2    d      2

pd.merge(df3, df4, left_on='lkey', right_on='rkey')
# <출력>
#   lkey  data1 rkey  data2
# 0    b      0    b      1
# 1    b      1    b      1
# 2    b      6    b      1
# 3    a      2    a      0
# 4    a      4    a      0
# 5    a      5    a      0



# merge()함수는 기본적으로 inner join 수행
# how 인자로 'left', 'right', 'outer' 설정 가능
pd.merge(df1, df2, how='outer')
# <출력>
#   key  data1  data2
# 0   b    0.0    1.0
# 1   b    1.0    1.0
# 2   b    6.0    1.0
# 3   a    2.0    0.0
# 4   a    4.0    0.0
# 5   a    5.0    0.0
# 6   c    3.0    NaN
# 7   d    NaN    2.0


###

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df1
# <출력>
#   key  data1
# 0   b      0
# 1   b      1
# 2   a      2
# 3   c      3
# 4   a      4
# 5   b      5
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
df2
# <출력>
#   key  data2
# 0   a      0
# 1   b      1
# 2   a      2
# 3   b      3
# 4   d      4

pd.merge(df1, df2, on='key', how='left')
# <출력>
#    key  data1  data2
# 0    b      0    1.0
# 1    b      0    3.0
# 2    b      1    1.0
# 3    b      1    3.0
# 4    a      2    0.0
# 5    a      2    2.0
# 6    c      3    NaN
# 7    a      4    0.0
# 8    a      4    2.0
# 9    b      5    1.0
# 10   b      5    3.0


#  두 로우의 데카르트곱 반환
pd.merge(df1, df2, how='inner')
# <출력>
#   key  data1  data2
# 0   b      0      1
# 1   b      0      3
# 2   b      1      1
# 3   b      1      3
# 4   b      5      1
# 5   b      5      3
# 6   a      2      0
# 7   a      2      2
# 8   a      4      0
# 9   a      4      2



# 여러 개의 키를 병합하려면 컬럼 이름이 담긴 리스트 이용
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],  'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],  'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})
pd.merge(left, right, on=['key1', 'key2'], how='outer')
# <출력>
#   key1 key2  lval  rval
# 0  foo  one   1.0   4.0
# 1  foo  one   1.0   5.0
# 2  foo  two   2.0   NaN
# 3  bar  one   3.0   6.0
# 4  bar  two   NaN   7.0

#
#겹치는 컬럼 이름에 대한 처리
#1. 수동으로 컬럼이름을 겹치게 한다.
#2. merge()함수에 있는 suffixes 인자로 두 DataFrame 객체에서 겹치는 컬럼 이름 뒤에 붙일 문자열지정

pd.merge(left, right, on='key1')
# <출력>
#   key1 key2_x  lval key2_y  rval
# 0  foo    one     1    one     4
# 1  foo    one     1    one     5
# 2  foo    two     2    one     4
# 3  foo    two     2    one     5
# 4  bar    one     3    one     6
# 5  bar    one     3    two     7

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
# <출력>
#   key1 key2_left  lval key2_right  rval
# 0  foo       one     1        one     4
# 1  foo       one     1        one     5
# 2  foo       two     2        one     4
# 3  foo       two     2        one     5
# 4  bar       one     3        one     6
# 5  bar       one     3        two     7






# pandas user guide 참조


## 병합하려는 키가 DataFrame 의 색인일 경우

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
left1
# <출력>
#   key  value
# 0   a      0
# 1   b      1
# 2   a      2
# 3   a      3
# 4   b      4
# 5   c      5

right1
# <출력>
#    group_val
# a        3.5
# b        7.0

pd.merge(left1, right1, left_on='key', right_index=True)
# <출력>
#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0



# 외부조인
pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
# <출력>
#   key  value  group_val
# 0   a      0        3.5
# 2   a      2        3.5
# 3   a      3        3.5
# 1   b      1        7.0
# 4   b      4        7.0
# 5   c      5        NaN


# 계층 색인된 데이터 병합
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002], 'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])
lefth
# <출력>
#      key1  key2  data
# 0    Ohio  2000   0.0
# 1    Ohio  2001   1.0
# 2    Ohio  2002   2.0
# 3  Nevada  2001   3.0
# 4  Nevada  2002   4.0

righth
# <출력>
#              event1  event2
# Nevada 2001       0       1
#        2000       2       3
# Ohio   2000       4       5
#        2000       6       7
#        2001       8       9
#        2002      10      11




# 리스트로 여러 개의 컬럼을 지정하여 병합 (중복되는 색인값을 다룰 때는 how='outer'옵션 사용
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
# <출력>
#      key1  key2  data  event1  event2
# 0    Ohio  2000   0.0       4       5
# 0    Ohio  2000   0.0       6       7
# 1    Ohio  2001   1.0       8       9
# 2    Ohio  2002   2.0      10      11
# 3  Nevada  2001   3.0       0       1

pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer')
# <출력>
#      key1  key2  data  event1  event2
# 0    Ohio  2000   0.0     4.0     5.0
# 0    Ohio  2000   0.0     6.0     7.0
# 1    Ohio  2001   1.0     8.0     9.0
# 2    Ohio  2002   2.0    10.0    11.0
# 3  Nevada  2001   3.0     0.0     1.0
# 4  Nevada  2002   4.0     NaN     NaN
# 4  Nevada  2000   NaN     2.0     3.0


# 양쪽에 공통적으로 존재하는 여러 개의 색인을 병합
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'], columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
left2
# <출력>
#    Ohio  Nevada
# a   1.0     2.0
# c   3.0     4.0
# e   5.0     6.0

right2
# <출력>
#    Missouri  Alabama
# b       7.0      8.0
# c       9.0     10.0
# d      11.0     12.0
# e      13.0     14.0

pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
# <출력>
#    Ohio  Nevada  Missouri  Alabama
# a   1.0     2.0       NaN      NaN
# b   NaN     NaN       7.0      8.0
# c   3.0     4.0       9.0     10.0
# d   NaN     NaN      11.0     12.0
# e   5.0     6.0      13.0     14.0



# 색인으로 병합할때 DataFrame 의 join 메서드 사용
left2.join(right2, how='outer')
# <출력>
#    Ohio  Nevada  Missouri  Alabama
# a   1.0     2.0       NaN      NaN
# b   NaN     NaN       7.0      8.0
# c   3.0     4.0       9.0     10.0
# d   NaN     NaN      11.0     12.0
# e   5.0     6.0      13.0     14.0



# join 메서드를 호출한 DataFrame 의 컬럼 중 하나에 대해 조인을 수행
left1.join(right1, on='key')
# <출력>
#   key  value  group_val
# 0   a      0        3.5
# 1   b      1        7.0
# 2   a      2        3.5
# 3   a      3        3.5
# 4   b      4        7.0
# 5   c      5        NaN

# 색인 대 색인으로 두 DataFrame 을 병합하려면 DataFrame 의 리스트에 join 메서드 사용
another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])
another
# <출력>
#    New York  Oregon
# a       7.0     8.0
# c       9.0    10.0
# e      11.0    12.0
# f      16.0    17.0

left2.join([right2, another])
# <출력>
#    Ohio  Nevada  Missouri  Alabama  New York  Oregon
# a   1.0     2.0       NaN      NaN       7.0     8.0
# c   3.0     4.0       9.0     10.0       9.0    10.0
# e   5.0     6.0      13.0     14.0      11.0    12.0

left2.join([right2, another], how='outer')
# <출력>
#    Ohio  Nevada  Missouri  Alabama  New York  Oregon
# a   1.0     2.0       NaN      NaN       7.0     8.0
# c   3.0     4.0       9.0     10.0       9.0    10.0
# e   5.0     6.0      13.0     14.0      11.0    12.0
# b   NaN     NaN       7.0      8.0       NaN     NaN
# d   NaN     NaN      11.0     12.0       NaN     NaN
# f   NaN     NaN       NaN      NaN      16.0    17.0





# Numpy 는 ndarray 를 이어붙이는 concatenate()함수 제공
arr = np.arange(12).reshape((3, 4))
arr
# <출력>
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])


# column 기준으로 병합
np.concatenate([arr, arr], axis=1)
# <출력>
# array([[ 0,  1,  2,  3,  0,  1,  2,  3],
#        [ 4,  5,  6,  7,  4,  5,  6,  7],
#        [ 8,  9, 10, 11,  8,  9, 10, 11]])





#####

s1 = pd.Series([0, 1], index=['a', 'b'])
s1
# <출력>
# a    0
# b    1
# dtype: int64

s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s2
# <출력>
# c    2
# d    3
# e    4
# dtype: int64

s3 = pd.Series([5, 6], index=['f', 'g'])
s3
# <출력>
# f    5
# g    6
# dtype: int64


#concat()함수에 전달하면 값과 색인을 연결
pd.concat([s1, s2, s3])
# <출력>
# a    0
# b    1
# c    2
# d    3
# e    4
# f    5
# g    6
# dtype: int64

# concat()함수는 axis=0 을 기본값으로 새로운 Series 객체를 생성
# 만약 axis=1 을 넘긴다면 결과는 DataFrame 이 된다(axis=1 은 컬럼을 의미)
pd.concat([s1, s2, s3], axis=1)
# <출력>
#      0    1    2
# a  0.0  NaN  NaN
# b  1.0  NaN  NaN
# c  NaN  2.0  NaN
# d  NaN  3.0  NaN
# e  NaN  4.0  NaN
# f  NaN  NaN  5.0
# g  NaN  NaN  6.0



# join='inner'옵션을 사용하여 교집합을 구할 수도 있다
# <s1>
# a    0
# b    1
# <s3>
# f    5
# g    6
s4 = pd.concat([s1, s3])
s4
# <출력>
# a    0
# b    1
# f    5
# g    6
# dtype: int64


pd.concat([s1, s4], axis=1)
# <출력>
#      0  1
# a  0.0  0
# b  1.0  1
# f  NaN  5
# g  NaN  6

pd.concat([s1, s4], axis=1, join='inner')
# <출력>
#    0  1
# a  0  0
# b  1  1




# join_axes 인자로 병합하려는 축을 직접 지정
pd.concat([s1, s4], axis=1, join_axes=[['a', 'b', 'c', 'f']])
# join_axes : deprecated
# <출력>
#      0    1
# a  0.0  0.0
# b  1.0  1.0
# c  NaN  NaN
# f  NaN  5.0



# 계층적 색인을 생성하려면 keys 인자 사용
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
result
# <출력>
# one    a    0
#        b    1
# two    a    0
#        b    1
# three  f    5
#        g    6
# dtype: int64

result.unstack()
# <출력>
#          a    b    f    g
# one    0.0  1.0  NaN  NaN
# two    0.0  1.0  NaN  NaN
# three  NaN  NaN  5.0  6.0


# axis=1 로 병합할 경우 keys 는 DataFrame 의 컬럼명이 된다.
pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])
# <출력>
#    one  two  three
# a  0.0  NaN    NaN
# b  1.0  NaN    NaN
# c  NaN  2.0    NaN
# d  NaN  3.0    NaN
# e  NaN  4.0    NaN
# f  NaN  NaN    5.0
# g  NaN  NaN    6.0


df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],  columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],  columns=['three', 'four'])
df1
# <출력>
#    one  two
# a    0    1
# b    2    3
# c    4    5

df2
# <출력>
#    three  four
# a      5     6
# c      7     8

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
# <출력>
#   level1     level2
#      one two  three four
# a      0   1    5.0  6.0
# b      2   3    NaN  NaN
# c      4   5    7.0  8.0



# 리스트 대신 객체의 dict 를 이용하면 dict 의 키가 keys 옵션으로 사용된다.
pd.concat({'level1': df1, 'level2': df2}, axis=1)
# <출력>
#   level1     level2
#      one two  three four
# a      0   1    5.0  6.0
# b      2   3    NaN  NaN
# c      4   5    7.0  8.0



# 새로 생성된 계층 names 로 지정
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'], names=['upper', 'lower'])
# <출력>
# upper level1     level2
# lower    one two  three four
# a          0   1    5.0  6.0
# b          2   3    NaN  NaN
# c          4   5    7.0  8.0

# DataFrame 의 로우색인이 분석에 필요한 데이터를 포함하고 있지 않은 경우
df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

df1
# <출력>
#           a         b         c         d
# 0  1.246435  1.007189 -1.296221  0.274992
# 1  0.228913  1.352917  0.886429 -2.001637
# 2 -0.371843  1.669025 -0.438570 -0.539741

df2
# <출력>
#           b         d         a
# 0  0.476985  3.248944 -1.021228
# 1 -0.577087  0.124121  0.302614



# 이 경우 ignore_index=True 옵션 사용
pd.concat([df1, df2], ignore_index=True) # row bind
# <출력>
#           a         b         c         d
# 0  1.246435  1.007189 -1.296221  0.274992
# 1  0.228913  1.352917  0.886429 -2.001637
# 2 -0.371843  1.669025 -0.438570 -0.539741
# 3 -1.021228  0.476985       NaN  3.248944
# 4  0.302614 -0.577087       NaN  0.124121



## combining




# 벡터화된 if-else 구문을 표현하는 NumPy 의 where()함수
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
a
# <출력>
# f    NaN
# e    2.5
# d    NaN
# c    3.5
# b    4.5
# a    NaN
# dtype: float64

b
# <출력>
# f    0.0
# e    1.0
# d    2.0
# c    3.0
# b    4.0
# a    NaN
# dtype: float64

# null 이면 b, 아니면 a
np.where(pd.isnull(a), b, a)
# <출력>
# array([0. , 2.5, 2. , 3.5, 4.5, nan])

#combine_first 메서드는 위와 동일한 연산을 제공
b[:-2].combine_first(a[2:])
# <출력>
# a    NaN
# b    4.5
# c    3.0
# d    2.0
# e    1.0
# f    0.0
# dtype: float64


#combine_first 메서드는 컬럼에 대해 같은 동작을 한다.
# 호출하는 객체에서 누락된 데이터를 인자로 넘긴 객체에 있는 값으로 채워 넣을 수 있다.
df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan], 'b': [np.nan, 2., np.nan, 6.],  'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],  'b': [np.nan, 3., 4., 6., 8.]})

df1
# <출력>
#      a    b   c
# 0  1.0  NaN   2
# 1  NaN  2.0   6
# 2  5.0  NaN  10
# 3  NaN  6.0  14

df2
# <출력>
#      a    b
# 0  5.0  NaN
# 1  4.0  3.0
# 2  NaN  4.0
# 3  3.0  6.0
# 4  7.0  8.0


# NaN 또는 empty 자리에 df2 데이터 채우기
df1.combine_first(df2)
# <출력>
#      a    b     c
# 0  1.0  NaN   2.0
# 1  4.0  2.0   6.0
# 2  5.0  4.0  10.0
# 3  3.0  6.0  14.0
# 4  7.0  8.0   NaN




# 계층적 색인은 DataFrame 의 데이터를 재배치하는 다음의 방식 제공
# 1. stack: 데이터의 컬럼을 로우로 피벗(회전)
# 2. unstack: 로우를 컬럼으로 피벗





data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'],
                                   name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                                     name='number'))
data
# <출력>
# number    one  two  three
# state
# Ohio        0    1      2
# Colorado    3    4      5


result = data.stack()
result
# <출력>
# state     number
# Ohio      one       0
#           two       1
#           three     2
# Colorado  one       3
#           two       4
#           three     5
# dtype: int32



# 레벨 숫자나 이름을 전달해서 끄집어낼 단계 지정 가능
result.unstack(0)
# <출력>
# state   Ohio  Colorado
# number
# one        0         3
# two        1         4
# three      2         5

result.unstack(1)
# <출력>
# number    one  two  three
# state
# Ohio        0    1      2
# Colorado    3    4      5

result.unstack('state')
# <출력>
# state   Ohio  Colorado
# number
# one        0         3
# two        1         4
# three      2         5



#unstack 하게 되면 누락된 데이터가 생길 수 있다.
s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s1
# <출력>
# a    0
# b    1
# c    2
# d    3
# dtype: int64


s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
s2
# <출력>
# c    4
# d    5
# e    6
# dtype: int64


data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2
# <출력>
# one  a    0
#      b    1
#      c    2
#      d    3
# two  c    4
#      d    5
#      e    6
# dtype: int64


data2.unstack()
# <출력>
#        a    b    c    d    e
# one  0.0  1.0  2.0  3.0  NaN
# two  NaN  NaN  4.0  5.0  6.0







# stack 메서드는 누락된 데이터를 자동으로 걸려내기 때문에 연산을 쉽게 원상 복구할 수 있다.
data2.unstack()
# <출력>
#        a    b    c    d    e
# one  0.0  1.0  2.0  3.0  NaN
# two  NaN  NaN  4.0  5.0  6.0


data2.unstack().stack()
# <출력>
# one  a    0.0
#      b    1.0
#      c    2.0
#      d    3.0
# two  c    4.0
#      d    5.0
#      e    6.0
# dtype: float64


data2.unstack().stack(dropna=False)
# <출력>
# one  a    0.0
#      b    1.0
#      c    2.0
#      d    3.0
#      e    NaN
# two  a    NaN
#      b    NaN
#      c    4.0
#      d    5.0
#      e    6.0
# dtype: float64


# DataFrame 을 unstack()할 때 unstack 레벨은 결과에서 가장 낮은 단계가 된다.
df = pd.DataFrame({'left': result, 'right': result + 5}, columns=pd.Index(['left', 'right'], name='side'))
df
# <출력>
# side             left  right
# state    number
# Ohio     one        0      5
#          two        1      6
#          three      2      7
# Colorado one        3      8
#          two        4      9
#          three      5     10


df.unstack('state')
# <출력>
# side   left          right
# state  Ohio Colorado  Ohio Colorado
# number
# one       0        3     5        8
# two       1        4     6        9
# three     2        5     7       10



# stack 을 호출할 때 쌓을 축의 이름을 지정할 수 있다.
df.unstack('state').stack('side')
# <출력>
# state         Colorado  Ohio
# number side
# one    left          3     0
#        right         8     5
# two    left          4     1
#        right         9     6
# three  left          5     2
#        right        10     7





# 시계열 데이터는 일반적으로 시간 순서대로 나열
data = pd.read_csv('C:/macrodata.csv')
data.head()
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})

ldata[:10]
# <출력>
#                            date     item     value
# 0 1959-03-31 23:59:59.999999999  realgdp  2710.349
# 1 1959-03-31 23:59:59.999999999     infl     0.000
# 2 1959-03-31 23:59:59.999999999    unemp     5.800
# 3 1959-06-30 23:59:59.999999999  realgdp  2778.801
# 4 1959-06-30 23:59:59.999999999     infl     2.340
# 5 1959-06-30 23:59:59.999999999    unemp     5.100
# 6 1959-09-30 23:59:59.999999999  realgdp  2775.488
# 7 1959-09-30 23:59:59.999999999     infl     2.740
# 8 1959-09-30 23:59:59.999999999    unemp     5.300
# 9 1959-12-31 23:59:59.999999999  realgdp  2785.204




#pivot 메서드가 이런 변형을 지원
pivoted = ldata.pivot('date', 'item', 'value')

pivoted
# <출력>
# item                           infl    realgdp  unemp
# date
# 1959-03-31 23:59:59.999999999  0.00   2710.349    5.8
# 1959-06-30 23:59:59.999999999  2.34   2778.801    5.1
# 1959-09-30 23:59:59.999999999  2.74   2775.488    5.3
# 1959-12-31 23:59:59.999999999  0.27   2785.204    5.6
# 1960-03-31 23:59:59.999999999  2.31   2847.699    5.2
#                              ...        ...    ...
# 2008-09-30 23:59:59.999999999 -3.16  13324.600    6.0
# 2008-12-31 23:59:59.999999999 -8.79  13141.920    6.9
# 2009-03-31 23:59:59.999999999  0.94  12925.410    8.1
# 2009-06-30 23:59:59.999999999  3.37  12901.504    9.2
# 2009-09-30 23:59:59.999999999  3.56  12990.341    9.6
# [203 rows x 3 columns]

#한 번에 두개의 컬럼을 동시에 변형
ldata['value2'] = np.random.randn(len(ldata))

ldata[:10]
# <출력>
#                            date     item     value    value2
# 0 1959-03-31 23:59:59.999999999  realgdp  2710.349 -0.204708
# 1 1959-03-31 23:59:59.999999999     infl     0.000  0.478943
# 2 1959-03-31 23:59:59.999999999    unemp     5.800 -0.519439
# 3 1959-06-30 23:59:59.999999999  realgdp  2778.801 -0.555730
# 4 1959-06-30 23:59:59.999999999     infl     2.340  1.965781
# 5 1959-06-30 23:59:59.999999999    unemp     5.100  1.393406
# 6 1959-09-30 23:59:59.999999999  realgdp  2775.488  0.092908
# 7 1959-09-30 23:59:59.999999999     infl     2.740  0.281746
# 8 1959-09-30 23:59:59.999999999    unemp     5.300  0.769023
# 9 1959-12-31 23:59:59.999999999  realgdp  2785.204  1.246435



#마지막 인자를 생략해서 계층적 컬럼을 가지는 DataFrame 을 얻울 수 있다.
pivoted = ldata.pivot('date', 'item')

pivoted[:5]
# <출력>
#                               value            ...    value2
# item                           infl   realgdp  ...   realgdp     unemp
# date                                           ...
# 1959-03-31 23:59:59.999999999  0.00  2710.349  ... -0.204708 -0.519439
# 1959-06-30 23:59:59.999999999  2.34  2778.801  ... -0.555730  1.393406
# 1959-09-30 23:59:59.999999999  2.74  2775.488  ...  0.092908  0.769023
# 1959-12-31 23:59:59.999999999  0.27  2785.204  ...  1.246435 -1.296221
# 1960-03-31 23:59:59.999999999  2.31  2847.699  ...  0.274992  1.352917

pivoted['value'][:5]
# <출력>
# item                           infl   realgdp  unemp
# date
# 1959-03-31 23:59:59.999999999  0.00  2710.349    5.8
# 1959-06-30 23:59:59.999999999  2.34  2778.801    5.1
# 1959-09-30 23:59:59.999999999  2.74  2775.488    5.3
# 1959-12-31 23:59:59.999999999  0.27  2785.204    5.6
# 1960-03-31 23:59:59.999999999  2.31  2847.699    5.2





# unstack 메서드를 이용해서 형태를 변경하는 단축키 같은 메서드
unstacked = ldata.set_index(['date', 'item']).unstack('item')

unstacked[:7]
# <출력>
#                               value            ...    value2
# item                           infl   realgdp  ...   realgdp     unemp
# date                                           ...
# 1959-03-31 23:59:59.999999999  0.00  2710.349  ... -0.204708 -0.519439
# 1959-06-30 23:59:59.999999999  2.34  2778.801  ... -0.555730  1.393406
# 1959-09-30 23:59:59.999999999  2.74  2775.488  ...  0.092908  0.769023
# 1959-12-31 23:59:59.999999999  0.27  2785.204  ...  1.246435 -1.296221
# 1960-03-31 23:59:59.999999999  2.31  2847.699  ...  0.274992  1.352917
# 1960-06-30 23:59:59.999999999  0.14  2834.390  ...  0.886429 -0.371843
# 1960-09-30 23:59:59.999999999  2.70  2839.022  ...  1.669025 -0.539741
# [7 rows x 6 columns]



#“Wide” to “Long”
df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

df
# <출력>
#    key  A  B  C
# 0  foo  1  4  7
# 1  bar  2  5  8
# 2  baz  3  6  9


#'key'를 그룹 구분자로 지정
melted = pd.melt(df, ['key'])

melted
# <출력>
#    key variable  value
# 0  foo        A      1
# 1  bar        A      2
# 2  baz        A      3
# 3  foo        B      4
# 4  bar        B      5
# 5  baz        B      6
# 6  foo        C      7
# 7  bar        C      8
# 8  baz        C      9


# pivot 을 사용하여 원래 모양으로 되돌릴 수 있다.
reshaped = melted.pivot('key', 'variable', 'value')

reshaped
# <출력>
# variable  A  B  C
# key
# bar       2  5  8
# baz       3  6  9
# foo       1  4  7


# reset_index 를 이용해서 데이터를 다시 컬럼으로 되돌려놓는다.
reshaped.reset_index()
# <출력>
# variable  key  A  B  C
# 0         bar  2  5  8
# 1         baz  3  6  9
# 2         foo  1  4  7


# 데이터값으로 사용할 컬럼들의 집합을 지정할 수도 있다.
pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])
# <출력>
#    key variable  value
# 0  foo        A      1
# 1  bar        A      2
# 2  baz        A      3
# 3  foo        B      4
# 4  bar        B      5
# 5  baz        B      6

# pandas.melt 는 그룹 구분자 없이도 사용할 수 있다.
pd.melt(df, value_vars=['A', 'B', 'C'])
# <출력>
#   variable  value
# 0        A      1
# 1        A      2
# 2        A      3
# 3        B      4
# 4        B      5
# 5        B      6
# 6        C      7
# 7        C      8
# 8        C      9


pd.melt(df, value_vars=['key', 'A', 'B'])
# <출력>
#   variable value
# 0      key   foo
# 1      key   bar
# 2      key   baz
# 3        A     1
# 4        A     2
# 5        A     3
# 6        B     4
# 7        B     5
# 8        B     6

















