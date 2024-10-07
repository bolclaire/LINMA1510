import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants (you'll need to set these values)
S_R = 1.0  # Example value for S_R
q_p = 5  # Example value for q_p
S_F30 = 0  # Example value for S_F30
S_L30 = 1.0  # Example value for S_L30
g = 9.81  # Gravitational constant

# Function that represents the ODE dh_3/dt
def dh3_dx(t, h3):
    return (1 / S_R) * q_p - (1 / S_R) * (S_F30 + S_L30) * np.sqrt(2 * g * h3)

# Initial condition for h_3
h3_0 = 0  # Initial value of h_3

# Define the range of x values over which to solve the ODE
t_span = (0, 10)  # Example range for x from 0 to 10

# Call solve_ivp to solve the ODE
solution = solve_ivp(dh3_dx, t_span, [h3_0], method='RK45')

# Plotting the solution
plt.plot(solution.t, solution.y[0])
plt.xlabel('x')
plt.ylabel('h_3')
plt.title('Solution of the ODE')
plt.show()
