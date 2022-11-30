
# 문1)
# <emil 양식 처리조건>
# 아이디 : 첫자 영문소문자, 단어길이 4자이상
# 호스트이름 : 영문소문자 시작, 단어길이 3자이상
# 최상위 도메인 : 영문소문자 3자리 이하
# 정규표현식 기본패턴 : '메타문자@메타문자.메타문자'

email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

from re import findall, match
for e in email.split(sep='\n') :
    result = match('^[a-z]\\w{3,}@[a-z\\w{2,}.[a-z]\\w{2,}',e)
    if result :
        print(e)

# <출력>
# you2@naver.com
# kimjs@gmail.com





# 문2)
# emp 변수를 이용하여 사원의 이름만 추출
# names = ['홍길동','이순신','유관순']

from re import findall,sub
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

def name_pro(emp):
    emp_re=sub('[0-9]','',emp)
    emp_re2 = ' '.join(emp_re.split())
    return emp_re2

names = [name_pro(emp) for emp in emp]
print('names=',names)
# <출력> names= ['홍길동', '이순신', '유관순']

# 문3)
# '입사년도이름급여'순 => emp 변수를 이용하여 사원의 이름만 추출
# < 전체 사원 급여 평균 : 260 >

from re import findall,sub
from statistics import mean
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

def pay_pro(emp):
        emp_re = sub('[가-힣]','',emp)
        emp_re2 = sub('[0-9]{4}','',emp_re)
        return emp_re2

pays_mean = [int(pay_pro(emp))for emp in emp]
avg = mean(pays_mean)
print('전체 사원의 급여 평균:', avg)

# <출력> 전체 사원의 급여 평균: 260


# 문4)
# '입사년도이름급여'순 => emp 변수를 이용하여 사원의 이름만 추출
# <출력>
# 전체 급여 평균 : 260
# 평균 이상 급여 수령자
# 이순신 => 300
# 유관순 => 260



from re import findall,sub
from statistics import mean
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]
import re
name = [re.findall('[가-힣]{3}',a)for a in emp]
name2 = [a[0]for a in name]

def pay_pro(emp):
        emp_re = sub('[가-힣]','',emp)
        emp_re2 = sub('[0-9]{4}','',emp_re)
        return emp_re2

pays_mean = [int(pay_pro(emp))for emp in emp]
avg = mean(pays_mean)
print('전체 사원의 급여 평균:', avg)
print('평균이상급여수령자')
for a in range(len(emp)):
    if  pays_mean[a] >= avg :
        print(name2[a],'=>', pays_mean[a])

# <출력>
# 전체 사원의 급여 평균: 260
# 평균이상급여수령자
# 이순신 => 300
# 유관순 => 260


# 문5)
# ['afabasabag','abttaa','uysfsfaa']

from re import findall, sub
texts = ['AFAB54747,asabag?','abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

def clean(text) :
    text_re1 = text.lower()
    text_re2 = sub('[0-9]','',text_re1)
    text_re3 = sub('[,.?!:;]','',text_re2)
    text_re4 = sub('[@#$%^&*()]','',text_re3)
    text_re5 = ''.join(text_re4.split())
    return text_re5
texts_result=[clean(text) for text in texts]
print(texts_result)

# <출력> ['afabasabag', 'abttaa', 'uysfsfaa']

