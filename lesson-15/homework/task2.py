import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
x = np.linspace(0, 2*np.pi, 1000)
plt.plot(x, np.sin(x), 'r-', linewidth=2, label='sin(x)', marker='o', markevery=100)
plt.plot(x, np.cos(x), 'g--', linewidth=2, label='cos(x)', marker='^', markevery=100)
plt.title('Sine and Cosine Functions', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], 
           ['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
plt.savefig('sin_cos_plot.png', dpi=300, bbox_inches='tight')
plt.close()