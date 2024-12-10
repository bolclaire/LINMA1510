import numpy as np
import matplotlib.pyplot as plt
import csv

# CSV file references

# Simulating data with different time-references
t1 = np.linspace(0,10,100)
y1 = t1**2
t2 = np.linspace(0,10,15)
y2 = t2**2 + t2

# Data extraction

# Pretty-plotting
plt.plot(t1,y1)
plt.plot(t2,y2)
plt.show()