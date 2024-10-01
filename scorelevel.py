import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("recruitment_data.csv")

# Assuming a 'score_level' column exists (independent variable)
# Assuming a 'HiringDecision' column exists (dependent variable)
# Update column names if different

# Encode HiringDecision (yes = 1, no = 0)
data["HiringDecision_code"] = data["HiringDecision"].map({"yes": 1, "no": 0})

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data["SkillScore"], data["HiringDecision_code"], c=data["HiringDecision"])
plt.xlabel("Score Level")
plt.ylabel("Hiring Decision (1=Yes, 0=No)")
plt.title("Hiring Decision by Score Level")
plt.legend()  # Add legend to show color mapping
plt.tight_layout()
plt.show()
