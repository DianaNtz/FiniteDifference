"""
The code below was written by https://github.com/DianaNtz and
is an implementation of the Finite Difference Derivatives.
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt
#create grids with 3 different resolutions.
nx1=30
h1=1/(nx1-1)
x1=np.linspace(0,1,nx1+1)

nx2=nx1*2
h2=1/(nx2-1)
x2=np.linspace(0,1,nx2+1)

nx3=nx2*2
h3=1/(nx3-1)
x3=np.linspace(0,1,nx3+1)
