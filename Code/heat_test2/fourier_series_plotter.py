import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt



x_0 = np.linspace(0, np.pi, 50) #the x mesh
n = 100 #number in the sum of the fourier series

n_list = np.arange(1,n+1, 1) # an array of integers from 1 to n

#An array of the fourier coefficients. The RHS will have to be updated for every series
A_n_list = (-2/n_list) *(-1)**(n_list)  #/ (n_list*n_list)

# A python list to append to. The internet says this is faster than directly declaring
# a matrix of arrays using numpy
sin_list = []

# Appends arrays to a list. Each row is sin(nx), one row for each n.
# Again this would have to be updated for every fourier series
for i in range(0,n,1):
    sin_list.append(np.sin(n_list[i] * x_0))

#Turns the list of arrays into a numpy matrix
sin_matrix = np.asarray(sin_list)


A_column = A_n_list.reshape(-1, 1) #reshape coefficients for multiplication

#Multiplies each coefficient across the entire corresponding x-mesh
#then sums the columns of the matrix to get the final value u(x, 0).
u = np.sum(A_column*sin_matrix, 0)
#     u = A_n * np.cos(n * t) * np.sin(n*x_0)
#
#     return u




#u_0 = fsoln(n_list, A_n_list, 0)  # type: float

plt.plot(x_0, u, 'r')
plt.axis([0, np.pi, 0, np.pi])
plt.show()
