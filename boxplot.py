import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('pure-data.csv')  

numeric_df = df.select_dtypes(include='number')


plt.figure(figsize=(12, len(numeric_df.columns) * 1.5))  
plt.boxplot([numeric_df[col].dropna() for col in numeric_df.columns], vert=False)
plt.yticks(range(1, len(numeric_df.columns) + 1), numeric_df.columns)

plt.xlabel("Value")
plt.title("Box Plot of Each Numeric Column")
plt.tight_layout()
plt.grid(True, axis='x', linestyle='--', alpha=0.6)


plt.show()

