import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.labelsize'] = 16  # Increased from 12
plt.rcParams['axes.titlesize'] = 18  # Increased from 14
plt.rcParams['xtick.labelsize'] = 14  # Increased from 10
plt.rcParams['ytick.labelsize'] = 14  # Increased from 10

ultra_bi_color = '#27ae60'  # Green
sao_color = '#e67e22'       # Orange

fig, ax = plt.subplots(figsize=(8, 6))

ax.grid(False)

groups = ['Ultra-BI', 'SAO']
values = [1046.9, 1019.0]
se = [90.0, 90.0]  # Estimated from the paper's CI

ax.text(0.5, 0.85, 'Difference: 27.8g/4 weeks (95% CI -149.7 to 205.4), p=0.76', 
        ha='center', va='center', transform=ax.transAxes, fontsize=16)  # Increased from 12

x_pos = np.arange(len(groups))
bars = ax.bar(x_pos, values, align='center', alpha=0.8, width=0.6, 
              color=[ultra_bi_color, sao_color], edgecolor='black', linewidth=1)

ax.errorbar(x_pos, values, yerr=se, fmt='none', ecolor='black', capsize=5)

for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height/2, 
            f'{values[i]}', ha='center', va='center', fontsize=16,  # Increased from 12
            fontweight='bold', color='white')

ax.set_ylabel('Alcohol Consumption (g/4 weeks)', fontweight='bold')
ax.set_title('Primary Outcome: Total Alcohol Consumption (24 weeks)', fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(groups, fontweight='bold')
ax.set_ylim(0, 1500)  # Set y-axis limit
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(pad=3)
plt.savefig('primary_outcome_graph_larger_text.png', dpi=300, bbox_inches='tight')
plt.close()

fig, ax = plt.subplots(figsize=(8, 6))

ax.grid(False)

groups = ['Ultra-BI', 'SAO']
values = [2.1, 1.9]  # Absolute values
se = [0.05, 0.05]  # Estimated from the paper's CI

ax.text(0.5, 0.85, 'Difference: 0.2 (95% CI 0.1 to 0.3), p=0.005', 
        ha='center', va='center', transform=ax.transAxes, fontsize=16)  # Increased from 12

x_pos = np.arange(len(groups))
bars = ax.bar(x_pos, values, align='center', alpha=0.8, width=0.6, 
              color=[ultra_bi_color, sao_color], edgecolor='black', linewidth=1)

ax.errorbar(x_pos, values, yerr=se, fmt='none', ecolor='black', capsize=5)

for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height/2, 
            f'{values[i]}', ha='center', va='center', fontsize=16,  # Increased from 12
            fontweight='bold', color='white')

ax.set_ylabel('Readiness to Change Score', fontweight='bold')
ax.set_title('Secondary Outcome: Readiness to Change (24 weeks)', fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(groups, fontweight='bold')
ax.set_ylim(0, 3)  # Set y-axis limit
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(pad=3)
plt.savefig('secondary_outcome_graph_larger_text.png', dpi=300, bbox_inches='tight')
plt.close()

print("Graphs with larger text created successfully!")
