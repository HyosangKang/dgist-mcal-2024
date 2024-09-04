import numpy as np
import matplotlib.pyplot as plt

plt.text(0, 0, '1', 
        fontsize=200,
        ha='center',
        va='center')
plt.axis('off')
plt.xlim([-.1,.1])
plt.ylim([-.1,.1])
plt.axis('equal')
plt.savefig('4.png', 
            bbox_inches='tight')