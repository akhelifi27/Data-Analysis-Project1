import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Assuming 'df' is a pandas DataFrame variable containing the data
df = pd.read_csv('recruitment_data.csv')

# Distribution plot

# Box plot for numerical features
sns.boxplot(x='HiringDecision', y='PersonalityScore', data=df)
plt.title('Personality Score vs Hiring Decision')
plt.show()

# Load dataset
df = pd.read_csv('recruitment_data.csv')

# Total number of candidates in each education level
total_SkillScore_counts = df['ExperienceYears'].value_counts()

# Number of hired candidates in each education level
hired_education_counts = df[df['HiringDecision'] == 1]['ExperienceYears'].value_counts()

# Calculate the percentage of hired candidates in each education level
hired_SkillScore_percentage = (hired_education_counts / total_SkillScore_counts) * 100

# Drop NaN values if any education level has no hired candidates
hired_SkillScore_percentage = hired_SkillScore_percentage.dropna()

# Create a pie plot
plt.figure(figsize=(10, 6))
plt.pie(hired_SkillScore_percentage, labels=hired_SkillScore_percentage.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of People Hired by Skill Score from Entire Pool')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

