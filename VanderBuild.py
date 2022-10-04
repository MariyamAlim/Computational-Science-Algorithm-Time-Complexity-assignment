#  builds the Vandermonde matrix

import numpy as np


def VanderBuild(N):  # inputs integer N

    x = []            # Stores values of xi for i = 0,....,N
    sum = 0
    step = 1 / N      # Stores the difference between 2 consecutive xi values
    V = np.empty([N + 1, N + 1]) # Stores the Vandermonde matrix

    for i in range(N + 1):
        for j in range(N + 1):
            x.append(sum)       # Append sum to list 'x'
            sum += step         # Update value of 'sum' by adding 'step' to it
            V[i, j] = x[i]**j   # Set entry in 'V'

    return V   # outputs the N+1 x N+1 numpy array with Vandermonde matrix
