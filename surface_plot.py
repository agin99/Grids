import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 11)
y = np.linspace(0, 10, 11)
X, Y = np.meshgrid(x, y, indexing='xy')
Z = np.sin(X) * np.cos(Y)

plt.figure(figsize=(8, 8))
contour = plt.contourf(X, Y, Z, levels=5)
plt.colorbar(contour, label='Z')
plt.title('Contour plot of f(x,y) = sin(x) * cos(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.clabel(contour, inline=True, fontsize=7, colors='black')
plt.show()

