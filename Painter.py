import matplotlib.pyplot as plt
import numpy as np
for j in [1]:
    for i in range(1, 11):
        xpoints = np.load(f'{j}/xpoints_1_{i}.npy')
        ypoints = np.load(f'{j}/ypoints_1_{i}.npy')
        plt.plot(xpoints, ypoints)
        plt.scatter(4, 4, color='orange', s=40, marker='o')

plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.show()