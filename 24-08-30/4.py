import matplotlib.pyplot as plt

im = plt.imread('sample.png')
h, w, _ = im.shape
for i in range(h):
  for j in range(w):
    plt.plot(j, 17-i, '.', markersize=20,
             color=tuple(im[i,j]))

plt.savefig('4.png')