import numpy as np
turn = 0
prices = np.zeros(shape=(1,5),dtype=np.intc)
prices[0][0] = 1000000
prices[0][1] = 1000000
prices[0][2] = 1000000
prices[0][3] = 1000000
prices[0][4] = 1000000

change = np.zeros(5, dtype=np.intc)

ss = 0
gc = 0
mc = 0
kk = 0
dt = 0