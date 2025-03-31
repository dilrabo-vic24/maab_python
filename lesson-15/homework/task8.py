import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
periods = ['T1', 'T2', 'T3', 'T4']
category_a = [20, 35, 30, 35]
category_b = [25, 32, 34, 20]
category_c = [15, 15, 19, 28]

plt.bar(periods, category_a, color='#4CAF50', label='Category A', edgecolor='black', linewidth=1)
plt.bar(periods, category_b, bottom=category_a, color='#2196F3', label='Category B', edgecolor='black', linewidth=1)
plt.bar(periods, category_c, bottom=np.array(category_a) + np.array(category_b), color='#F44336', label='Category C', edgecolor='black', linewidth=1)

plt.title('Stacked Contributions by Category Over Time', fontsize=14)
plt.xlabel('Time Period', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i in range(len(periods)):
    total = category_a[i] + category_b[i] + category_c[i]
    plt.text(i, total + 1, f'{total}', ha='center', va='bottom', fontsize=10)

plt.savefig('stacked_bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()