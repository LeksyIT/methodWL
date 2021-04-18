import matplotlib.pyplot as plt
import numpy as np


def rk4(r, t, h):
    """ Runge-Kutta 4 method """
    k1 = h * func(r, t)
    k2 = h * func(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * func(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * func(r + k3, t + h)
    return (k1 + 2 * k2 + 2 * k3 + k4) / 6


def func(r, t):
    x, y = r[0], r[1]
    fxd = x * (emps1 - alpha1 * y)
    fyd = -y * (emps2 - alpha2 * x)
    return np.array([fxd, fyd], float)


h = 0.001
emps1 = 5
alpha1 = 2.5
emps2 = 2
alpha2 = 1
tpoints = np.arange(0, 30, h)
x_0 = 2
y_0 = 2
for i in range(1, 7):
    xpoints, ypoints = [], []
    r = np.array([x_0 + i, y_0 + i], float)
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        r += rk4(r, t, h)
    plt.plot(xpoints, ypoints)
    plt.scatter(2, 2, color='orange', s=40, marker='o')
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.show()
