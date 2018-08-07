import numpy as np
import math
knum = 2
t = 1000
tau = 0.1


def reward(kp):
    if kp == 1:
        if np.random.rand() <= 0.4:
            return int(1)
        else:
            return int(0)
    elif kp == 2:
        if np.random.rand() <= 0.2:
            return int(1)
        else:
            return int(0)



r = 0
q = np.array([0, 0])
count = np.array([0, 0])
for i in range(t):
    pro = 0
    for j in range(knum):
        pro = pro+math.exp(q[j]/tau)
    epsilon = math.exp(q[0]/tau)/pro
    if np.random.rand() < epsilon:
        k = 1
    else:
        k = 2

    v = reward(k)
    r = r+v
    q[k-1] = (q[k-1]*count[k-1]+v)/(count[k-1]+1)
    count[k-1] = count[k-1]+1

print(r/t)
