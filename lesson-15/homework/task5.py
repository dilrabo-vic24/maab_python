import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
np.random.seed(42)
data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Histogram of Normal Distribution', fontsize=14)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, alpha=0.3)

plt.axvline(data.mean(), color='r', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.2f}')
plt.axvline(data.mean() + data.std(), color='g', linestyle='-.', linewidth=2, label=f'Mean + Std: {data.mean() + data.std():.2f}')
plt.axvline(data.mean() - data.std(), color='g', linestyle='-.', linewidth=2, label=f'Mean - Std: {data.mean() - data.std():.2f}')
plt.legend()

plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
plt.close()