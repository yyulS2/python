# 신유라





# 1.  pandas와 numpy를 import하고, pandas의 Series와 DataFrame을 네임스페이스로 import 하시오.
# random seed는 1357로 설정하시오.
# (난이도 : 3 / 배점 : 6점)

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


np.random.seed(1357)




# 2  다음의 데이터프레임을 구성하고 "debt" 컬럼이 Null인지 확인하시오.
# (난이도 : 3 / 배점 : 6점)
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002, 2003],
# 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
#
# frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four','five', 'six'])



data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
df=pd.DataFrame(data)
# print(df)

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four','five', 'six'])
df2=pd.DataFrame(frame2)
# print(df2)


df2.isnull()
# <출력>
#         year  state    pop  debt
# one    False  False  False  True
# two    False  False  False  True
# three  False  False  False  True
# four   False  False  False  True
# five   False  False  False  True
# six    False  False  False  True



#3 다음의 문자열 리스트를 Series로 변환하고 display하시오.
#(난이도 : 3 / 배점 : 6점)
#['aardvark', 'artichoke',  , 'avocado'] (3번째 자리 빈칸)


data = ['aardvark', 'artichoke', ' ', 'avocado']
str = pd.Series(data)
print(str)

# <출력>
# state    [Ohio, Ohio, Ohio, Nevada, Nevada, Nevada]
# year           [2000, 2001, 2002, 2001, 2002, 2003]
# pop                  [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
# dtype: object

# print(type(str))     # 문자열 리스트를 Series로 변환 됬는지 확인
print(str)






# 4  (4-6). 다음의 DataFrame을 구성하고 문제에서 필요한 python coding을 하시오.
# data = pd.DataFrame(np.arange(16).reshape((4, 4)),
# index=['Ohio', 'Colorado', 'Utah', 'New York'],
# columns=['one', 'two', 'three', 'four'])
#
# 'three'컬럼의 값이 5초과인 데이터를 display하시오


data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])



df4 = pd.DataFrame(data)
df4

# <출력>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

print(df4[(df4['three']>5)])

# <출력>
#           one  two  three  four
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15


# 5   'four' 컬럼을 삭제하고 결과를 display하시오
print(df4.drop(['four'],axis=1))

# <출력>
#           one  two  three
# Ohio        0    1      2
# Colorado    4    5      6
# Utah        8    9     10
# New York   12   13     14


# 6    'Utah' 로우를 삭제하고 결과를 display하시오.
print(df4.drop(['Utah'],axis=0))

# <출력>
#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# New York   12   13     14    15





# 7. 다음의 DataFrame을 구성하고 문제에서 필요한 python coding을 하시오.
# frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
# index=['three', 'one'],
# columns=['d', 'a', 'b', 'c'])
#
# 로우(row) 기준으로 내림차순으로 정렬하시오.

frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])


frame.sort_index(axis=0,ascending=False)

# <출력>
#         data1     data2
# 999 -0.806614  0.102174
# 998  1.612270  1.582495
# 997 -2.311026  0.857575
# 996 -0.653635 -0.795275
# 995 -0.544615 -0.020213
# ..        ...       ...
# 4    0.588798  0.502717
# 3    0.396050  0.026582
# 2    0.495327 -1.205817
# 1   -0.574306  0.580201
# 0    1.287155  0.557884
# [1000 rows x 2 columns]







# 8 컬럼(column) 기준으로 오름차순으로 정렬하시오.

#위에서 아래로


frame.sort_index(axis=1)
# <출력>
#         data1     data2
# 0    1.287155  0.557884
# 1   -0.574306  0.580201
# 2    0.495327 -1.205817
# 3    0.396050  0.026582
# 4    0.588798  0.502717
# ..        ...       ...
# 995 -0.544615 -0.020213
# 996 -0.653635 -0.795275
# 997 -2.311026  0.857575
# 998  1.612270  1.582495
# 999 -0.806614  0.102174
# [1000 rows x 2 columns]





# 9) (9-10). 아래 리스트를 이용하여 문제에서 필요한 python coding을 하시오.
# [1., , 3.5, , 7] (2번째 및 4번째 자리 빈칸)
#
# Series로 변환한 후 display하시오.



data = pd.Series([1,np.nan, 3.5,np.nan, 7])
data

# <출력>
# 0    1.0
# 1    NaN
# 2    3.5
# 3    NaN
# 4    7.0
# dtype: float64


data.dropna()
print(data.dropna())



# 10 ) NA(빈칸)을 제외한 숫자들의 평균을 빈칸에 추가하고 display하시오.

data2=data.fillna(data.mean())
data2

# <출력>
# 0    1.000000
# 1    3.833333
# 2    3.500000
# 3    3.833333
# 4    7.000000
# dtype: float64




# 11(11-13). 다음의 데이터프레임을 구성하고 문제에서 필요한 python coding을 하시오.
# np.random.seed(1234)
# data = pd.DataFrame(np.random.randn(1000, 4))
#
# 왼쪽에서 3번째 컬럼을 display하시오


np.random.seed(1234)
data = pd.DataFrame(np.random.randn(1000, 4))

data[2]

# <출력>
# 0     -0.787729
# 1     -1.023548
# 2     -1.681742
# 3      0.982752
# 4      0.928455
#          ...
# 995   -0.800367
# 996    0.861256
# 997   -0.523576
# 998    0.975213
# 999    0.734046
# Name: 2, Length: 1000, dtype: float64




# 12 해당 객체의 데이터의 각종 통계량을 요약해서 출력해주는 메서드를 사용하여 요약하여 보이시오

data.describe()

# <출력>
#                  0            1            2            3
# count  1000.000000  1000.000000  1000.000000  1000.000000
# mean      0.018901     0.028236     0.009364     0.010606
# std       1.022649     0.979162     0.996411     1.009030
# min      -3.263783    -3.016387    -3.264204    -3.599400
# 25%      -0.661701    -0.669782    -0.638663    -0.676337
# 50%       0.045745     0.052448    -0.042213    -0.000832
# 75%       0.774108     0.670692     0.674106     0.711965
# max       3.001147     2.904143     2.851651     3.287788




# 13   데이터의 절대값이 3이상인 데이터는 데이터의 부호(+/-)의 3배 한 값으로 대체하시오.

data[np.abs(data) >= 3] =  data * 3
data

# <출력>
#             0         1         2         3
# 0   -0.811898 -1.919443 -0.787729  2.559703
# 1   -0.004541  0.119074 -1.023548  2.175465
# 2    0.339052  0.575126 -1.681742  0.551767
# 3   -0.963786  0.910079  0.982752 -1.038906
# 4   -0.966813  0.836247  0.928455 -1.297852
# ..        ...       ...       ...       ...
# 995 -0.904152  1.008862 -0.800367  0.013173
# 996  0.615322 -1.048624  0.861256 -0.703710
# 997 -0.061109 -0.580050 -0.523576  0.732265
# 998  1.032645  0.527047  0.975213 -1.438392
# 999 -2.588696 -1.396938  0.734046 -0.061854






# 14  (14-15). 다음의 데이터프레임을 구성하고 문제에서 필요한 python coding을 하시오.
# df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
# 'A': [1, 2, 3],
# 'B': [4, 5, 6],
# 'C': [7, 8, 9]})
#
# 'key'를 그룹 구분자로 지정하여 wide form을 long form으로 변환하고 display하시오.
# (난이도 : 3 / 배점 : 6점)

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
df

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





# 15 pivot을 사용하여 long form에서 wide form으로 변환(원래의 데이터프레임으로 변환)하고 display하시오
# (난이도 : 3 / 배점 : 6점)

reshaped = melted.pivot('key', 'variable', 'value')

reshaped
# <출력>
# variable  A  B  C
# key
# bar       2  5  8
# baz       3  6  9
# foo       1  4  7

reshaped.reset_index()
# <출력>
# variable  key  A  B  C
# 0         bar  2  5  8
# 1         baz  3  6  9
# 2         foo  1  4  7




















