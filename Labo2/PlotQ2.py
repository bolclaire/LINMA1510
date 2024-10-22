import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

# Q2 : P, PI, PID controllers, with and without disturbance

time = np.linspace(0,50,200)
ref = np.ones_like(time)

# Peut etre retire
disturbance = np.zeros_like(time)
disturbance[time >= 15] = 0.5

title = ["P controller", "PI controller", "PID controller", "P controller w/ disturbance", "PI controller w/ disturbance", "PID controller w/ disturbance"]
plant_input = ['Controle_P.csv','Controle_PI.csv','Controle_PID.csv','Controle_P_d.csv','Controle_PI_d.csv','Controle_PID_d.csv']
plant_output = ['Controle_P_sum.csv','Controle_PI_sum.csv','Controle_PID_sum.csv','Controle_P_sum_d.csv','Controle_PI_sum_d.csv','Controle_PID_sum_d.csv']


def display_data(title,plant_input,plant_output,d=False) :

    plt.figure(title)

    csv1 = pd.read_csv(plant_input)
    t1,y1 = csv1['COlonne1'],csv1['Colonne2']

    csv2 = pd.read_csv(plant_output)
    t2,y2 = csv2['COlonne1'],csv2['Colonne2']

    plt.figure(title,figsize=(10, 6))
    plt.plot(time,ref,label="Ref input", color='yellow')
    #plt.plot(t1, y1, label="Plant input", color='blue', linewidth=1)
    plt.plot(t2, y2, label="Output", color = 'green')
    if d : 
        plt.plot(time,disturbance, label="Disturbance", color='red')
        title = title + " w/ disturbance"

    plt.title(title)
    plt.xlabel("Time [s]")
    plt.legend()

    plt.grid(True)
    plt.tight_layout()
    plt.show()


for i in range(3) :
    display_data(title[i],plant_input[i],plant_output[i])
    display_data(title[i],plant_input[i],plant_output[i], True)