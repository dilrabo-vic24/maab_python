import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['#4CAF50', '#2196F3', '#F44336', '#FFC107', '#9C27B0']

bars = plt.bar(products, sales, color=colors, width=0.6, edgecolor='black', linewidth=1)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 5,
             f'{height}', ha='center', va='bottom', fontsize=10)

plt.title('Sales by Product', fontsize=14)
plt.xlabel('Products', fontsize=12)
plt.ylabel('Sales (units)', fontsize=12)
plt.ylim(0, 300) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
plt.close()