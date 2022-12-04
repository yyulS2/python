#   dot     ; 행렬의 곱셈                        dot
x=np.array([[1.,2.,3.],[4.,5.,6.]])
y=np.array([[6.,23.],[-1,7],[8,9]])

# x.dot(y) == np.dot(x,y)
x.dot(y)
# <출력>
# array([[ 28.,  64.],
#        [ 67., 181.]])

np.dot(x,y)
# <출력>
# array([[ 28.,  64.],
#        [ 67., 181.]])




np.dot(x,np.ones(3))
x @ np.ones(3)
# <출력> array([ 6., 15.])





# np.linalg ; 역행렬
from numpy.linalg import inv,qr
x = np.random.randn(5,5)
x
mat = x.T.dot(x)   #x의 전치행렬과 x의 곱
mat
inv(mat)
mat.dot(inv(mat))
q,r = qr(mat)
q
r



import numpy as np
# Pseudorandom
samples = np.random.normal(size=(4,4))
samples

from random import normalvariate
N=1000000

from datetime import datetime
start = datetime.now()

samples = [normalvariate(0,1)for _ in range(N)]
np.random.normal(size=N)

print(datetime.now() - start)





# np.random.seed: NumPy 에 존재하는 random generator 에 직접 접근하여 난수 생성
np.random.seed(1234)
np.random.uniform(0, 10, 5)
np.random.rand(3,3)

# np.random.RandomState: 난수 생성기라는 object 를 만들어서 접근
rng2 = np.random.RandomState(1234)
rng2.uniform(0, 10, 5)
np.random.rand(3,3)








# 계단 오르내리기 예제
import numpy as np
import matplotlib.pyplot as plt
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)

plt.figure()

# 처음 100회
plt.plot(walk[:100])

#1000번 수행
np.random.seed(12345)

nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws > 0,1,-1)
walk = steps.cumsum            # 누적한 층수

walk.min()
walk.max()

# 10 또는 -10인 시점
(np.abs(walk) >= 10).argmax()






#
# 각 컬럼에서 누적합을 구해서 5,000 회의 시뮬레이션을 한번에 처리
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks
26


# 최대값과 최소값
walks.max()
walks.min()


# 누적합이 30 또는 -30 에 도달하는 최소시점 계산
hits30 = (np.abs(walks) >= 30).any(1)
hits30
hits30.sum() # Number that hit 30 or -30



# 처음 위치에서 30 칸 이상 멀어지는 최소 횟수:
# 컬럼 선택하고 절대값이 30 을 넘는 경우에 대해 축 1 의 argmax 값
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()



# normal 함수 이용
steps = np.random.normal(loc=0, scale=0.25,size=(nwalks, nsteps))
