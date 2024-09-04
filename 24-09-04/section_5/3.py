import numpy as np
import matplotlib.pyplot as plt

im = plt.imread('2.png')
h, w, _ = im.shape
print(h,w)
x = np.array([i for i in range(w) for _ in range(h)])
y = np.array([h-1-i for _ in range(w) for i in range(h)])
c = [tuple(im[j][i]) for i in range(w) for j in range(h)]
k = [i for i in range(len(c)) 
     if c[i][0]*c[i][1]*c[i][2] < 1.0]
x, y = x[k], y[k]

import numpy.random as rd

c = tuple(rd.rand(3))

t = -1 + 2*rd.rand()
r = np.array([
  [np.cos(t), -np.sin(t)],
  [np.sin(t), np.cos(t)]
])
l1, l2 = .8 + .4*rd.rand(), .8 + .4*rd.rand()
p = np.array([l1*x, l2*y])
p = r@p
x, y = p[0], p[1]

plt.scatter(x, y, marker='.', s=100, color=c)
plt.axis('equal')
plt.axis('off')
plt.savefig('3.png')
