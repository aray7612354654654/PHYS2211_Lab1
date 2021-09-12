import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Interpolation import *
from Experimental_Data import *

"""Imputing a mathematical model via polynomial interpolation"""

function = PolyInterpolate(lab1Data['t'][0:2], lab1Data['x'][0:2])
coeffs = function.find_coefficients()

# The correlation table shows that the experimental graph is essentially linear,
# thus it is reasonable to assume constant velocity.
print(lab1Data.corr())

print('\n*******************************************************\n')

# Because the velocity is roughly constant, a linear (1-degree) mathematical model will work well.
print(coeffs)

print(lab1Data)

print('\n*******************************************************\n')

print(coeffs)

print('\n*******************************************************\n')

def repeatInterp():
    x = 0
    valLst = []
    while x in lab1Data['t']:
        x += 2
        val = PolyInterpolate(lab1Data['t'][0:x+1:x], lab1Data['x'][0:x+1:x])
        valLst.append(val.find_coefficients())
    return valLst

def eval():
    valLst = []
    for x in lab1Data['t']:
        val = np.mean(repeatInterp(), dtype=object)[0] + np.mean(repeatInterp(), dtype=object)[1] * x
        valLst.append(val)
    return valLst

print("Repeated Interpolation:")
print(repeatInterp())

print('\n*******************************************************\n')

print("Standard Dev:")
print(np.std(repeatInterp(), dtype=object))

print('\n*******************************************************\n')

print("Average:")
print(np.mean(repeatInterp(), dtype=object))

print('\n*******************************************************\n')

print("The model evaluated at each t:")
print(eval())