import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
np.random.seed(42) 
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100) 
sizes = np.random.randint(20, 200, 100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, cmap='viridis', marker='o', edgecolors='k', linewidths=0.5)
plt.colorbar(label='Color Value')
plt.title('Random 2D Scatter Plot', fontsize=14)
plt.xlabel('X-axis', fontsize=12)
plt.ylabel('Y-axis', fontsize=12)
plt.grid(True)
plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
plt.close()