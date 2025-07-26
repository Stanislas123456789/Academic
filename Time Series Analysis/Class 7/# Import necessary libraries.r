# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("C:\Users\Stanislas Michel\OneDrive\Bureau\FGV - Time Series Analysis\Meeting03_data.csv")

# Clean the data
data = data.dropna(subset=["Gini", "Public_2018_SOCX"])  # Remove rows with missing Gini or social spending
data["Public_2018_SOCX"] = pd.to_numeric(data["Public_2018_SOCX"], errors='coerce')
data["Gini"] = pd.to_numeric(data["Gini"], errors='coerce')

# Plot Gini vs. Public Social Spending
plt.figure(figsize=(12, 8))
sns.scatterplot(data=data, x="Public_2018_SOCX", y="Gini", hue="Region", style="OECD", s=100)
plt.title("Gini Coefficient vs. Public Social Spending (2018)", fontsize=16)
plt.xlabel("Public Social Spending (% of GDP)")
plt.ylabel("Gini Coefficient (lower is more equal)")
plt.grid(True)
plt.axhline(y=data["Gini"].mean(), color='red', linestyle='--', label='Average Gini')
plt.axvline(x=data["Public_2018_SOCX"].mean(), color='blue', linestyle='--', label='Average Social Spending')
plt.legend()
plt.tight_layout()
plt.show()