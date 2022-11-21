## 08/29 while
## 1~100사이에서 5의 배수이면서 3의 배수가 아닌 수의 합 계산하기

cnt = 0
tot = 0


while cnt < 100:
    cnt += 1
    if cnt % 5 == 0 and cnt % 3 !=0 :
        tot += cnt

print(tot)



# Q. -1, 3, -5, 7, -9, ... 99 까지의 합을 구하시오.

cnt = cnt2 = cnt3 = tot = 0
dataset = []
while cnt < 100:
    cnt += 1
    if (cnt % 2) != 0:
        cnt2 += 1
        if (cnt2 % 2) != 0:
            cnt3 = cnt*(-1)
            tot += cnt3
            dataset.append(cnt3)
        else:
            tot += cnt
            dataset.append(cnt)

print('-1, 3, -5, 7, -9 ~ 99까지의 합 = %d' % tot)
print('dataset =', dataset)



# Q. -1, 3, -5, 7, -9, ... 99 까지의 합을 구하시오.

num = -1
tot = 0

while num < 100 :
    num += 1
    tot += num
    if num % 4 == 1:
        tot -= num*2
    if num % 2 == 0:
        tot -= num

print(tot)





# Q. -1, 3, -5, 7, -9, ... 99 까지의 합을 구하시오.

cnt = tot = 0

while cnt < 100:
    cnt += 1
    if cnt % 4 == 3:
        tot += cnt
    elif cnt % 4 == 1:
        tot -= cnt

print(tot)

















