
### 7-2
import re

data = """
park 800905-1049118
kim 700905-1059119
"""

pat=re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))
# <출력>
# park 800905-*******
# kim 700905-*******



# dot(.) = \n을 제외한 모든 문자와 매치됨
#a[.]b "a.b" 매치되고 "a0b"와는 매치 안됨


#ca{2,5}t = >"c+a(2~5회 반복)+t"

#ab?c = > a+b(있어도 되고 없어도 됨)+c


import re
p=re.compile('[a-z]+')

m= p.match("python")
print(m)
# <출력> <re.Match object; span=(0, 6), match='python'>

import re
p=re.compile('[a-z]+')
m= p.match("3 python")
print(m)
# <출력> None


from re import split,match,compile
import re
p= re.compile['a-z]+']
m = p.match('string goes here')
if m:
    print('match found:',m.group())
else:
    print('no match')

import re
p= re.compile

m = p.search("3 python")
print(m)




p=re.compile('[a-z]+')
m=p.match("python")

m=re.match('[a-z]+',"python")






### 7-3
#메타문자

# |
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)

# <출력> <re.Match object; span=(0, 4), match='Crow'>

# ^
print(re.search('^Life', 'Life is too short'))
# <출력> <re.Match object; span=(0, 4), match='Life'>

print(re.search('^Life', 'My Life'))
# <출력> None

# $
print(re.search('short$', 'Life is too short'))
# <출력> <re.Match object; span=(12, 17), match='short'>

print(re.search('short$', 'Life is too short, you need python'))
# <출력> None

# \A : 문자열의 처음과 매치됨

# \Z : 문자열의 끝과 매치됨


# \b : 단어 구분자
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
# <출력> <re.Match object; span=(3, 8), match='class'>



# \B : 단어가 아닌경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
# <출력> None

print(p.search('the declassified algorithm'))
# <출력><re.Match object; span=(6, 11), match='class'>

print(p.search('one subclass is'))
# <출력> None




# 그루핑 :

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')

print(m)
# <출력> <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())
# <출력> ABCABCABC


p = re.compile(r"(\w)+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

# <출력> park


p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

# <출력> 010-1234-1234

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

# <출력> 010

p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring').group()
print(m)     #the the







# 문자열 바꾸기
p = re.compile('(blue|white|red)')
r=p.sub('colour', 'blue socks and red shoes')
print(r)

# <출력> colour socks and colour shoes

p = re.compile('(blue|white|red)')
y=p.sub('colour', 'blue socks and red shoes', count=1)
print(y)

# <출력>  colour socks and red shoes





# 이름 + 전화번호의 문자열을 전화번호 + 이름으로 바꾸는 예
# sub의 바꿀 문자열 부분에 \g<그룹이름>을 사용하면 정규식의 그룹 이름을 참조
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))

# <출력> 010-1234-1234 park





# 메서드 매게변수
def hexrepl(match):              # 16진수로 변환하여 돌려주는 함수
    value = int(match.group())
    return hex(value)            #정규식과 매치된 match 객체가 입력

p = re.compile(r'\d+')
z=p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(z)
# <출력> Call 0xffd2 for printing, 0xc000 for user code.




###
s = '<html><head><title>Title</title>'
len(s)
print(re.match('<.*">',s).span())
print(re.match('<.*>',s).group())