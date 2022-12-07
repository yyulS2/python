
####################################################################

# data_loading_n_storage_part
# pandas_dataset2/파일 경로 설정

import pandas as pd
import numpy as np


df = pd.read_csv('pandas_dataset2/ex1.csv')
df
# <출력>
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo



# 구분자 => ,
pd.read_table('pandas_dataset2/ex1.csv', sep=',')
# <출력>
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo

# type examples/ex2.csv
pd.read_csv('pandas_dataset2/ex2.csv', header=None)
# <출력>
#    0   1   2   3      4
# 0  1   2   3   4  hello
# 1  5   6   7   8  world
# 2  9  10  11  12    foo

# 컬럼명 지정
pd.read_csv('pandas_dataset2/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
# <출력>
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo



# message 컬럼을 색인으로 하는 DAtaFrame 을 반환하려면 index_col 인자에 4 번째 컬럼
# 또는 'message'이름을 가진 컬럼을 지정하여 색인으로 만듦
names = ['a', 'b', 'c', 'd', 'message']
pd.read_csv('pandas_dataset2/ex2.csv', names=names, index_col='message')
# <출력>
#          a   b   c   d
# message
# hello    1   2   3   4
# world    5   6   7   8
# foo      9  10  11  12


# type examples/csv_mindex.csv
# 계층적 색인 지정 시 컬럼 번호나 이름의 리스트를 넘긴다.
parsed = pd.read_csv('pandas_dataset2/csv_mindex.csv', index_col=['key1', 'key2'])
parsed
# <출력>
#            value1  value2
# key1 key2
# one  a          1       2
#      b          3       4
#      c          5       6
#      d          7       8
# two  a          9      10
#      b         11      12
#      c         13      14
#      d         15      16

# 구분자 없이 공백이나 다른 패턴으로 필드를 구분
list(open('pandas_dataset2/ex3.txt'))
# <출력>['            A         B         C\n',
# 'aaa -0.264438 -1.026059 -0.619500\n',
# 'bbb  0.927272  0.302904 -0.032399\n',
# 'ccc -0.264273 -0.386314 -0.217601\n',
# 'ddd -0.871858 -0.348382  1.100491\n']


# \s = 스페이스 , \s+ =>한개이상반복
result = pd.read_table('pandas_dataset2/ex3.txt', sep='\s+')
result
# <출력>
#             A         B         C
# aaa -0.264438 -1.026059 -0.619500
# bbb  0.927272  0.302904 -0.032399
# ccc -0.264273 -0.386314 -0.217601
# ddd -0.871858 -0.348382  1.100491

# skiprows 를 이용하여 첫번째, 세번째, 네번째 로우를 건너뛴다.
pd.read_csv('pandas_dataset2/ex4.csv', skiprows=[0, 2, 3])
# <출력>
#    a   b   c   d message
# 0  1   2   3   4   hello
# 1  5   6   7   8   world
# 2  9  10  11  12     foo


# 텍스트파일에서 누락된 값은 표기되지 않거나(비어 있는 문자열) => NA, NULL
result = pd.read_csv('pandas_dataset2/ex5.csv')
result
# <출력>
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo

pd.isnull(result)
# <출력>
#    something      a      b      c      d  message
# 0      False  False  False  False  False     True
# 1      False  False  False   True  False    False
# 2      False  False  False  False  False    False




# na_values 옵션은 리스트나 문자열 집합을 받아서 누락된 값 처리
result = pd.read_csv('pandas_dataset2/ex5.csv', na_values=['NULL'])
result
# <출력>
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo

# 컬럼마다 다른 NA 문자를 사전값으로 넘겨서 처리
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('pandas_dataset2/ex5.csv', na_values=sentinels)
# <출력>
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       NaN  5   6   NaN   8   world
# 2     three  9  10  11.0  12     NaN




# 큰 파일을 다루기 전에 pandas 의 출력 설정
pd.options.display.max_rows = 10 # 최대 10 개의 데이터 출력
# 쓰고서 풀어줄땐 '=None' 해주기
# <출력>

result = pd.read_csv('pandas_dataset2/ex6.csv')
result
# <출력>

# 처음 몇줄만 읽을 때 ; nrows
pd.read_csv('pandas_dataset2/ex6.csv', nrows=5)
# <출력>
#         one       two     three      four key
# 0  0.467976 -0.038649 -0.295344 -1.824726   L
# 1 -0.358893  1.404453  0.704965 -0.200638   B
# 2 -0.501840  0.659254 -0.421691 -0.057688   G
# 3  0.204886  1.074134  1.388361 -0.982404   R
# 4  0.354628 -0.133116  0.283763 -0.837063   Q

# 파일을 여러 조각으로 나누어서 읽고 싶다면 chunksize 옵션으로 로우 개수 설정
chunker = pd.read_csv('pandas_dataset2/ex6.csv', chunksize=1000)
 # 담는거라 display 되는건 없다
 # 아래에서 하나씩 빼서 쓰려고 만든것
# <출력>

# 예로 ex6.csv 파일을 순회하면서 'key'로우에 있는 값을 세어보려면 다음과 같이 한다.
chunker = pd.read_csv('pandas_dataset2/ex6.csv', chunksize=1000)
tot = pd.Series([])
for piece in chunker:
 tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
tot[:10]

# <출력>




# write                         write

# 데이터를 구분자로 구분한 형식으로 내보내기
data = pd.read_csv('pandas_dataset2/ex5.csv')
data
# <출력>
#   something  a   b     c   d message
# 0       one  1   2   3.0   4     NaN
# 1       two  5   6   NaN   8   world
# 2     three  9  10  11.0  12     foo
# data.to_csv('out.csv')
data.to_csv('out.csv')






import sys
data.to_csv(sys.stdout, sep='|')
# <출력>
# |something|a|b|c|d|message
# 0|one|1|2|3.0|4|
# 1|two|5|6||8|world
# 2|three|9|10|11.0|12|foo

# 누락된 값 > 원하는 값
data.to_csv(sys.stdout, na_rep='NULL')
# <출력>
# ,something,a,b,c,d,message
# 0,one,1,2,3.0,4,NULL
# 1,two,5,6,NULL,8,world
# 2,three,9,10,11.0,12,foo

# 옵션명시x => 로우와 컬럼 기록
# 로우와 컬럼 이름을 포함하지 않을 경우
data.to_csv(sys.stdout, index=False, header=False)
# <출력>
# one,1,2,3.0,4,
# two,5,6,,8,world
# three,9,10,11.0,12,foo

# 컬럼의 일부분만 기록, 순서 지정
data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
# <출력>
# a,b,c
# 1,2,3.0
# 5,6,
# 9,10,11.0

# to_csv 메서드
dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('tseries.csv')








import pandas as pd
import numpy as np

# pandas_read_table() 함수를 이용하여 대부분의 파일 형식을 불러 올 수 있다.
# csv 파일을 불러오는 경우
import csv
f = open('pandas_dataset2/ex7.csv')
reader = csv.reader(f)
f
# <출력>
# <_io.TextIOWrapper name='pandas_dataset2/ex7.csv' mode='r' encoding='cp949'>

# 큰 따옴표가 제거된 튜플
for line in reader:
 print(line)
# <출력>
# ['a', 'b', 'c']
# ['1', '2', '3']
# ['1', '2', '3']


# 원하는 형태 저장
# 파일을 읽어 줄 단위 리스트로 저장
with open('pandas_dataset2/ex7.csv') as f: lines = list(csv.reader(f))
# lines 에 리스트로 요소별로 담기



# 헤더와 데이터 구분
header, values = lines[0], lines[1:]
# ['a', 'b', 'c']
# [['1', '2', '3'], ['1', '2', '3']]


# 전치해주는 zip(*values)이용 데이터 컬럼 사전
data_dict = {h: v for h, v in zip(header, zip(*values))}
data_dict

# <출력>
# {'a': ('1', '1'), 'b': ('2', '2'), 'c': ('3', '3')}
# head 를 키로 놓고 dic




# csv 파일 > 구분자, 문자열을 둘러싸는 방법, 개행 문자 >> csv.Dialect 를 상속받아 새로운 클래스를 정의해서 해결
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


# reader = csv.reader(f, dialect=my_dialect)
reader = csv.reader('pandas_dataset2/ex7.csv', dialect=my_dialect)


# 서브클래스를 정의하지 않고 csv.readr 에 키워드 인자로 각각의 csv 파일의 특징을 지정해서 전달해도 된다.
# reader = csv.reader(f, delimiter='|')
reader = csv.reader('pandas_dataset2/ex7.csv', delimiter='|')




with open('mydata.csv', 'w') as f:
 writer = csv.writer(f, dialect=my_dialect)
 writer.writerow(('one', 'two', 'three'))
 writer.writerow(('1', '2', '3'))
 writer.writerow(('4', '5', '6'))
 writer.writerow(('7', '8', '9'))


pd.options.display.max_rows = None





