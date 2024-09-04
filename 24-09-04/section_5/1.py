import numpy as np
import matplotlib.pyplot as plt

im = plt.imread('sample.png')
h, w, _ = im.shape
x = [i for i in range(w) for _ in range(h)]
y = [h-1-i for _ in range(w) for i in range(h)]
c = [tuple(im[j][i]) for i in range(w) for j in range(h)]

t = 1.0
r = np.array([
  [np.cos(t), -np.sin(t)],
  [np.sin(t), np.cos(t)]
])
p = np.array([x,y])
p = r@p
x, y = p[0], p[1]

plt.scatter(x, y, marker=',', s=100, color=c)
plt.savefig('1.png')
