import pytest as pt
import numpy as np
from VanderBuild import VanderBuild

def test_vander():
    n = 4

    A = np.array([[1.        , 0.        , 0.        , 0.        , 0.        ],
       [1.        , 0.25      , 0.0625    , 0.015625  , 0.00390625],
       [1.        , 0.5       , 0.25      , 0.125     , 0.0625    ],
       [1.        , 0.75      , 0.5625    , 0.421875  , 0.31640625],
       [1.        , 1.        , 1.        , 1.        , 1.        ]]) 
    
    V = VanderBuild(n)
    
#    print(np.linalg.norm(A-V,2) <= 1.0e-6)
    
    assert np.linalg.norm(A-V,2) <= 1.0e-6