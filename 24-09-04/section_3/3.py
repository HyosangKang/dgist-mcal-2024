import numpy as np
import matplotlib.pyplot as plt

im = plt.imread('sample.png')
h, w, _ = im.shape

x = np.array([i for i in range(w) for _ in range(h)])
y = np.array([17-i for _ in range(w) for i in range(h)])

# do something with x and y to get rotation!


c = [tuple(im[j][i]) for i in range(w) for j in range(h)]
plt.scatter(x, y, marker=',', s=100, color=c)
plt.axis('equal')
plt.savefig('3.png')