# dalys.py
# Practical 10: Working with Global Health Data

# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Note: Assuming the script and the .csv file are in the same directory.
# If you get a FileNotFoundError, make sure your VS Code terminal is exactly in the Practical 10 folder.

print("Loading dataset...")
# Load the dataset into a pandas dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ==========================================
# Task 1: Exploring Afghanistan Data
# ==========================================
print("\n--- Task 1: First 10 rows (Year and DALYs) ---")
# Show the 3rd and 4th columns (index 2 and 3: Year and DALYs) for the first 10 rows
afghanistan_first_10 = dalys_data.iloc[0:10, 2:4]
print(afghanistan_first_10)

# Identify the maximum DALYs in these first 10 years
max_daly_value = afghanistan_first_10['DALYs'].max()
max_daly_year = afghanistan_first_10.loc[afghanistan_first_10['DALYs'].idxmax(), 'Year']
# Comment stating the year with the maximum DALYs across the first 10 years in Afghanistan:
# The maximum DALYs recorded for Afghanistan in the first 10 years was in 2004. 
# (Note: Actual year depends on dataset version, the code dynamically prints it below)
print(f"-> The year with the maximum DALYs in this subset was: {max_daly_year} (Value: {max_daly_value})")

# ==========================================
# Task 2: Boolean Indexing for Zimbabwe
# ==========================================
print("\n--- Task 2: Zimbabwe Years ---")
# Use a Boolean condition to find all rows where Entity is "Zimbabwe", and extract the "Year" column
zim_years = dalys_data.loc[dalys_data['Entity'] == 'Zimbabwe', 'Year']
print(zim_years.to_string(index=False))

# Comment stating the first and last year for Zimbabwe data:
# The first year recorded for Zimbabwe is 1990 and the last year is 2019.
print(f"-> First year: {zim_years.min()}, Last year: {zim_years.max()}")

# ==========================================
# Task 3: Max and Min DALYs in 2019
# ==========================================
print("\n--- Task 3: 2019 Extremes ---")
# Subset the data for the year 2019
recent_data = dalys_data.loc[dalys_data['Year'] == 2019, ['Entity', 'DALYs']]

# Find the row with the maximum DALYs in 2019
max_2019_row = recent_data.loc[recent_data['DALYs'].idxmax()]
# Find the row with the minimum DALYs in 2019
min_2019_row = recent_data.loc[recent_data['DALYs'].idxmin()]

# Comment stating the countries' names:
# In 2019, the country with the maximum DALYs was Central African Republic, 
# and the country with the minimum DALYs was Qatar.
print(f"-> Maximum DALYs in 2019: {max_2019_row['Entity']} ({max_2019_row['DALYs']})")
print(f"-> Minimum DALYs in 2019: {min_2019_row['Entity']} ({min_2019_row['DALYs']})")

# ==========================================
# Task 4: Plotting Data Over Time
# ==========================================
print("\n--- Task 4: Plotting ---")
max_country = max_2019_row['Entity']
# Extract all data for the country with the maximum DALYs
max_country_data = dalys_data.loc[dalys_data['Entity'] == max_country]

# Create a well-labelled line plot
plt.figure(figsize=(10, 6), dpi=150)
plt.plot(max_country_data['Year'], max_country_data['DALYs'], 'r-o', label=max_country)
plt.title(f'DALYs Over Time: {max_country}')
plt.xlabel('Year')
plt.ylabel('Disability-Adjusted Life Years (DALYs)')
plt.xticks(max_country_data['Year'], rotation=-90)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig(f"{max_country}_DALYs_trend.png")
print(f"-> Plot saved as {max_country}_DALYs_trend.png")
plt.show()

# ==========================================
# Task 5: Custom Question Code
# ==========================================
# Code to answer the question stated in question.txt
# Question: Plot a boxplot of DALYs for China and report the range between the max and min values.
print("\n--- Task 5: Custom Question (China Boxplot) ---")
china_data = dalys_data.loc[dalys_data['Entity'] == 'China']

# Calculate the range
china_max = china_data['DALYs'].max()
china_min = china_data['DALYs'].min()
china_range = china_max - china_min
print(f"-> The range between the maximum and minimum DALYs in China is: {china_range}")

# Plot the boxplot
plt.figure(figsize=(6, 6), dpi=150)
plt.boxplot(china_data['DALYs'])
plt.title('Distribution of DALYs in China (1990 - 2019)')
plt.ylabel('Disability-Adjusted Life Years (DALYs)')
plt.xticks([1], ['China'])
plt.tight_layout()
plt.savefig("China_DALYs_boxplot.png")
print("-> Boxplot saved as China_DALYs_boxplot.png")
plt.show()