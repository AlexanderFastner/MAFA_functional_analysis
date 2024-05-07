import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("../data/ULM_vs_MLM.csv", index_col=0)
print(data)
# print()
# print(data.loc["Top_25"])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

## Pearson and Spearman Correlations
ax1.plot(data.loc["Pearson"], color='blue', label='Pearson')
ax1.plot(data.loc["Spearman"], color='green', label='Spearman')
ax1.set_ylabel('Correlations')
ax1.set_ylim(0, 1)
ax1.tick_params('y', colors='blue')
ax1.legend(loc='upper left')

## Top 25% and Top 10% Overlap
ax2.plot(data.loc["Top_25"], color='purple', label='Top 25%')
ax2.plot(data.loc["Top_10%"], color='brown', label='Top 10%')
ax2.set_xlabel('Columns')
ax2.set_xticks(np.arange(6))
ax2.set_ylabel('Percentage overlap')
ax2.tick_params('y', colors='red')
ax2.set_ylim(0, 100)
ax2.set_xticklabels(['WT_T0', 'WT_T1', 'WT_T2', 'MUT_T0', 'MUT_T1', 'MUT_T2'])
ax2.legend(loc='upper left')

plt.show()
plt.savefig('../figures/ulm_mlm/ULM_vs_MLM.png', dpi=300)