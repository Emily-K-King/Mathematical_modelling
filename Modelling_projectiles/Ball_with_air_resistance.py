import numpy as np
import matplotlib.pyplot as plt


#Functionalise the euler method 
def simulate_projectile(vx0, vy0, dt, g, m, k=0, drag=True):
    x, y = 0, 0
    vx, vy = vx0, vy0
    x_values = [x]
    y_values = [y]

    while y>=0:
        if drag:
            ax = -(k/m) * vx
            ay = -g - (k/m) * vy
        else:
            ax = 0
            ay = -g
        vx = vx + ax * dt 
        vy = vy + ay * dt

        x = x + vx * dt
        y = y + vy * dt 

        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

#Constants
g = 9.81
m = 0.15
k = 0.05
dt = 0.01

#With air resistance
x_values, y_values = simulate_projectile(15, 20, dt, g, m, k=k, drag=True)

#Without air resistance
x_values_no, y_values_no = simulate_projectile(15, 20, dt, g, m, drag=False)


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