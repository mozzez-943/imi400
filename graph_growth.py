import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate synthetic data (replace with real data if available)
months = [
    "Jan 2023", "Feb 2023", "Mar 2023", "Apr 2023", "May 2023", "Jun 2023", "Jul 2023", "Aug 2023", "Sep 2023", "Oct 2023", "Nov 2023", "Dec 2023",
    "Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024", "May 2024", "Jun 2024", "Jul 2024", "Aug 2024", "Sep 2024", "Oct 2024", "Nov 2024", "Dec 2024"
]
# Q1 2023, Q3 2023, Q1 2024, Q3 2024
# Q2 2023, Q4 2023, Q2 2024, Q4 2024
users = [
    0, 0, 0, 1000, 1100, 1210, 2474, 2771, 3104, 5334, 6188, 7178,
    0, 0, 0, 1573, 1730, 1903, 3538, 4034, 4598, 8470, 9994, 11793
]  # Example growth trend

# Define quarters for grouping
quarters = ["Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026", "Q3 2026", "Q4 2026"]
quarter_labels = [quarters[i // 3] for i in range(len(months))]

# Create a DataFrame for better handling
market_data = pd.DataFrame({"Month": months, "Users": users, "Quarter": quarter_labels})

# Group by quarters
grouped_data = market_data.groupby("Quarter")["Users"].apply(list).tolist()

# Plot
plt.figure(figsize=(12, 6))
x = np.arange(len(quarters))  # X-axis positions for each quarter
width = 0.25  # Bar width

# Create a grouped bar chart
for i in range(3):  # Three months per quarter
    month_values = [q[i] for q in grouped_data]
    plt.bar(x + i * width, month_values, width=width, label=f"Month {i+1}")

# Formatting
plt.xlabel("Quarter")
plt.ylabel("Number of Users")
plt.title("HeadFirst Bikeshare Helmet User Growth (2025-2026)")
plt.xticks(x + width, quarters, rotation=45)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show plot
plt.show()