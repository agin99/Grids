import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
y = [np.sin(i) for i in x]
FDS_dy = []
for i in range(len(x)):
    if i < len(x) - 1: 
        FDS_dy.append((np.sin(x[i+1]) - np.sin(x[i])) / (x[i+1] - x[i]))
    else:
        FDS_dy.append((np.sin(x[i]) - np.sin(x[i-1])) / (x[i] - x[i-1]))

BDS_dy = []
for i in range(len(x)):
    if i == 0:
        BDS_dy.append((np.sin(x[i+1]) - np.sin(x[i])) / (x[i+1] - x[i]))
    else:
        BDS_dy.append((np.sin(x[i]) - np.sin(x[i-1])) / (x[i] - x[i-1]))

CDS_dy = []
for i in range(len(x)):
    if i == 0:
        CDS_dy.append((np.sin(x[i+1]) - np.sin(x[i])) / (x[i+1] - x[i]))
    elif i == len(x) - 1:
        CDS_dy.append((np.sin(x[i]) - np.sin(x[i-1])) / (x[i] - x[i-1]))
    else:
        CDS_dy.append((np.sin(x[i+1]) - np.sin(x[i-1])) / (x[i+1] - x[i-1]))

true_dy = np.cos(x)
plt.figure(figsize=(8,8))
plt.plot(x, FDS_dy, 's-', label='Forward Difference Scheme')
plt.plot(x, BDS_dy, '^-.', label='Backward Difference Scheme')
plt.plot(x, CDS_dy, '+:', label='Central Difference Scheme')
plt.plot(x, true_dy, 'x--', label='True Derivative: cos(x)')
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title("Finite Difference Approximation vs. True Derivative")
plt.grid(True)
plt.legend(loc='upper right')
plt.show()
