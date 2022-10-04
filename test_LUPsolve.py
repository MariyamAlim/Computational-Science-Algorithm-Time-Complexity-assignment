import pytest as pt
import numpy as np
from LUPsolve import LUPsolve
    
    
class TestLUPsolve:

    n = 25
    A = np.random.rand(n,n)
    b = np.random.rand(n,1)
    x,L,U,P = LUPsolve(A,b)


    def test_residual(self):
        assert np.linalg.norm(self.A@self.x-self.b,2)<=1.0e-6
    
    def test_decomp(self):
        assert np.linalg.norm(self.P@self.A-self.L@self.U,2)<=1.0e-6
    
    