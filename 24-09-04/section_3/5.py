import numpy as np
import matplotlib.pyplot as plt

im = plt.imread('4.png')
h, w, _ = im.shape

x = np.array([i for i in range(w) for _ in range(h)])
y = np.array([h-1-i for _ in range(w) for i in range(h)])
c = [tuple(im[j][i]) for i in range(w) for j in range(h)]

k = [i for i in range(len(c)) if c[i][0]*c[i][1]*c[i][2] < 1.0]
x, y = x[k], y[k]

theta = 1.0
x, y = 1.5*x, .8*y
x, y = x*np.cos(theta) - y*np.sin(theta), x*np.sin(theta) + y*np.cos(theta)

import numpy.random as rd

c = tuple(rd.rand(3))

plt.scatter(x, y, marker='.', s=10, color=c, alpha=.3)
plt.axis('equal')
plt.savefig('5.png')