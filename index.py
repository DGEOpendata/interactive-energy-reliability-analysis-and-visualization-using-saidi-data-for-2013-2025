python
import pandas as pd
import matplotlib.pyplot as plt

# Load the SAIDI dataset
data_path = 'SAIDI.csv'  # Path to the SAIDI dataset file
data = pd.read_csv(data_path)

# Basic data exploration
print("Dataset Head:")
print(data.head())

print("\nDataset Info:")
print(data.info())

# Convert the 'Year' column to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Plotting the SAIDI data
plt.figure(figsize=(12, 6))
plt.plot(data['Year'], data['SAIDI (minutes)'], marker='o', linestyle='-', color='b', label='SAIDI')
plt.title('Annual SAIDI Data (2013-2025)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('SAIDI (minutes)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('saidi_trend_analysis.png')
plt.show()

# Example of exporting the processed data to a new CSV file
output_path = 'Processed_SAIDI.csv'
data.to_csv(output_path, index=False)
print(f"Processed data saved to {output_path}")
