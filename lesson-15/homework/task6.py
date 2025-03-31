import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

surface = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=True, alpha=0.8)

fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label='Z Value')

ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)
ax.set_zlabel('Z-axis', fontsize=12)
ax.set_title('3D Surface Plot: $f(x, y) = \cos(x^2 + y^2)$', fontsize=14)

plt.savefig('3d_surface_plot.png', dpi=300, bbox_inches='tight')
plt.close()