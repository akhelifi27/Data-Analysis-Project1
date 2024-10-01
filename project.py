### Import necessary libraries
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify


### Load the CSV file by copying the file path into the parenthesis
data = pd.read_csv(r"recruitment_data.csv")


### Drop unwanted columns
# data = data.drop(['Age', 'Gender', 'DistanceFromCompany'], axis=1)

### Define dependent variable
y = data['HiringDecision']
# data = data.drop(['HiringDecision'], axis=1)

### Define independent variables and add a constant term
X = sm.add_constant(data.drop('HiringDecision', axis=1))

### Add interaction term
# X['RushingY_Oppdef_Interact'] = X["EducationLevel"] * X["SkillScore"]

### Create the OLS model
model = sm.OLS(y, X)

### Fit the model
results = model.fit()

### Print regression summary
print(results.summary())

### Check correlation matrix
correlation_matrix = data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

### Check VIF for multicollinearity
vif_data = pd.DataFrame()
vif_data['feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print('\nVIF Data:')
print(vif_data)
pd.options.display.max_columns = None
pd.options.display.width = None
df = pd.read_csv("recruitment_data.csv")

sns.scatterplot(x="Age", y="HiringDecision", data=df)
plt.show()