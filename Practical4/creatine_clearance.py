# Pseudocode Plan:
# 1. Store variables for age, weight, gender, and creatinine concentration.
# 2. Check if input values are within specified correct ranges.
# 3. If invalid, report which variable needs correction.
# 4. If valid, calculate and report CrCl using the formula.

age = 25
weight = 70
gender = "male"
creatinine = 80

# Check ranges [cite: 201, 202]
if age >= 100:
    print("Correction needed: age must be < 100 years.")
elif weight <= 20 or weight >= 80:
    print("Correction needed: weight must be > 20kg and < 80kg.")
elif creatinine <= 0 or creatinine >= 100:
    print("Correction needed: creatinine concentration must be > 0 and < 100.")
elif gender not in ["male", "female"]:
    print("Correction needed: gender must be male or female.")
else:
    # Set gender factor [cite: 196]
    gender_factor = 0.85 if gender == "female" else 1.0
    # Formula calculation [cite: 196, 197]
    cr_cl = ((140 - age) * weight * gender_factor) / (72 * creatinine)
    print("Creatine clearance rate (CrCl): " + str(cr_cl))