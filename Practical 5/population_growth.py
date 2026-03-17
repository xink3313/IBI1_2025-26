import matplotlib.pyplot as plt

# 1. Data based on the World Bank table provided in the practical [cite: 266, 267]
# Format: {Country: [Population_2020, Population_2024]}
data = {
    'UK': [66.7, 69.2],
    'China': [1426, 1410],
    'Italy': [59.4, 58.9],
    'Brazil': [208.6, 212.0],
    'USA': [331.6, 340.1]
}

# 2. Calculate and print percentage change for each country [cite: 268, 269]
changes = {}
print("Percentage Population Change:")
for country, pops in data.items():
    pop2020, pop2024 = pops[0], pops[1]
    # Calculation formula: ((pop2024 - pop2020) / pop2020) * 100
    pct_change = ((pop2024 - pop2020) / pop2020) * 100
    changes[country] = pct_change
    print(f"{country}: {pct_change:.2f}%")

# 3. Sort changes from largest increase to largest decrease [cite: 270, 275]
sorted_changes = sorted(changes.items(), key=lambda x: x[1], reverse=True)
print("\nCountries sorted by population change:")
for country, change in sorted_changes:
    print(f"{country}: {change:.2f}%")

# 4. Identify countries with the largest increase and decrease [cite: 271, 276]
print(f"\nCountry with the largest increase: {sorted_changes[0][0]}")
print(f"Country with the largest decrease: {sorted_changes[-1][0]}")

# 5. Create a well-labelled bar chart showing the change for each country [cite: 272, 277]
countries = [x[0] for x in sorted_changes]
pct_values = [x[1] for x in sorted_changes]

plt.bar(countries, pct_values)
plt.ylabel('Percentage Change (%)')
plt.title('Population Growth Rate (2020-2024)')
plt.axhline(0, color='black', linewidth=0.8) # Adds a line at 0 for clarity
plt.show()