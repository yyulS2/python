


# 판다스 데이터프레임 안에 넘파이에의한 랜덤난수
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
        index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame
# <출력>
#                b         d         e
# Utah    0.274992  0.228913  1.352917
# Ohio    0.886429 -2.001637 -0.371843
# Texas   1.669025 -0.438570 -0.539741
# Oregon  0.476985  3.248944 -1.021228
np.abs(frame)

f = lambda x:x.max() - x.min()
frame.apply(f)
# <출력>
# b    1.394034
# d    5.250581
# e    2.374144
# dtype: float64

# axis=1 열방향(좌>우)로 추출 == axis='columns'
frame.apply(f,axis='columns')
# <출력> Utah      1.124004
# Ohio      2.888067
# Texas     2.208767
# Oregon    4.270171
# dtype: float64



# 소수점 2로 적용 > 적용은 컬럼 위주로
format = lambda x : '%2f' % x
frame.applymap(format)
# <출력>
#                b          d          e
# Utah    0.274992   0.228913   1.352917
# Ohio    0.886429  -2.001637  -0.371843
# Texas   1.669025  -0.438570  -0.539741
# Oregon  0.476985   3.248944  -1.021228

frame['e'].map(format)
# <출력>
# Utah       1.352917
# Ohio      -0.371843
# Texas     -0.539741
# Oregon    -1.021228
# Name: e, dtype: object




# axis=1 열방향(좌>우)
# axis=0 행방향 (위>아래)로 추출
#axis 연산을 수행할 축, DataFrame 에서 0 은 로우고 1 은 컬럼






# sort                             sort
obj = pd.Series(range(4),index=['d','a','b','c'])
obj.sort_index()
# <출력>
# a    1
# b    2
# c    3
# d    0
# dtype: int64

# 로우 컬럼 축 기준으로 정렬
frame=pd.DataFrame(np.arange(8).reshape((2,4)),
                   index=['three','one'],columns=['d','a','b','c'])
frame
# <출력>
#        d  a  b  c
# three  0  1  2  3
# one    4  5  6  7

frame.sort_index

# 행방향 (위>아래)로 추출
frame.sort_index(axis=0)
# <출력>
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3

# 열방향 (좌>우)
frame.sort_index(axis=1)
# <출력>
#        a  b  c  d
# three  1  2  3  0
# one    5  6  7  4

# 내림차순으로 정렬
frame.sort_index(axis=1,ascending=False)
# <출력>
#        d  c  b  a
# three  0  3  2  1
# one    4  7  6  5



# 객체 정렬 _ sort_values 사용
obj = pd.Series([4, 7, -3, 2])
obj.sort_values()
# <출력>
# 2   -3
# 3    2
# 0    4
# 1    7
# dtype: int64


# 비어있는값은 정렬시 맨뒤로
obj = pd.Series([4,np.nan,7,np.nan,-3,2])
obj.sort_values()
# <출력>
# 4   -3.0
# 5    2.0
# 0    4.0
# 2    7.0
# 1    NaN
# 3    NaN
# dtype: float64



# 하나이상의 컬럼에 있는 값으로 정렬
frame = pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
frame
# <출력>
#    b  a
# 0  4  0
# 1  7  1
# 2 -3  0
# 3  2  1

#인덱스와 b값이 함께 움직여서 변경
frame.sort_values(by='b')
# <출력>
#    b  a
# 2 -3  0
# 3  2  1
# 0  4  0
# 1  7  1


# 여러개의 컬럼 정렬 > 컬럼 이름 담긴 리스트 사용
frame.sort_values(by=['a','b'])
# <출력>
#    b  a
# 2 -3  0
# 0  4  0
# 3  2  1
# 1  7  1

# rank
obj= pd.Series([7,-5,7,4,2,0,4])
obj
# <출력>
# 0    7
# 1   -5
# 2    7
# 3    4
# 4    2
# 5    0
# 6    4
# dtype: int64


# 객체의 평균값이 나오는게 아니라 순위의 평균값
# 4등이 두개 있으면 4.5 7등이 두개있으면 6.5
obj.rank()
# 0    6.5
# 1    1.0
# 2    6.5
# 3    4.5
# 4    3.0
# 5    2.0
# 6    4.5
# dtype: float64

obj.rank(method='first')
# <출력>
# 0    6.0
# 1    1.0
# 2    7.0
# 3    4.0
# 4    3.0
# 5    2.0
# 6    5.0
# dtype: float64

#내림차순 순위 정렬 obj.rank(ascending=False)
obj.rank(ascending=False, method='max')
# <출력>
# 0    2.0
# 1    7.0
# 2    2.0
# 3    4.0
# 4    5.0
# 5    6.0
# 6    4.0
# dtype: float64


# 데이터 프레임 에서는 로우나 컬럼에 대해 순위 결정
frame = pd.DataFrame({'b': [4.3, 7, -3, 2],
                      'a': [0, 1, 0, 1],
                      'c': [-2, 5, 8, -2.5]})
frame
# <출력>
#      b  a    c
# 0  4.3  0 -2.0
# 1  7.0  1  5.0
# 2 -3.0  0  8.0
# 3  2.0  1 -2.5

frame.rank(axis='columns')
# <출력>
#       b    a    c
# 0  3.0  2.0  1.0
# 1  3.0  1.0  2.0
# 2  1.0  2.0  3.0
# 3  3.0  2.0  1.0




# 판다스 ; 중복색인 허용
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
obj
# <출력>
# a    0
# a    1
# b    2
# b    3
# c    4
# dtype: int64

# 유일하지 않고 중복된 값이 있으면 False
obj.index.is_unique
# <출력>False


# 중복색인이여도 로우 선택 가능
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
df
# <출력>
#           0         1         2
# a -1.265934  0.119827 -1.063512
# a  0.332883 -2.359419 -0.199543
# b -1.541996 -0.970736 -1.307030
# b  0.286350  0.377984 -0.753887

df.loc['b']
# <출력>
#           0         1         2
# b -1.541996 -0.970736 -1.307030
# b  0.286350  0.377984 -0.753887





# 수학 메서드 통계 메서드 갖고있음
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
df
# <출력>
#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3



df.sum()
# <출력>
# one    9.25
# two   -5.80
# dtype: float64

df.sum(axis='columns')
# <출력>
# a    1.40
# b    2.60
# c    0.00
# d   -0.55
# dtype: float64

df.mean(axis='columns',skipna=False)
# <출력>
# a      NaN
# b    1.300
# c      NaN
# d   -0.275
# dtype: float64



#skipna ; 누락된 값을 제외할 것인지 정하는 옵션, default 는 True



# argmin, argmax 최소값, 최대값을 가지는 색인의 위치(정수)
# idxmin, idxmax 최소값, 최대값을 가지는 색인의 값
df.idxmin()
# <출력>
# one    d
# two    b
# dtype: object

df.idxmax()
# <출력>
# one    b
# two    d
# dtype: object


# ★ describe 요약통계  ; 여러개의 통계 결과 반환
df.describe()
# <출력>
#             one       two
# count  3.000000  2.000000
# mean   3.083333 -2.900000
# std    3.493685  2.262742
# min    0.750000 -4.500000
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000

# 수치 데이터가 아닐경우는 다른 요약 통계 생성
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()
# <출력>
# count     16
# unique     3
# top        a
# freq       8
# dtype: object




#
# pandas_datareader 패키지 이용
# conda install pandas-datareader
# pip install pandas-datareader
# 판다스 데이터프레임 안에 넘파이에의한 랜덤난수
import pandas as pd
import numpy as np


price = pd.read_pickle('yahoo_price.pkl')
volume = pd.read_pickle('yahoo_volume.pkl')


# 주가정보
import pandas_datareader.data as web
all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

#주식 퍼센트 변화율 계산
returns = price.pct_change()
returns.tail()


# corr 상관관계 / cov 공분산
returns['MSFT'].corr(returns['IBM'])
returns['MSFT'].cov(returns['IBM'])



#
returns.MSFT.corr(returns.IBM)
returns.corr()
returns.cov()

returns.corrwith(returns.IBM)
returns.corrwith(volume)



# Unique Values, Value Counts, and Membership
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
uniques


#정렬
obj.value_counts()
#내림차순정렬
pd.value_counts(obj.values, sort=False)


# 존재하는지 확인
obj
mask = obj.isin(['b', 'c'])
mask
obj[mask]


# 여러값이 들어있는 배열에 유일한 색인값 구하기
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
pd.Index(unique_vals).get_indexer(to_match)




# 히스토그램
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
 'Qu2': [2, 3, 1, 2, 3],
 'Qu3': [1, 5, 2, 4, 4]})
data
result = data.apply(pd.value_counts).fillna(0)
result















