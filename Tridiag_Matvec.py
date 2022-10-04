# function for computing the matrix vector product 
#    where A is a tridiagonal matrix
import numpy as np

def Tridiag_Matvec(a,b,c,x):
    
    n = np.size(x)
    y = np.empty([n, 1]) # Creating n x 1 matrix of zeroes

    # Calculating first entry of y
    y[0] = b[0] * x[0] + c[0] * x[1]
    
    # Calculating all entries of y (except for rows 1 and n)
    for i in range(1, n - 1):
        y[i] = a[i] * x[i - 1] + b[i] * x[i] + c[i] * x[i + 1]

    # Calculating last entry of y
    y[n - 1] = a[n - 1] * x[n - 2] + b[n - 1] * x[n - 1]


    return y   # y = Ax
