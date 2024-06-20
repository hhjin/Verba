import numpy as np
import matplotlib.pyplot as plt

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Time step
dt = 0.01

# Number of steps
n_steps = 10000

# Initialize the arrays
x = np.zeros(n_steps)
y = np.zeros(n_steps)
z = np.zeros(n_steps)

# Initial conditions
x[0], y[0], z[0] = (0.1, 0.0, 0.0)

# Integrate the Lorenz equations
for i in range(n_steps - 1):
    x_dot = sigma * (y[i] - x[i])
    y_dot = x[i] * (rho - z[i]) - y[i]
    z_dot = x[i] * y[i] - beta * z[i]
    x[i + 1] = x[i] + x_dot * dt
    y[i + 1] = y[i] + y_dot * dt
    z[i + 1] = z[i] + z_dot * dt

# Plotting
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
