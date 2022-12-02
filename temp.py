import numpy as np

turn = 0

prices = np.zeros(shape=(1,5),dtype=np.intc)
prices[0][0] = 1000000
prices[0][1] = 1000000
prices[0][2] = 1000000
prices[0][3] = 1000000
prices[0][4] = 1000000

temp = np.array([[prices[turn - 1][0] - 100000],
                     [prices[turn - 1][1] - 100000],
                     [prices[turn - 1][2] - 100000],
                     [prices[turn - 1][3] - 100000],
                     [prices[turn - 1][4] - 100000],
                     ])
prices = np.r_[prices, temp]