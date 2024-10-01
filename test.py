import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('recruitment_data.csv')

# Filter the data to include only those who were hired
hired_df = df[df['HiringDecision'] == 1]

# Calculate the median years of experience for those who were hired
median_experience = hired_df['ExperienceYears'].median()

print(f"Median years of experience for people hired: {median_experience}")
