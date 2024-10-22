import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Q1 : Model identification

csv_exp = pd.read_csv('Open-loop.csv')
csv_sim = pd.read_csv('Open-loop-sim.csv')

t1,y1 = csv_exp['time'],csv_exp['concentration']  
t2,y2 = csv_sim['time'],csv_sim['concentration'] 

plt.figure(figsize=(10, 6))
plt.plot(t1, y1, label="Experiment", color='blue', linewidth=1)
plt.plot(t2, y2, label="Simulation", color='red', linewidth=2)

plt.title("Model identification: First-order TF")
plt.xlabel("Time [s]")
plt.ylabel("Concentration")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()

# Q2 : P, PI, PID controllers, with and without disturbance

csv = pd.read_csv('Controle')