import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson


df = pd.read_csv("5in1.csv")


X = df[["Rating", "Log Transformed Rating Count", "Rating * Log TRC"]]  
y = df["Log Transformed Views"]  


X = sm.add_constant(X)


model = sm.OLS(y, X).fit()

print(model.summary())

print("\nPrecise p-values for each variable:")
for var, p in model.pvalues.items():
    print(f"{var}: p-value = {p:.5e}")

residuals = model.resid
fitted_vals = model.fittedvalues


plt.figure(figsize=(8, 5))
sns.residplot(x=fitted_vals, y=residuals, lowess=True, line_kws={'color': 'red'})
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")
plt.axhline(0, color='gray', linestyle='--')
plt.tight_layout()
plt.show()


sm.qqplot(residuals, line='45', fit=True)
plt.title("Q-Q Plot of Residuals")
plt.tight_layout()
plt.show()

dw = durbin_watson(residuals)
print(f"Durbin-Watson statistic: {dw:.4f}")
print(f"R-squared: {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")
print(f"Root Mean Squared Error (RMSE): {np.sqrt(np.mean(residuals**2)):.4f}")

