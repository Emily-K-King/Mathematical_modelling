import numpy as np
import matplotlib.pyplot as plt

#Constants
g = 9.81
m = 0.15
k = 0.05
dt = 0.01

#Initial conditions 
x = 0
y = 0

vx = 15
vy = 20

x_values = [x]
y_values = [y]

#Euler method 
while y >= 0:
    #Change in acceleration
    ax = -(k/m)*vx
    ay = -g -(k/m)*vy
    #Change in velocity 
    vx = vx + ax * dt
    vy = vy + ay * dt

    x = x + vx * dt
    y = y + vy * dt

    x_values.append(x)
    y_values.append(y)

#Plot with no air resistance 
x_no = 0
y_no = 0

vx_no = 15
vy_no = 20

x_values_no = [x_no]
y_values_no = [y_no]

#Euler loop for no air resistance
while y_no >= 0:

    # Accelerations
    ax = 0
    ay = -g

    # Update velocities
    vx_no = vx_no + ax * dt
    vy_no = vy_no + ay * dt

    # Update positions
    x_no = x_no + vx_no * dt
    y_no = y_no + vy_no * dt

    # Store positions
    x_values_no.append(x_no)
    y_values_no.append(y_no)


#Plot
plt.plot(x_values, y_values, label="With Air Resistance")
plt.plot(x_values_no, y_values_no,
         linestyle="--", label="No Air Resistance")
plt.title("Projectile Motion with Air Resistance")
plt.xlabel("Horizontal Distance Travelled (m)")
plt.ylabel("Height(m)")
plt.legend()

plt.xlim(left=0)
plt.ylim(bottom=0)

plt.grid()

plt.savefig("Air_resistance_projectile.png")