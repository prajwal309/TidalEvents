import numpy as np
import matplotlib.pyplot as plt


def CreateBasisVector(x, mu, sigma, period):
    return np.exp(-((x%period - mu) ** 2) / (2 * sigma ** 2))


def MexicanHat(x, sigma, period):
    return (2 / (np.sqrt(3 * sigma) * (np.pi ** 0.25))) * (1 - ((x) ** 2) / sigma ** 2) * np.exp(-((x) ** 2) / (2 * sigma ** 2))



time = np.linspace(-10, 10, 10000)
Basis1 = CreateBasisVector(time, 5, 1, 10)
Basis2 = MexicanHat(time, 1, 10)

plt.figure()
plt.plot(time, Basis1, "k-")
plt.plot(time, Basis2, "r-")
plt.xlabel("Time")
plt.ylabel("Basis Function")
plt.tight_layout()
plt.show()