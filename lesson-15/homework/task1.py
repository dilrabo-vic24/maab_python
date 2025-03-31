
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

plt.figure(figsize=(10, 6))
x = np.linspace(-10, 10, 1000)
y = x**2 - 4*x + 4
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Quadratic Function: $f(x) = x^2 - 4x + 4$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.savefig('quadratic_function.png', dpi=300, bbox_inches='tight')
plt.close()