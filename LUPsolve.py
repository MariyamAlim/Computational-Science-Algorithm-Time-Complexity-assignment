#  solves Ax=b by via the decomposition PA = LU

import numpy as np
import scipy.linalg

def LUPsolve(A,b):

    Pt, L, U = scipy.linalg.lu(A) # Computing the decomposition PA = LU with pivoting
    P = Pt.T
    Pb = np.matmul(P, b) # Computing Pb
    y = scipy.linalg.solve_triangular(L, Pb, lower = True) # Solving for y by forward substitution
    x = scipy.linalg.solve_triangular(U, y, lower = False) # Solving for x by backward substitution
    
    return x, L, U, P  # outputs solution x, and numpy arrays L, U and P from PA = LU decomposition
