import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lab1Data = pd.read_csv('PHYS2211_LAB1_DATA.csv')

def graphData():
    fig = plt.figure()
    fig.subplots_adjust(top=1)
    ax1 = fig.add_subplot()
    ax1.set_ylabel('Position')
    ax1.set_xlabel('Time')
    ax1.set_title('Experimental Position vs Time Graph')

    line, = ax1.plot(lab1Data['t'], lab1Data['x'], lw=3)
    plt.show()
