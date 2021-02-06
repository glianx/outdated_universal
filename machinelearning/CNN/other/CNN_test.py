import numpy as np
from icecream import ic

a = np.array([x for x in range(10)])
b = np.array([x for x in range(10,20)])

p = np.random.permutation(len(a))

ic(p, type(p))
ic(a[p])
ic(b[p])

#ic(a[np.array([6, 7, 8, 5, 9])])

ic(np.random.permutation(10))