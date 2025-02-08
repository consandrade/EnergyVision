import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
monthly_data = pd.read_csv('/home/ctand/EnergyVision/data/processed/MONTHLYDATA.csv')

# Convert 'date' column to datetime
monthly_data['date'] = pd.to_datetime(monthly_data['date'])

# Set Seaborn theme
sns.set_theme(style="whitegrid", palette="muted")

# Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_data, x='date', y='COAST', marker='o', linewidth=2.5, color='b', label='Energy Consumption')

# Formatting
plt.xlabel('Date', fontsize=14)
plt.ylabel('Energy Consumption (MWh)', fontsize=14)
plt.title('Monthly Energy Consumption Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12, loc='upper right')

# Show the plot
plt.show()

