import numpy as np
import matplotlib.pyplot as plt


fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Multiple Function Plots', fontsize=16)

x1 = np.linspace(-5, 5, 1000)
axs[0, 0].plot(x1, x1**3, 'b-', linewidth=2)
axs[0, 0].set_title('$f(x) = x^3$', fontsize=12)
axs[0, 0].set_xlabel('x', fontsize=10)
axs[0, 0].set_ylabel('f(x)', fontsize=10)
axs[0, 0].grid(True)

x2 = np.linspace(0, 2*np.pi, 1000)
axs[0, 1].plot(x2, np.sin(x2), 'r-', linewidth=2)
axs[0, 1].set_title('$f(x) = \sin(x)$', fontsize=12)
axs[0, 1].set_xlabel('x', fontsize=10)
axs[0, 1].set_ylabel('f(x)', fontsize=10)
axs[0, 1].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
axs[0, 1].set_xticklabels(['0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
axs[0, 1].grid(True)

x3 = np.linspace(-2, 2, 1000)
axs[1, 0].plot(x3, np.exp(x3), 'g-', linewidth=2)
axs[1, 0].set_title('$f(x) = e^x$', fontsize=12)
axs[1, 0].set_xlabel('x', fontsize=10)
axs[1, 0].set_ylabel('f(x)', fontsize=10)
axs[1, 0].grid(True)

x4 = np.linspace(0, 5, 1000)
axs[1, 1].plot(x4, np.log(x4 + 1), 'm-', linewidth=2)
axs[1, 1].set_title('$f(x) = \log(x+1)$', fontsize=12)
axs[1, 1].set_xlabel('x', fontsize=10)
axs[1, 1].set_ylabel('f(x)', fontsize=10)
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('function_subplots.png', dpi=300, bbox_inches='tight')
plt.close()