import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('5in1.csv')  

variable = ''  

plt.figure(figsize=(8, 5))
sns.kdeplot(df[variable], shade=True, color='skyblue', linewidth=2)

plt.title(f'Distribution of {variable}', fontsize=14)
plt.xlabel(variable, fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()


