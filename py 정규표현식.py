


# findall
#
import re             # 모듈추가 방법1 # 모듈추가 방법2
from re import findall   # 모듈추가

st1 = '123456 abc훈민정음 ABC_555_6 세종대왕'

# 숫자 찾기
print(findall('1234',st1))       # <출력> ['1234']
print(findall('[0-9]',st1))      # <출력> ['1', '2', '3', '4', '5', '6', '5', '5', '5', '6']
print(findall('[0-9]{3}',st1))   # <출력> ['123', '456', '555']
print(findall('[0-9]{3,}',st1)   # <출력> ['123456', '555']
print(findall('\\d{3,}',st1))    # <출력> ['123456', '555']

# 문자열 찾기
print(findall('[가-힣]{2,}',st1))    # <출력> ['훈민정음', '세종대왕']
print(findall('[a-b]{2,}',st1))     # <출력> ['ab']
print(findall('[a-z|A-Z]{3}',st1))  # <출력> ['abc', 'ABC']




#특정위치 문자열

st2 = 'test12abcABC 123mbc 456test'

#접두어/접미어
print(findall('^test',st2))       # <출력> ['test']
print(findall('st$',st2))         # <출력> ['st']

#종료문자
print(findall('.bc',st2))         # <출력> ['abc', 'mbc']

#시작문자
print(findall('t.',st2))          # <출력> ['te', 't1', 'te']




#단어찾기
from re import findall            # 모듈추가
st3 = 'test^훈민정음 abc 세종*대왕 123$sbc'

words = findall('\\w{3,}',st3)
print(words)
# <출력> ['test', '훈민정음', 'abc', '123', 'sbc']

findall ('[^t]',st3)
# <출력> ['e', 's', '^', '훈', '민', '정', '음', ' ', 'a', 'b', 'c', ' ', '세', '종', '*', '대', '왕', ' ', '1', '2', '3', '$', 's', 'b', 'c']

findall ('[^t]+',st3)
# <출력> ['es', '^훈민정음 abc 세종*대왕 123$sbc']

#문자열제외
from re import findall            # 모듈추가
st3 = 'test^훈민정음 abc 세종*대왕 123$sbc'
print(findall('[^^*$]+',st3))
# <출력> ['test', '훈민정음 abc 세종', '대왕 123', 'sbc']




#문자열 검사 match

from re import match               # 모듈추가

juminnum = '123456-7890123'
result = match('[0-9]{6}-[1-4][0-9]{6}',juminnum)
print(result)

if result :
    print("주민번호 일치")
else :
    print("주민번호 확인요함")


#패턴 불일치

from re import match               # 모듈추가

juminnum = '123567-4890123'
result = match('[0-9]{6}-[1-4][2-5][0-9]{6}',juminnum)
print(result)       #None

if result :
    print("주민번호 일치")
else :
    print("주민번호 확인요함")




#문자열 치환_sub
from re import sub

st3 = 'test^훈민정음 abc 세종*대왕 123$sbc'

# 특수문자제거
text1=sub('[\^*$]+','',st3)
print(text1)
# <출력> test훈민정음 abc 세종대왕 123sbc

# 숫자제거
text2 = sub('[0-9]','',st3)
print(text2)
# <출력> test^훈민정음 abc 세종*대왕 $sbc





# split _compile
from re import split,match,compile


#텍스트 자료
multi_line = """http://www.naver.com     
http://www.daum.net
www.hong.com."""

web_site = split("\n",multi_line)
print(web_site)
# <출력> ['http://www.naver.com     ', 'http://www.daum.net', 'www.hong.com.']



# 패턴객체
pattern  = compile("http://")

sel_site = [site for site in web_site if match(pattern,site)]
print(sel_site)
# <출력> ['http://www.naver.com     ', 'http://www.daum.net']



# 자연어 전처리  _   preprocessing

from re import findall,sub    # 모듈추가
texts = ['대한민국, 우리나라%$만세','안약 50MG 사용!','코리아사람','택시비 5000원']

# 1 - 소문자변경
texts_rel = [t.lower()for t in texts]
print("texts_rel:",texts_rel)

# <출력> texts_rel: ['대한민국, 우리나라%$만세', '안약 50mg 사용', '코리아사람', '택시비 5000원']

# 2 - 숫자제거
texts_re2 = [sub("[0-9]",'',text) for text in texts_rel]
print('texts_re2 :',texts_re2)

# <출력> texts_re2 : ['대한민국, 우리나라%$만세', '안약 mg 사용', '코리아사람', '택시비 원']

# 4 - 문장부호 제거
texts_re3 = [sub('[,.?!:;]','',text)for text in texts_re2]
print('texts_re3 :',texts_re3)

# <출력> texts_re3 : ['대한민국 우리나라%$만세', '안약 mg 사용', '코리아사람', '택시비 원']

# 5 - 특수문자제거
str = '[@#$%^&*()]'
texts_re4 = [sub(str,'',text) for text in texts_re3]
print('texts_re4 :',texts_re4)

# <출력> texts_re4 : ['대한민국 우리나라만세', '안약 mg 사용', '코리아사람', '택시비 원']

# 6 - 영어제거
texts_re5 = [''.join(findall("[^a-z]",text))for text in texts_re4]
print('texts_re5 :',texts_re5)

# <출력> texts_re5 : ['대한민국 우리나라만세', '안약  사용', '코리아사람', '택시비 원']

#7 - 공백제거
texts_re6 = [' '.join(text.split())for text in texts_re5]
print('texts_re6 :',texts_re6)

# <출력> texts_re6 : ['대한민국 우리나라만세', '안약 사용', '코리아사람', '택시비 원']




# 전처리 함수 _func

from re import findall,sub
texts = ['대한민국, 우리나라%$만세','안약 50MG 사용!','코리아사람','택시비 5000원']
def clean_text(text) :
    texts_re =text.lower()
    texts_re2=sub('[0-9]','',texts_re)
    texts_re3=sub('[,.?!;:]','',texts_re2)
    texts_re4=sub('[@#$%^&*()]','',texts_re3)
    texts_re5=sub('[a-z]','',texts_re4)
    texts_re6=' '.join(texts_re5.split())
    return texts_re6
texts_result = [clean_text(text) for text in texts]
print(texts_result)

# <출력> ['대한민국 우리나라만세', '안약 사용', '코리아사람', '택시비 원']


















