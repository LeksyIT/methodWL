import matplotlib.pyplot as plt
import numpy as np
for j in range(1,2):
    for i in range(1, 7):
        xpoints = np.load(f'1/xpoints_1_{i}.npy')
        ypoints = np.load(f'1/ypoints_1_{i}.npy')
        plt.plot(xpoints, ypoints)
        plt.scatter(2, 2, color='orange', s=40, marker='o')
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.show()