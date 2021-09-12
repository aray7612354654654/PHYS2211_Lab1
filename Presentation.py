import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from Experimental_Data import *
from Find_Model import *
from Interpolation import *

st.title("""Arya Nahri - PHYS2211 Lab 1 Summary""")

st.write("")
st.write("")
st.write("")

col1, col2, col3 = st.columns(3)

st.write("")
col1.write("***Experimental Data***:")
col1.write(lab1Data)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(
    lab1Data['t'],
    lab1Data['x'],
    c='g'
)

ax.set_xlabel('Time')
ax.set_ylabel('Position')

col1.write("***Experimental Data Graph***:")
col1.write(fig)

col2.write("***Model Data***:")
col2.write(pd.DataFrame(eval(), lab1Data['t']))


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(
    lab1Data['t'],
    eval(),
    c='r'
)

ax.set_xlabel('Time')
ax.set_ylabel('Position')

col2.write("***Model Data Graph***:")
col2.write(fig)

st.write("")
col3.write("***Experimental Correlation Table (Justifies Linear Model)***:")
col3.write(lab1Data.corr())

col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")
col3.write("")

col3.write("***Correlation Graph Between Experimental and Model Data***:")
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(
    x=lab1Data['t'],
    y=eval() / lab1Data['x'],
)

ax.set_xlabel('Time')
ax.set_ylabel('Model Position / Experimental Position')

col3.write(fig)

st.write("")
st.write("***Interpolation Math***:")

with st.echo(code_location='below'):

    class PolyInterpolate:
        def __init__(self, Inputs=[0], Outputs=[0]):
            self.inputs = Inputs
            self.outputs = Outputs
            self.coeffs = np.array([])

        # Returns Vandermonde matrix of polynomial
        def find_vandermonde(self):
            return np.vander(self.inputs)

        # Inverts the Vandermonde matrix
        def invert_vandermonde(self):
            self.find_vandermonde()
            return np.linalg.inv(self.find_vandermonde())

        # Returns the coefficients of the polynomial by matrix multiplying the inverted vandermonde matrix
        # by the vector of outputs
        def find_coefficients(self):
            self.invert_vandermonde()
            self.coeffs = np.matmul(self.invert_vandermonde(), self.outputs)
            self.coeffs = np.flipud(self.coeffs)
            return self.coeffs

        def __repr__(self):
            self.find_vandermonde()
            self.invert_vandermonde()
            self.find_coefficients()
            return f'{self.coeffs}'


    def repeatInterp():
        x = 0
        valLst = []
        while x in lab1Data['t']:
            x += 2
            val = PolyInterpolate(lab1Data['t'][0:x + 1:x], lab1Data['x'][0:x + 1:x])
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