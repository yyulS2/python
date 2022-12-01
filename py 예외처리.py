


# 예외처리



#
print('\n유형별 예외처리')
try :
    div = 1000/2.53
    print('div=%5.2f'%(div)  )        #정상
    div = 1000 / 0                   #1차 산술적예외
    f=open ('c:\\test/txt')          #2차 파일열기
    num = int(input('숫자입력:'))      #3차 기타예외
    print('num=',num)
except Exception as e :       # 다중예외처리 x -> "except Exception as e " 하나만 넣어도 오류가 어디서 발생 되었는지 확인 가능
    print('오류정보:',e)       #except Exception as e ::: 예외의 유형을 판단 할 수 없는 경우 사용할 수 있는 클래스
finally :
    print('finally 영역-항상 실행되는 영역')

# 유형별 예외처리
# div=395.26
# 오류정보: division by zero
# finally 영역-항상 실행되는 영역


print('\n유형별 예외처리')
try:
    div = 1000 / 2.53
    print('div=%5.2f' % (div))
    div = 1000 / 0                     # 1차 산술적예외
    f = open('c:\\test/txt')           # 2차 파일열기
    num = int(input('숫자입력:'))       # 3차 기타예외
    print('num=', num)
except ZeroDivisionError as e:         # 다중예외처리
    print('오류정보:', e)
except FileNotFoundError as e:         # 다중예외처리
    print('오류정보:', e)
except Exception as e:
    print('오류정보:', e)
finally:
    print('finally 영역-항상 실행되는 영역')

# <출력>
# 유형별 예외처리
# div=395.26
# 오류정보: division by zero
# finally 영역-항상 실행되는 영역






# 파일 입출력

import os
print('\n현재경로:',os.getcwd())    # 현재경로확인

try:
    ftest1 = open('ch8_data/data/ftest.txt',mode = 'r')        # 파일읽기
    print(ftest1.read())

    ftest2 = open('ch8_data/data/ftest2.txt',mode='w')         # 파일 쓰기
    ftest2.write('my first text~~')

    ftest3 = open('ch8_data/data/test2.txt',mode='a')          # 파일 쓰기 + 내용추가
    ftest2.write('\nmy second text~~')
except Exception as e :
    print('Error 발생:',e)
finally:
    ftest1.close()                 # 파일 객체 닫기
    ftest2.close()
    ftest3.close()

# <출력>
# programming is fun
# very fun!
# have a good time
# mouse is input device
# keyboard is input device
# computer is input output system





# 파일자료 읽기

try :
    ftest = open('ch8_data/data/ftest.txt',mode = 'r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    ftest =open('ch8_data/data/ftest.txt',mode = 'r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단수 :',len(lines))

    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)

    ftest = open('ch8_data/data/ftest.txt',mode='r')
    line = ftest.readlines()
    print(line)
    print(type(line))

except Exception as e:
    print('Error 발생:',e)

finally:
    ftest.close()





# os 모듈 파일 디렉터리 관련함수

import os

# 디렉터리확인
print(os.getcwd())

# 디렉터리 변경
os.chdir('ch8_data')
print(os.getcwd())

# 디렉터리 목록 list 반환
os.listdir('.')
# <출력> ['data', 'images', 'images2', 'txt_data']


# 'text' 생성
os.mkdir('text')
print(os.listdir('.'))
# <출력> ['data', 'images', 'images2', 'test', 'text', 'txt_data']


# 'text' 이동
os.chdir('text')
print(os.getcwd())


# 여러 디렉터리 생성
os.makedirs('test2/test3')
print(os.listdir('.'))
# <출력> ['data', 'images', 'images2', 'test','test2','test3' , 'txt_data']


# test3 이동
os.chdir('test3')
print(os.listdir('.'))
# <출력> ['data', 'images', 'images2', 'test','test2','txt_data']


# test3 삭제
os.rmdir('test3')
print(os.listdir('.'))
# <출력> ['data', 'images', 'images2', 'test','test2','txt_data']


# 상위 디렉터리 2개 이동
os.chdir('../..')
os.getcwd()


# 여러 디렉터리 삭제
os.removedirs('test/test2')






import os.path

os.getcwd()           #'C:\\Users\\xxxx\\PycharmProjects\\pythonProject3'
os.chdir('ch8_data')
os.getcwd()           #'C:\\Users\\xxxx\\PycharmProjects\\pythonProject3\\ch8_data'

# 파일 절대경로
os.path.abspath('txt_data/second')


# 디렉터리 이름
os.path.dirname('txt_data/second')
# <출력> 'txt_data'


# pythonProject3 디렉터리 유무확인
os.path.exists('C:\\Users\\xxxx\\PycharmProjects\\pythonProject3')
# <출력> True


# 파일 유무확인
os.path.isfile('txt_data/second')
# <출력> False


# 디렉터리 유무확인
os.path.isdir
# <출력> <function isdir at 0x00000251A5D5B430>






import glob
glob.glob('data*.py')
# <출력> []









import os
print(os.getcwd())                               # 기본작업 디렉터리 C:\Users\tj-bu\PycharmProjects\pythonProject3
txt_data = 'ch8_data/txt_data/'                  # 상대경로 지정

sub_dir = os.listdir(txt_data)                   # txt_data 목록반한
print(sub_dir)                                   # <출력> ['first', 'second']

def textPro(sub_dir) :                           # 각 디렉터리 텍스트 자료 수집
    first_txt = []                               #디렉터리 텍스트 저장
    second_txt = []
    for sdir in sub_dir :                        #디렉터리 구성
        dirname = txt_data + '/' + sdir
        file_list = os.listdir(dirname)          #파일목록반환

        for fname in file_list :
            file_path = dirname + '/' + fname

            if os.path.isfile(file_path) :
                try:
                    file = open(file_path, 'r')
                    if sdir == 'first' :
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외발생:',e)
                finally:
                    file.close()
    return first_txt ,second_txt
first_txt,second_txt = textPro(sub_dir)

print('first_tex 길이 =', len(first_txt))
print('second_tex 길이 =', len(second_txt))

# 자료 결합
tot_texts = first_txt + second_txt
print('tot_texts 길이 =', len(tot_texts))

print(tot_texts)
print(type(tot_texts))







## pickle

import pickle
#pfile_w = open("ch8_data/data/tot_texts.pck", mode = 'wb')    #파일명 저장 이진파일 형식으로 쓰기용 파일객체 생성


pfile_r = open("ch8_data/data/tot_texts.pck", mode = 'rb')    #파일명 저장 이진파일 형식으로 읽기용 파일객체 생성
tot_texts_read = pickle.load(pfile_r)
print('tot_texts 길이 =', len(tot_texts_read))
print(type(tot_texts_read))





# 이미지 파일 이동

import os
from glob import glob

# 이미지 파일경로
print(os.getcwd())
img_path = 'ch8_data/images/'                        # 이미지 원본
img_path2 = 'ch8_data/images2/'                      # 이미지 이동

# 디렉터리 존재유무
if os.path.exists(img_path) :
    print("해당 디렉터리가 존재함")

    images = []                                      # 파일저장
    os.mkdir(img_path2)                              # 이미지 이동 디렉터리 생성

    # 이미지 디렉터리 에서 png 검색
    for pic_path in glob(img_path + '*.png') :

        img_path = os.path.split(pic_path)           # 파일명 경로 분리
        images.append(img_path[1])                   # 파일명 추가


        #이진파일 읽기
        rfile = open(file = pic_path, mode = 'rb')
        output = rfile.read()

        #이진파일 쓰기
        wfile = open(img_path2 + img_path[1], mode = 'wb')
        wfile.write(output)

    rfile.close()
    wfile.close()                                    # 파일 객체 닫기
else :
    print("해당 디렉터리가 없음")
print('png file =',images)





# cvs _ excel _ file
import pandas as pd
import os
print(os.getcwd())

score = pd.read_csv("ch8_data/data/score.csv")
print(score.info())
print(score.head())

kor = score.kor
eng = score['eng']
mat = score['mat']
dept = score['dept']

print('max kor=', max(kor))
print('max eng=', max(eng))
print('max mat=', max(mat))

print('min kor=', max(kor))
print('min eng=', max(eng))
print('min mat=', max(mat))

from statistics import mean
print('국어 점수 평균 :',round(mean(kor),3))
print('영어 점수 평균 :',round(mean(eng),3))
print('수학 점수 평균 :',round(mean(mat),3))

dept_count = {}

for key in dept:
    dept_count[key] = dept_count.get(key,0)+1

print(dept_count)








