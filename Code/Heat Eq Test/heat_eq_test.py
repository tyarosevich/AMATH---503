import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 72

x_0 = np.linspace(0, 1, 100)
alpha = 1
a_1 = 12.7324
a_3 = 4.2441
a_5 = 2.5464

def fsoln(x_0, t)
    u = (a_1 * np.exp(-(alpha*np.pi)**2) * np.sin(np.pi * x_0)
    + a_3 * np.exp(- (alpha*3*np.pi)**2) * np.sin(np.pi *3* x_0)
    + a_5 * np.exp(- (alpha*5*np.pi)**2) * np.sin(np.pi *5* x_0))
    return u

u_0 = fsoln(x_0, 0)
