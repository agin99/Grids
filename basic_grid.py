import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y = np.linspace(0, 10, 11)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(6,6))
plt.scatter(X, Y, marker='o', color='blue')
x_ticks = np.linspace(0, 10, 11)
y_ticks = np.linspace(0, 10, 11)
plt.xticks(x_ticks)
plt.xlabel('x')
plt.yticks(y_ticks)
plt.ylabel('y')
plt.title('2D Uniform Grid')
plt.grid(True)
plt.show()
