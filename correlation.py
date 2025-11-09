import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("5in1.csv")

corr_vars = df[['Rating', 'Views', 'Rating Count', 'Log Transformed Views', 'Log Transformed Rating Count']]

corr_matrix = corr_vars.corr(method='pearson')

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Between Key Variables", fontsize=14)
plt.tight_layout()
plt.show()

