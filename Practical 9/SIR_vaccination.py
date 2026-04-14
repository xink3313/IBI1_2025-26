import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 1. Basic model parameters
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# Vaccination rates to test: 0.0 to 1.0
vaccination_rates = np.arange(0.0, 1.1, 0.1)

# Set up the plot
plt.figure(figsize=(8, 5), dpi=150)

# 2. Loop through each vaccination rate
for i, v_rate in enumerate(vaccination_rates):
    V = int(N * v_rate)
    I_current = 1
    S_current = N - V - I_current
    I = [I_current]
    
    # 3. Time course simulation
    for t in range(time_steps):
        p_infect = beta * (I_current / N)
        p_infect = min(p_infect, 1.0)
        
        if S_current > 0:
            new_infected = np.sum(np.random.choice([1, 0], size=S_current, p=[p_infect, 1 - p_infect]))
        else:
            new_infected = 0
            
        if I_current > 0:
            new_recovered = np.sum(np.random.choice([1, 0], size=I_current, p=[gamma, 1 - gamma]))
        else:
            new_recovered = 0
            
        S_current -= new_infected
        I_current = I_current + new_infected - new_recovered
        I.append(I_current)
        
    # 4. Plot the Infected curve
    label_name = "0" if v_rate == 0 else f"{int(v_rate * 100)}%"
    plt.plot(I, label=label_name, color=cm.viridis(i * 25))

# 5. Finalize and save
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("SIR_vaccination.png", format="png")
plt.show()