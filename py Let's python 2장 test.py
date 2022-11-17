## 56~57pg

#1 수량,단가변수 > 금액출력____틀
su=5   #su
dan=800    #dan

print(id(su))
print(id(dan))

#오답
su=5   #su
dan=800    #dan
price = su*dan

print('su주소 : ', id(su))
print('dan주소 : ',id(dan))
print('금액 : ', price)



#2   ___ 틀
x=2
y=2.5*x**2+3.3*x+6
print('2차방정식결과=',y)




#3 칼로리합계 계산 ___ 맞

num1=int(input("지방의 그램을 입력하세요 : "))
num2=int(input("탄수화물의 그램을 입력하세요 : "))
num3=int(input("단백질의 그램을 입력하세요 : "))

cal=num1*9+num2*4+num3*4
print("총칼로리 : ", format(num1*9+num2*4+num3*4,"3,d"),"cal")



#4_____맞긴한데 너무 복잡. 간단히 하는법
word1 = "Korea"
word2 = "Baseball"
word3 = "Orag"

var1=(word1,word2,word3)

print("첫번째단어 :",word1)
print("두번째단어 :",word2)
print("세번째단어 :",word3)

print("="*17)

word1[0]
word2[0]
word3[0]

abbr = word1[0]+word2[0]+word3[0]   ##틀) abbr= 으로 못묶음


print("약자: " , abbr)


#4-2  ___변형문제 ___
word4 = "Victory"

word1[3]
word2[-1]   #대문자로변경


word3[0]
word4[0]   #소문자로변경


word[-1].upper()+word4[0].lower()+word3[0]+word1[3]



##간단히 하기
word1 = "Korea"
word2 = "Baseball"
word3 = "Orag"
print("첫번째단어 :",word1)
print("두번째단어 :",word2)
print("세번째단어 :",word3)

print("="*17)
word1[0]
word2[0]
word3[0]

abbr = word1[0]+word2[0]+word3[0]
print("약자: " , abbr)

#4-2
word1 = "Korea"
word2 = "Baseball"
word3 = "Orag"
word4 = "Victory"
word1[3]
word2[-1]
word3[0]
word4[0]

word2[-1].upper()+word3[0].lower()+word4[0].lower()+word1[3]