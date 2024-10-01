import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set options for wider display (optional)
pd.options.display.max_columns = None
pd.options.display.width = None

# Read the data from the CSV file
df = pd.read_csv("recruitment_data.csv")

# Create the scatter plot with color coding
sns.scatterplot(x="SkillScore", y="HiringDecision", hue="HiringDecision", data=df, palette="Set2")  # Adjust palette as desired
plt.xlabel("Skill Score")
plt.ylabel("Hiring Decision")
plt.title("Hiring Decision vs. Skill Score")
plt.legend()  # Add legend to show color mapping
plt.show()
