import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from Experimental_Data import *
from Find_Model import *
from Interpolation import *

def graphExpData():
    fig = plt.figure()
    fig.subplots_adjust(top=1)
    ax1 = fig.add_subplot()
    ax1.set_ylabel('Position')
    ax1.set_xlabel('Time')
    ax1.set_title('Experimental Position vs Time Graph')

    line, = ax1.plot(lab1Data['t'], lab1Data['x'], lw=3)
    plt.show()

graphExpData()

def graphModData():
    fig = plt.figure()
    fig.subplots_adjust(top=1)
    ax1 = fig.add_subplot()
    ax1.set_ylabel('Position')
    ax1.set_xlabel('Time')
    ax1.set_title('Experimental Position vs Time Graph')

    line, = ax1.plot(lab1Data['t'], eval(), lw=3, c='r')
    plt.show()

graphModData()

def graphAllData():
    plt.plot(lab1Data['t'], lab1Data['x'], 'b')
    plt.plot(lab1Data['t'], eval(), 'r')
    plt.show()

graphAllData()