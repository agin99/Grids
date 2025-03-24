import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(2 * np.pi * x) + 0.5 * np.exp(-200 * (x - 0.5)**2)

def fprime_exact(x):
    return 2 * np.pi * np.cos(2 * np.pi * x) - 200 * (x - 0.5) * np.exp(-200 * (x - 0.5)**2)

def fds(x, y):
    fds_approx = []
    monitor_mass_value = 0
    monitor_mass = []
    for i in range(len(x)):
        if i < len(x) - 1: 
            monitor_mass_value += 1 + abs((y[i+1] - y[i]) / (x[i+1] - x[i]))
            fds_approx.append((y[i+1] - y[i]) / (x[i+1] - x[i]))
        else:
            monitor_mass_value += 1 + abs((y[i] - y[i-1]) / (x[i] - x[i-1]))
            fds_approx.append((y[i] - y[i-1]) / (x[i] - x[i-1]))
        monitor_mass.append(monitor_mass_value)
    return fds_approx, monitor_mass

x = np.linspace(0, 1, 101)
y = f(x)
fds_approx, monitor_mass = fds(x,y)
delta_gamma = monitor_mass[-1]/len(monitor_mass)
x_adjusted = []
for i in range(len(monitor_mass) - 1): 
    interval_mass = monitor_mass[i+1] - monitor_mass[i]
    for j in np.arange(monitor_mass[i], monitor_mass[i + 1], delta_gamma): 
        x_adjusted.append(x[i] + (j - monitor_mass[i]) / (monitor_mass[i + 1] - monitor_mass[i]) * (x[i + 1] - x[i]))

y_adjusted = f(np.array(x_adjusted))
fds_approx_adjusted, monitor_mass_adjusted = fds(x_adjusted, y_adjusted)
print(len(x))
print(len(x_adjusted))

fig, axes = plt.subplots(1, 2, figsize=(10,5)) 
axes[0].plot(x, fds_approx, 's-', label='Normal')
axes[0].set_title("Finite Difference on Uniform Grid")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f'(x)")
axes[0].grid(True)
axes[0].legend()

axes[1].plot(x_adjusted, fds_approx_adjusted, '^-.', label='Adjusted')
axes[1].set_title("Finite Difference on Adaptive Grid")
axes[1].set_xlabel("x")
axes[1].set_ylabel("f'(x)")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()