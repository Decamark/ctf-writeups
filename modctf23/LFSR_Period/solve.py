import numpy as np
from pylfsr import LFSR

# lfsr('01110000000100001001', (20, 15, 11, 1))

state = [0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1]
fpoly = [20,15,11]
L = LFSR(fpoly=fpoly, initstate=state, verbose=True)

count = 0
while True:
    L.next()
    count += 1
    if np.array_equal(L.state, state):
        print(count)
        break
