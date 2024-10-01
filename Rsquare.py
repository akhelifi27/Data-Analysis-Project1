import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

# Read the data from the CSV file
df = pd.read_csv('recruitment_data.csv')

# Assuming the last column is the target variable and all other columns are features
# Modify the column names as per your actual dataset
X = df.iloc[:, :-1]
Y = df.iloc[:, -1]

# Adding a constant for the intercept term for statsmodels
X_with_const = sm.add_constant(X)

# Fit the model using statsmodels
model = sm.OLS(Y, X_with_const).fit()

# Calculate R-squared and Adjusted R-squared
r_squared = model.rsquared
adjusted_r_squared = model.rsquared_adj

print(f"R-squared: {r_squared}")
print(f"Adjusted R-squared: {adjusted_r_squared}")
