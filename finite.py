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
#Finite Difference Derivatives first order
def first(f):
    n=len(f)
    h=1/(n-1)
    fx=np.zeros(n)
    fx[0]=(f[1]-f[0])/h
    fx[n-1]=(f[n-1]-f[n-2])/h
    for i in range(1,n-1):
        fx[i]=(f[i+1]-f[i-1])/(2*h)
    return fx
