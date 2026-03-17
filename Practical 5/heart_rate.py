import matplotlib.pyplot as plt

# The heart rate data provided in the practical [cite: 254]
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 1. Calculate number of patients and mean heart rate [cite: 256]
num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients
print(f"Number of patients: {num_patients}, Mean heart rate: {mean_hr}")

# 2. Categorize the heart rates [cite: 257, 258]
low, normal, high = 0, 0, 0
for hr in heart_rates:
    if hr < 60:
        low += 1
    elif hr <= 120:
        normal += 1
    else:
        high += 1

counts = [low, normal, high]
categories = ['Low', 'Normal', 'High']
print(f"Low: {low}, Normal: {normal}, High: {high}")

# Identify the largest category [cite: 258]
max_idx = counts.index(max(counts))
print(f"The category with the largest number of patients is: {categories[max_idx]}")

# 3. Create a well-labelled pie chart [cite: 259, 264]
plt.pie(counts, labels=categories, autopct='%1.1f%%')
plt.title('Distribution of Heart Rate Categories')
plt.show()