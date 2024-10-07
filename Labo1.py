import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import csv

filename = "open-loop-simulation.csv"

# Constants (you'll need to set these values)
S_R   = 40.0     # Section of the cylinder tank (T3) (cm^2)
q_p   = 5.00     # Pump flow to the tank (control system input) (mL/s)
S_F30 = 0.00     # Front valve surface (characterizes the control system modeled disturbance) (cm^2)
S_L30 = 1.00     # Left valve surface (parameter to compute)
g     = 9.81     # Gravitational constant

# h3 is the height of the water in the tank (= control system output) (cm)

# Function that represents the ODE dh_3/dt
def dh3_dx(t, h3):
    return (1 / S_R) * q_p - (1 / S_R) * (S_F30 + S_L30) * np.sqrt(2 * g * h3)

# Initial condition for h_3
h3_0 = 0  # Initial value of h_3

# Define the range of x values over which to solve the ODE
t_span = (0, 250)  # Example range for x from 0 to 10

# Call solve_ivp to solve the ODE
solution = solve_ivp(dh3_dx, t_span, [h3_0], method='RK45')

# Plotting the solution
plt.plot(solution.t, solution.y[0]) # what are the other dimensions of y ?
plt.xlabel('x')
plt.ylabel('h_3')
plt.title('Solution of the ODE')
plt.show()

# Saving the data
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["t", "h3"])  # Header

    for t in solution.t:
        for y in solution.y[0]:
            writer.writerow([t, y])

# Computing rise time, settling time
# TODO : ensure it is necessary and do it only in this case