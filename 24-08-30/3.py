import matplotlib.pyplot as plt
import numpy as np

im = plt.imread('sample.png')
print(type(im))
print(im.shape)
print(im[5, 10, :])

plt.imshow(im)
plt.savefig('3.png')