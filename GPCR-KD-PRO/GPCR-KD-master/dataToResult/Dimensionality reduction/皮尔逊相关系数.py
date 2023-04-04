import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({"x": [1, 4, 3, 5], "y": [1, 3, 4, 5]})
df_corr = data.corr("pearson")
print(df_corr)

# 画出热力图
# sns.heatmap(df_corr, vmax=1, vmin=-1, center=0, annot=True)
# plt.savefig('heatmap_corr_example.png')
