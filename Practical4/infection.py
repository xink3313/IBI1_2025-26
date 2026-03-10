# Pseudocode Plan:
# 1. Start with initial infected individuals and the growth rate.
# 2. Use a while loop to calculate and display infected students each day.
# 3. The loop stops once all students (n=91) are infected.
# 4. Report how many days were taken to infect all.

# Starting variables [cite: 176, 177, 178]
initial_infected = 5
growth_rate = 0.4
total_students = 91
current_infected = initial_infected
days = 1

# Display day 1 status 
print("Day " + str(days) + ": " + str(current_infected))

# Loop until all students are infected 
while current_infected < total_students:
    days = days + 1
    # Update infected count based on growth rate [cite: 175, 177]
    current_infected = current_infected + (current_infected * growth_rate)
    print("Day " + str(days) + ": " + str(current_infected))

# Report the final result [cite: 179]
print("It took " + str(days) + " days to infect all students.")