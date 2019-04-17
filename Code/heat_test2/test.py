import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
# rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
# rc('text', usetex=True)
# # Figure dpi
# dpi = 72

x_0 = np.linspace(0, 1, 100)
alpha = 1
a_1 = 12.7324
a_3 = 4.2441
a_5 = 2.5464
a_7 = 1.8189
def fsoln(x, t):
    u = (a_1 * np.exp(-((alpha*np.pi)**2)*t) * np.sin(np.pi * x)
    + a_3 * np.exp(- ((alpha*3*np.pi)**2)*t) * np.sin(np.pi *3* x)
    + a_5 * np.exp(- ((alpha*5*np.pi)**2)*t) * np.sin(np.pi *5* x)
    + a_7 * np.exp(- ((alpha*7*np.pi)**2)*t) * np.sin(np.pi *7* x))
    return u




u_0 = fsoln(x_0, .1)  # type: float

plt.plot(x_0, u_0, 'r')
plt.axis([0, 1, 0, 12])
plt.show()
