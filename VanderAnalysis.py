#  analysis of linear systems involving Vandermonde matrix

from VanderBuild import VanderBuild
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

rel_err = []
max_rel_err = []
n = []

# loop over matrix sizes
for i in range(15, 26):

   N = i
   n.append(N)

   # call VanderBuild to get V
   V = VanderBuild(N)
   cond = np.linalg.cond(V, 2)
   
   # form the vector c (the right hand side of the equation Vx=c)
   c = V[:, N]

   # compute solution x_exact
   x_exact = np.zeros(N + 1)
   x_exact[N] = 1
   
   # compute the error
   s = scipy.linalg.solve(V, c) # Approximate solution of Vx = c

   r = np.matmul(V, s) - c # Residual vector
   res = np.linalg.norm(r, 2) # Calculating residual
   
   e = x_exact - s # Error vector
   err = np.linalg.norm(e, 2) # Calculating relative error
   rel_err.append(err) # Append relative error to list 'rel_err'
   
   # compute the max relative error
   m = cond * res / np.linalg.norm(c, 2) # Calculating maximal relative error
   max_rel_err.append(m) # Append maximal relative error to list 'max_rel_err'


# plot error and max relative error versus the matrix size on a logarithmic scale on the y-axis (semilogy)
plt.plot(n, rel_err)
plt.plot(n, max_rel_err)
plt.yscale("log")
plt.xlabel("N")
plt.ylabel("Errors")
plt.legend(["Relative error", "Maximal relative error"])
plt.show()






