import pytest as pt
import numpy as np
from Tridiag_Matvec import Tridiag_Matvec

def test_execution():
    n = 500
    a = np.random.rand(n,1)           # Set up random tridiagonal matrix and right hand side
    b = np.random.rand(n,1)
    c = np.random.rand(n,1)
    x = np.random.rand(n,1)

    A = np.zeros((n,n))
    A[0,0] = b[0]
    A[0,1] = c[0]
    for i in range(1,n-1):
        A[i,i-1] = a[i]
        A[i,i] = b[i]
        A[i,i+1] = c[i]
    A[n-1,n-2] = a[n-1]
    A[n-1,n-1] = b[n-1]

 #   print(np.linalg.norm((np.dot(A,x) - Tridiag_Matvec(a,b,c,x)), 2) <= 1e-6)

    assert np.linalg.norm((np.matmul(A,x) - Tridiag_Matvec(a,b,c,x)), 2) <= 1e-6