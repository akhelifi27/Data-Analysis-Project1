import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('recruitment_data.csv')

# Select relevant features and target
features = ['EducationLevel', 'SkillScore', 'PersonalityScore', 'InterviewScore', 'ExperienceYears']
target = 'HiringDecision'

# Convert categorical variables to numerical ones if necessary
# df['EducationLevel'] = df['EducationLevel'].astype('category').cat.codes

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(df[features])
y = df[target]

# Fit logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Extract coefficients
coefficients = model.coef_[0]
feature_names = features

# Create a DataFrame for visualization
coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})

# Plot the coefficients
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=coef_df)
plt.title('Logistic Regression Coefficients')
plt.show()
