import numpy as np
import matplotlib.pyplot as plt

plt.text(0, 0, '8', fontsize=200,
        ha='center', va='center')
plt.axis('off')
plt.xlim([-.1,.1])
plt.ylim([-.1,.1])
plt.savefig('2.png', bbox_inches='tight')