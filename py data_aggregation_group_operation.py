#

import numpy as np
import pandas as pd
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)




#  group by

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
df
# <출력>
#   key1 key2     data1     data2
# 0    a  one  0.981007 -1.006219
# 1    a  two -0.873717 -0.902148
# 2    b  one -1.015634  0.752769
# 3    b  two -0.411244 -0.490509
# 4    a  one  1.465621 -0.524672

# 이 데이터를 key1 으로 묶고 각 그룹에서 data1 의 평균을 구하기
grouped = df['data1'].groupby(df['key1'])
grouped

grouped.mean()
# <출력>
# key1
# a    0.524304
# b   -0.713439
# Name: data1, dtype: float64

means=df['data1'].groupby([df['key1'],df['key2']]).mean()
means
# <출력>
# key1  key2
# a     one     1.223314
#       two    -0.873717
# b     one    -1.015634
#       two    -0.411244
# Name: data1, dtype: float64

# 두개의 색인으로 묶음
means.unstack()
# <출력>
# key2       one       two
# key1
# a     1.223314 -0.873717
# b    -1.015634 -0.411244



# 길이만 같다면 어떤 배열도 상관없다.
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])

df['data1'].groupby([states, years]).mean()
# <출력>
# California  2005   -0.873717
#             2006   -1.015634
# Ohio        2005    0.284882
#             2006    1.465621
# Name: data1, dtype: float64


df.groupby('key1').mean()
# <출력>
#          data1     data2
# key1
# a     0.524304 -0.811013
# b    -0.713439  0.131130

df.groupby(['key1', 'key2']).mean()
# <출력>
#               data1     data2
# key1 key2
# a    one   1.223314 -0.765446
#      two  -0.873717 -0.902148
# b    one  -1.015634  0.752769
#      two  -0.411244 -0.490509


#  GroupBy 메서드는 그룹의 크기를 담고 있는 Series 를 반환하는 size 메서드
df.groupby(['key1', 'key2']).size()
# <출력>
# key1  key2
# a     one     2
#       two     1
# b     one     1
#       two     1
# dtype: int64


# 튜플로 반환
for name, group in df.groupby('key1'):
 print(name)
 print(group)

# <출력>
# a
#   key1 key2     data1     data2
# 0    a  one  0.981007 -1.006219
# 1    a  two -0.873717 -0.902148
# 4    a  one  1.465621 -0.524672
# b
#   key1 key2     data1     data2
# 2    b  one -1.015634  0.752769
# 3    b  two -0.411244 -0.490509


# 색인이 여럿 존재하는 경우 튜플의 첫 번째 원소가 색인값이 된다.
for (k1, k2), group in df.groupby(['key1', 'key2']):
 print((k1, k2))
 print(group)

# <출력>
# ('a', 'one')
#   key1 key2     data1     data2
# 0    a  one  0.981007 -1.006219
# 4    a  one  1.465621 -0.524672
# ('a', 'two')
#   key1 key2     data1     data2
# 1    a  two -0.873717 -0.902148
# ('b', 'one')
#   key1 key2     data1     data2
# 2    b  one -1.015634  0.752769
# ('b', 'two')
#   key1 key2     data1     data2
# 3    b  two -0.411244 -0.490509




# dict 로 반환
pieces = dict(list(df.groupby('key1')))

pieces['b']
# <출력>
#   key1 key2     data1     data2
# 2    b  one -1.015634  0.752769
# 3    b  two -0.411244 -0.490509


# axis = 0,1
df.dtypes
grouped = df.groupby(df.dtypes, axis=1)


for dtype, group in grouped:
 print(dtype)
 print(group)

# <출력>
# float64
#       data1     data2
# 0  0.981007 -1.006219
# 1 -0.873717 -0.902148
# 2 -1.015634  0.752769
# 3 -0.411244 -0.490509
# 4  1.465621 -0.524672
# object
#   key1 key2
# 0    a  one
# 1    a  two
# 2    b  one
# 3    b  two
# 4    a  one





## selecting

df.groupby('key1')['data1']
df.groupby('key1')[['data2']]


# =
df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1'])


# 소수의 컬럼만 집계하고 싶은 경우
df.groupby(['key1', 'key2'])[['data2']].mean()
# <출력>
#               data2
# key1 key2
# a    one  -0.765446
#      two  -0.902148
# b    one   0.752769
#      two  -0.490509



#단일 값으로 하나의 컬럼 이름만 넘겼을 경우
s_grouped = df.groupby(['key1', 'key2'])['data2']
s_grouped
s_grouped.mean()
# <출력>
# key1  key2
# a     one    -0.765446
#       two    -0.902148
# b     one     0.752769
#       two    -0.490509
# Name: data2, dtype: float64



# grouping
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1, 2]] = np.nan # Add a few NA values

people
# <출력>
#                a         b         c         d         e
# Joe    -0.699196  0.352361  0.068103 -0.930342  0.845400
# Steve   0.016472  0.844963  1.850834  0.022074 -1.369179
# Wes     0.887204       NaN       NaN -0.048565  1.235021
# Jim    -0.433295  1.391035  0.820211 -0.247423  0.302271
# Travis  0.543980 -0.942369 -1.266383  0.937250 -0.720102

mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f' : 'orange'}
by_column = people.groupby(mapping, axis=1)

by_column.sum()
# <출력>
#             blue       red
# Joe    -0.862239  0.498565
# Steve   1.872908 -0.507744
# Wes    -0.048565  2.122225
# Jim     0.572787  1.260011
# Travis -0.329133 -1.118490


map_series = pd.Series(mapping)
map_series
# <출력>
# a       red
# b       red
# c      blue
# d      blue
# e       red
# f    orange
# dtype: object


people.groupby(map_series, axis=1).count()
# <출력>
#         blue  red
# Joe        2    3
# Steve      2    3
# Wes        1    2
# Jim        2    3
# Travis     2    3



##########################


# 길이별로 그룹묶기
people.groupby(len).sum()
# <출력>
#           a         b         c         d         e
# 3 -0.245287  1.743396  0.888313 -1.226330  2.382692
# 5  0.016472  0.844963  1.850834  0.022074 -1.369179
# 6  0.543980 -0.942369 -1.266383  0.937250 -0.720102

key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()
# <출력>
#               a         b         c         d         e
# 3 one -0.699196  0.352361  0.068103 -0.930342  0.845400
#   two -0.433295  1.391035  0.820211 -0.247423  0.302271
# 5 one  0.016472  0.844963  1.850834  0.022074 -1.369179
# 6 two  0.543980 -0.942369 -1.266383  0.937250 -0.720102


# 하나만 사용해서 집계

columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]], names=['cty', 'tenor'])
hier_df = pd.DataFrame(np.random.randn(4,5),columns=columns)
hier_df
# <출력>
# cty          US                            JP
# tenor         1         3         5         1         3
# 0     -1.593952 -0.375498 -0.958704  0.794336 -1.605108
# 1      0.543710  0.925166 -1.469629 -0.399592  1.417343
# 2     -0.897609  1.844805  1.253168 -1.490932 -0.027734
# 3      1.375236 -0.025208 -0.667880 -2.868018  0.210689


# level 예약어 사용
hier_df.groupby(level='cty',axis=1).count()
# <출력>
# cty  JP  US
# 0     2   3
# 1     2   3
# 2     2   3
# 3     2   3



##### 데이터 집계 #####


df
# <출력>
#   key1 key2     data1     data2
# 0    a  one  0.981007 -1.006219
# 1    a  two -0.873717 -0.902148
# 2    b  one -1.015634  0.752769
# 3    b  two -0.411244 -0.490509
# 4    a  one  1.465621 -0.524672

grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)
# <출력>
# key1
# a    1.368698
# b   -0.471683
# Name: data1, dtype: float64


# 자신의 데이터 집계함수를 사용하려면 배열의 aggregate 나 agg 메서드에 해당 함수를 넘기면 된다.
def peak_to_peak(arr):
 return arr.max() - arr.min()

grouped.agg(peak_to_peak)
# <출력>
# data1     data2
# key1
# a     2.339338  0.481547
# b     0.604391  1.243278


# describe ; 데이터를 집계하지 않아도 잘 작동
grouped.describe()
# <출력>
#      data1                                ...     data2
#      count      mean       std       min  ...       25%       50%      75%       max
# key1                                      ...
# a      3.0  0.524304  1.234730 -0.873717  ... -0.954183 -0.902148 -0.71341 -0.524672
# b      2.0 -0.713439  0.427369 -1.015634  ... -0.179689  0.131130  0.44195  0.752769
# [2 rows x 16 columns]


###### column wise



#  read_csv()함수로 데이터를 불러온 다음 팁의 비율을 담기 위한 컬럼인 tip_pct 를 추가
tips = pd.read_csv('C:/tips.csv')
# <출력>


# Add tip percentage of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips[:6]
# <출력>
#    total_bill   tip smoker  day    time  size   tip_pct
# 0       16.99  1.01     No  Sun  Dinner     2  0.059447
# 1       10.34  1.66     No  Sun  Dinner     3  0.160542
# 2       21.01  3.50     No  Sun  Dinner     3  0.166587
# 3       23.68  3.31     No  Sun  Dinner     2  0.139780
# 4       24.59  3.61     No  Sun  Dinner     4  0.146808
# 5       25.29  4.71     No  Sun  Dinner     4  0.186240




grouped = tips.groupby(['day', 'smoker'])


# 함수 이름을 문자열로 넘기기

grouped = tips.groupby(['day', 'smoker'])

grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')
# <출력>
# day   smoker
# Fri   No        0.151650
#       Yes       0.174783
# Sat   No        0.158048
#       Yes       0.147906
# Sun   No        0.160113
#       Yes       0.187250
# Thur  No        0.160298
#       Yes       0.163863
# Name: tip_pct, dtype: float64


# 함수 이름을 컬럼 이름으로 하는 DataFrame 생성
grouped_pct.agg(['mean', 'std', peak_to_peak])
# <출력>
#                  mean       std  peak_to_peak
# day  smoker
# Fri  No      0.151650  0.028123      0.067349
#      Yes     0.174783  0.051293      0.159925
# Sat  No      0.158048  0.039767      0.235193
#      Yes     0.147906  0.061375      0.290095
# Sun  No      0.160113  0.042347      0.193226
#      Yes     0.187250  0.154134      0.644685
# Thur No      0.160298  0.038774      0.193350
#      Yes     0.163863  0.039389      0.151240



# # (2 개의 튜플을 가지는 리스트가 순서대로 매핑된다.)
grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])
# <출력>
#                   foo       bar
# day  smoker
# Fri  No      0.151650  0.028123
#      Yes     0.174783  0.051293
# Sat  No      0.158048  0.039767
#      Yes     0.147906  0.061375
# Sun  No      0.160113  0.042347
#      Yes     0.187250  0.154134
# Thur No      0.160298  0.038774
#      Yes     0.163863  0.039389

# tip_pct 와 total_bill 컬럼에 대해 동일한 세 가지 통계를 계산한다고 가정
functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
result
# <출력>



result['tip_pct']
# <출력>

# 튜플의 리스트를 넘기는 것도 가능/Durchschnitt ; 평균 , Abweichung ; 편차
ftuples = [('Durchschnitt', 'mean'), ('Abweichung', np.var)]
grouped['tip_pct', 'total_bill'].agg(ftuples)
# <출력>
#                  tip_pct              total_bill
#             Durchschnitt Abweichung Durchschnitt  Abweichung
# day  smoker
# Fri  No         0.151650   0.000791    18.420000   25.596333
#      Yes        0.174783   0.002631    16.813333   82.562438
# Sat  No         0.158048   0.001581    19.661778   79.908965
#      Yes        0.147906   0.003767    21.276667  101.387535
# Sun  No         0.160113   0.001793    20.506667   66.099980
#      Yes        0.187250   0.023757    24.120000  109.046044
# Thur No         0.160298   0.001503    17.113111   59.625081
#      Yes        0.163863   0.001551    19.190588   69.808518




#컬럼마다 다른함수 적용하기 ; agg 메서드
grouped.agg({'tip' : np.max, 'size' : 'sum'})
grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'], 'size' : 'sum'})
# <출력>
#               tip_pct                               size
#                   min       max      mean       std  sum
# day  smoker
# Fri  No      0.120385  0.187735  0.151650  0.028123    9
#      Yes     0.103555  0.263480  0.174783  0.051293   31
# Sat  No      0.056797  0.291990  0.158048  0.039767  115
#      Yes     0.035638  0.325733  0.147906  0.061375  104
# Sun  No      0.059447  0.252672  0.160113  0.042347  167
#      Yes     0.065660  0.710345  0.187250  0.154134   49
# Thur No      0.072961  0.266312  0.160298  0.038774  112
#      Yes     0.090014  0.241255  0.163863  0.039389   40


# as_index=False ; 색인되지 않도록 함 -> 불필요한 계산 피할 수 있음

tips.groupby(['day', 'smoker'], as_index=False).mean()
# <출력>
#     day smoker  total_bill       tip      size   tip_pct
# 0   Fri     No   18.420000  2.812500  2.250000  0.151650
# 1   Fri    Yes   16.813333  2.714000  2.066667  0.174783
# 2   Sat     No   19.661778  3.102889  2.555556  0.158048
# 3   Sat    Yes   21.276667  2.875476  2.476190  0.147906
# 4   Sun     No   20.506667  3.167895  2.929825  0.160113
# 5   Sun    Yes   24.120000  3.516842  2.578947  0.187250
# 6  Thur     No   17.113111  2.673778  2.488889  0.160298
# 7  Thur    Yes   19.190588  3.030000  2.352941  0.163863




### apply


def top(df, n=5, column='tip_pct'):
 return df.sort_values(by=column)[-n:]

top(tips, n=6)
# <출력> 
#      total_bill   tip smoker  day    time  size   tip_pct
# 109       14.31  4.00    Yes  Sat  Dinner     2  0.279525
# 183       23.17  6.50    Yes  Sun  Dinner     4  0.280535
# 232       11.61  3.39     No  Sat  Dinner     2  0.291990
# 67         3.07  1.00    Yes  Sat  Dinner     1  0.325733
# 178        9.60  4.00    Yes  Sun  Dinner     2  0.416667
# 172        7.25  5.15    Yes  Sun  Dinner     2  0.710345

tips.groupby('smoker').apply(top)
# <출력>     
#             total_bill   tip smoker   day    time  size   tip_pct
# smoker                                                           
# No     88        24.71  5.85     No  Thur   Lunch     2  0.236746
#        185       20.69  5.00     No   Sun  Dinner     5  0.241663
#        51        10.29  2.60     No   Sun  Dinner     2  0.252672
#        149        7.51  2.00     No  Thur   Lunch     2  0.266312
#        232       11.61  3.39     No   Sat  Dinner     2  0.291990
# Yes    109       14.31  4.00    Yes   Sat  Dinner     2  0.279525
#        183       23.17  6.50    Yes   Sun  Dinner     4  0.280535
#        67         3.07  1.00    Yes   Sat  Dinner     1  0.325733
#        178        9.60  4.00    Yes   Sun  Dinner     2  0.416667
#        172        7.25  5.15    Yes   Sun  Dinner     2  0.710345

# apply 메서드로 넘길 함수가 추가적인 인자를 받는다면 함수 이름 뒤에 붙여서 넘겨주면 된다.
tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill')
# <출력>             
#                  total_bill    tip smoker   day    time  size   tip_pct
# smoker day                                                             
# No     Fri  94        22.75   3.25     No   Fri  Dinner     2  0.142857
#        Sat  212       48.33   9.00     No   Sat  Dinner     4  0.186220
#        Sun  156       48.17   5.00     No   Sun  Dinner     6  0.103799
#        Thur 142       41.19   5.00     No  Thur   Lunch     5  0.121389
# Yes    Fri  95        40.17   4.73    Yes   Fri  Dinner     4  0.117750
#        Sat  170       50.81  10.00    Yes   Sat  Dinner     3  0.196812
#        Sun  182       45.35   3.50    Yes   Sun  Dinner     3  0.077178
#        Thur 197       43.11   5.00    Yes  Thur   Lunch     4  0.115982


# 앞에서 GroupBy 객체에 describe 메서드를 호출한 적이 있다.
result = tips.groupby('smoker')['tip_pct'].describe()
result
# <출력>       
#         count      mean       std  ...       50%       75%       max
# smoker                             ...                              
# No      151.0  0.159328  0.039910  ...  0.155625  0.185014  0.291990
# Yes      93.0  0.163196  0.085119  ...  0.153846  0.195059  0.710345

result.unstack('smoker')
# <출력> 
#        smoker
# count  No        151.000000
#        Yes        93.000000
# mean   No          0.159328
#        Yes         0.163196
# std    No          0.039910
#        Yes         0.085119
# min    No          0.056797
#        Yes         0.035638
# 25%    No          0.136906
#        Yes         0.106771
# 50%    No          0.155625
#        Yes         0.153846
# 75%    No          0.185014
#        Yes         0.195059
# max    No          0.291990
#        Yes         0.710345
# dtype: float64


# describe 같은 메서드를 호출하면 GroupBy 내부적으로 다음과 같은 단계를 수행
f = lambda x: x.describe()
grouped.apply(f)
# <출력> 
#                    total_bill       tip  size   tip_pct
# day  smoker                                            
# Fri  No     count    4.000000  4.000000  4.00  4.000000
#             mean    18.420000  2.812500  2.25  0.151650
#             std      5.059282  0.898494  0.50  0.028123
#             min     12.460000  1.500000  2.00  0.120385
#             25%     15.100000  2.625000  2.00  0.137239
#                        ...       ...   ...       ...
# Thur Yes    min     10.340000  2.000000  2.00  0.090014
#             25%     13.510000  2.000000  2.00  0.148038
#             50%     16.470000  2.560000  2.00  0.153846
#             75%     19.810000  4.000000  2.00  0.194837
#             max     43.110000  5.000000  4.00  0.241255
# [64 rows x 4 columns]



# groupby 메서드에 group_keys=False 로 설정하여 막을 수 있다.
tips.groupby('smoker', group_keys=False).apply(top)
# <출력> 
#      total_bill   tip smoker   day    time  size   tip_pct
# 88        24.71  5.85     No  Thur   Lunch     2  0.236746
# 185       20.69  5.00     No   Sun  Dinner     5  0.241663
# 51        10.29  2.60     No   Sun  Dinner     2  0.252672
# 149        7.51  2.00     No  Thur   Lunch     2  0.266312
# 232       11.61  3.39     No   Sat  Dinner     2  0.291990
# 109       14.31  4.00    Yes   Sat  Dinner     2  0.279525
# 183       23.17  6.50    Yes   Sun  Dinner     4  0.280535
# 67         3.07  1.00    Yes   Sat  Dinner     1  0.325733
# 178        9.60  4.00    Yes   Sun  Dinner     2  0.416667
# 172        7.25  5.15    Yes   Sun  Dinner     2  0.710345



# quntile
frame = pd.DataFrame({'data1': np.random.randn(1000), 'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)

quartiles[:10]
# <출력>
# 0     (-0.242, 1.509]
# 1    (-1.994, -0.242]
# 2     (-0.242, 1.509]
# 3     (-0.242, 1.509]
# 4     (-0.242, 1.509]
# 5    (-1.994, -0.242]
# 6       (1.509, 3.26]
# 7    (-1.994, -0.242]
# 8     (-0.242, 1.509]
# 9    (-1.994, -0.242]
# Name: data1, dtype: category
# Categories (4, interval[float64, right]):
# [(-3.752, -1.994] < (-1.994, -0.242] < (-0.242, 1.509] < (1.509, 3.26]]

def get_stats(group):
 return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}

grouped = frame.data2.groupby(quartiles)

grouped.apply(get_stats).unstack()
# <출력>
#                        min       max  count      mean
# data1
# (-3.752, -1.994] -2.815059  1.766162   17.0  0.210374
# (-1.994, -0.242] -2.925113  2.653656  400.0 -0.011117
# (-0.242, 1.509]  -3.184377  2.424667  512.0 -0.010956
# (1.509, 3.26]    -3.428254  2.513530   71.0  0.161407



grouping=pd.qcut(frame.datal,10,labels=False) # qcut 데이터에 같은 수가 들어가도록 하는것
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()











# ex1

s = pd.Series(np.random.randn(6))
s[::2] = np.nan
s

s.fillna(s.mean())
states = ['Ohio', 'New York', 'Vermont', 'Florida', 'Oregon', 'Nevada', 'California', 'Idaho']
group_key=['East']*4+['West']*4
data=pd.Series(np.random.randn(8),index=states)
data

data[['Vermont','Nevada','Idaho']] = np.nan
data

data.groupby(group_key).mean()

fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)

fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)
# <출력>
# Ohio         -1.759884
# New York      0.143524
# Vermont       0.500000
# Florida       0.775893
# Oregon        0.570685
# Nevada       -1.000000
# California    0.333238
# Idaho        -1.000000
# dtype: float64


# ex2

suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
 cards.extend(str(num) + suit for num in base_names)
deck = pd.Series(card_val, index=cards)
deck[:13]

def draw(deck, n=5):
 return deck.sample(n)
draw(deck)

get_suit = lambda card: card[-1] # last letter is suit
deck.groupby(get_suit).apply(draw, n=2)

deck.groupby(get_suit, group_keys=False).apply(draw, n=2)
# <출력>
# 5C     5
# 6C     6
# 2D     2
# 9D     9
# 7H     7
# QH    10
# 6S     6
# 8S     8
# dtype: int64


# ex3


import numpy as np
import pandas as pd


df = pd.DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                   'data': np.random.randn(8), 'weights': np.random.rand(8)})
df

grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
grouped.apply(get_wavg)

close_px = pd.read_csv('pandas_dataset2/stock_px.csv', parse_dates=True, index_col=0)
close_px.info()

close_px[-4:]

spx_corr = lambda x: x.corrwith(x['SPX'])
rets = close_px.pct_change().dropna()
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
by_year.apply(spx_corr)

by_year.apply(lambda g: g['AAPL'].corr(g['MSFT']))
# <출력>
# 1990    0.408271
# 1991    0.266807
# 1992    0.450592
# 1993    0.236917
# 1994    0.361638
#           ...
# 2007    0.417738
# 2008    0.611901
# 2009    0.432738
# 2010    0.571946
# 2011    0.581987
# Length: 22, dtype: float64



# ex4

import statsmodels.api as sm
def regress(data,yvar,xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept']=1.
    result = sm.OLS(Y,X).fit()
    return result.params
by_year.apply(regress,'AAPL',['SPX'])
# <출력>
#            SPX  intercept
# 1990  1.512772   0.001395
# 1991  1.187351   0.000396
# 1992  1.832427   0.000164
# 1993  1.390470  -0.002657
# 1994  1.190277   0.001617
#         ...        ...
# 2007  1.198761   0.003438
# 2008  0.968016  -0.001110
# 2009  0.879103   0.002954
# 2010  1.052608   0.001261





















































