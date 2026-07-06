import matplotlib.pyplot as plt
import numpy as np

# Define the decay parameters
t_half = 10 
lam = np.log(2) / t_half
N_0 = 10000
t_max = 50

# Time step 
dt = 0.1
num_steps = int(t_max / dt)

t_euler = np.zeros(num_steps + 1)
N_euler = np.zeros(num_steps + 1)

# Setting the initial vaues
t_euler[0] = 0
N_euler[0] = N_0

# Euler's method loop
for i in range (num_steps):
    dN = -lam * N_euler[i] * dt 

    N_euler[i+1] = N_euler[i] + dN
    t_euler[i+1] = t_euler[i] + dt

# Calculate the exact solutions for comparison
N_exact = N_0 * np.exp(-lam * t_euler)

# Plot results 
plt.figure(figsize=(8, 5))
plt.plot(t_euler, N_euler, 'b--', label = "Euler's Method", linewidth=2)
plt.plot(t_euler, N_exact, 'r-', label="Exact Solution", alpha=0.7)
plt.title(f"Radioactive Decay using Euler's Method (dt = {dt}s)")
plt.xlabel('Time (s)')
plt.ylabel('Number of Atoms ($N$)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("Radioactive_Decay_Euler.png")
#plt.show()