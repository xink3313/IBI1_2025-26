# SIR.py
# A probabilistic SIR model to simulate the spread of an infectious disease

import numpy as np
import matplotlib.pyplot as plt

# 1. Define the basic variables of the model
N = 10000            # Total population [cite: 408, 409]
I_current = 1        # Initially, one person is infected 
S_current = N - 1    # The rest of the population is Susceptible 
R_current = 0        # Nobody has yet recovered 

beta = 0.3           # Infection probability upon contact [cite: 395, 410]
gamma = 0.05         # Recovery probability [cite: 396, 410]
time_steps = 1000    # Loop over 1000 time points [cite: 414]

# Arrays to track how variables evolve over time [cite: 411, 412]
S = [S_current]
I = [I_current]
R = [R_current]

# 2. The time course simulation
for t in range(time_steps):
    # The probability of infection: beta * proportion of infected people [cite: 422, 423]
    p_infect = beta * (I_current / N)
    
    # Ensure probability does not exceed 1.0
    p_infect = min(p_infect, 1.0)
    
    # Pick susceptible individuals at random to become infected [cite: 415]
    # np.random.choice returns an array of 1s (infected) and 0s (safe) [cite: 419, 420]
    new_infected = np.sum(np.random.choice([1, 0], size=S_current, p=[p_infect, 1 - p_infect]))
    
    # Pick infected individuals at random to become recovered [cite: 416]
    # Recovery probability for each infected individual is simply gamma [cite: 421]
    new_recovered = np.sum(np.random.choice([1, 0], size=I_current, p=[gamma, 1 - gamma]))
    
    # Update the population categories
    S_current -= new_infected
    I_current = I_current + new_infected - new_recovered
    R_current += new_recovered
    
    # Record the output of this time step [cite: 424]
    S.append(S_current)
    I.append(I_current)
    R.append(R_current)

# 3. Plot the results [cite: 425]
# Set up dimensions and resolution [cite: 444, 445]
plt.figure(figsize=(6, 4), dpi=150) 

plt.plot(S, label='susceptible')
plt.plot(I, label='infected')
plt.plot(R, label='recovered')

# Label axes and add legend [cite: 426]
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

# Save the plot as a png file [cite: 447]
plt.savefig("SIR_model.png", format="png")
plt.show()