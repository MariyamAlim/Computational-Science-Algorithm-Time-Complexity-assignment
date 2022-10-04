#  analysis of matrix-vector products with 
#    tridiagonal matrix A

import numpy as np
from time import time                     # for timing the banded_matvec function
import matplotlib.pyplot as plt
from Tridiag_Matvec import Tridiag_Matvec   # your banded_matvec function

n_x = []
time_taken = []

# loop over matrix sizes
for i in range(3, 7):

   n = 10 ** i
   n_x.append(n)

   # generate random arrays a, b, c and x using numpy.random.rand or fix them, for instance to all 1s.
   a = np.random.rand(n, 1)
   b = np.random.rand(n, 1)
   c = np.random.rand(n, 1)
   x = np.random.rand(n, 1)

   # start the timer
   begin = time()

   # call Tridiag_Matvec
   y = Tridiag_Matvec(a, b, c, x)

   # stop the timer and store the wall time
   end = time()
   wall_time = end - begin
   time_taken.append(wall_time)

# plot the wall time versus the matrix size on a logarithmic scale along with your prediction
plt.plot(n_x, time_taken)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("Time taken")
plt.title("Time taken vs. n")
plt.show()
