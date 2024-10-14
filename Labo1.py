import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants (you'll need to set these values)
S_R = 40.0  
q_p = 30  
S_F30 = 0  
S_L30_non_linéaire = 0.158
S_L30_linéaire = 0.314  
g = 981  # Gravitational constant
h_bar = 18.5
K_p_1 = 3
K_p_2 = 10


# Function that represents the ODE dh_3/dt
def dh3_dx(t, h3):
    return (1 / S_R) * q_p - (1 / S_R) * (S_F30 + S_L30_non_linéaire) * np.sqrt(2 * g * h3)
def dh3_dt_linéarise(t, h3_0):
    return A(S_L30_linéaire , S_R , g , h_bar) * h3_0 + B(S_R) * q_p 
def dh3_dx_point_2_non_lineaire(t, h3):
    return (1 / S_R) * (K_p_1 * (q_p - h3)) - (1 / S_R) * (S_F30 + S_L30_non_linéaire) * np.sqrt(2 * g * h3)
def dh3_dx_point_2lineaire(t, h3 ):
    return A(S_L30_linéaire , S_R , g , h_bar) * h3_0 + B(S_R) * (K_p_1 * (h_bar - h3))
def dh3_dx_point_2_non_lineaire_2(t, h3):
    return (1 / S_R) * (K_p_2 * (q_p - h3)) - (1 / S_R) * (S_F30 + S_L30_non_linéaire) * np.sqrt(2 * g * h3)
def dh3_dx_point_2lineaire_2(t, h3 ):
    return A(S_L30_linéaire , S_R , g , h_bar) * h3_0 + B(S_R) * (K_p_2 * (h_bar - h3))
# def q_p() :
#     return K_p*(h_bar - h3_0)
def A(S_L30 , S_R , g , h_bar) : 
    return (-np.sqrt(2*g)*S_L30)/(2*S_R*np.sqrt(h_bar))
def B(S_R) : 
    return 1 / S_R 
def C(S_R , g , h_bar) : 
    return - np.sqrt(2 * g * h_bar) / S_R

# Initial condition for h_3
h3_0 = 0  # Initial value of h_3

# Define the range of x values over which to solve the ODE
t_span = (0, 250)  # Example range for x from 0 to 250

# Call solve_ivp to solve the ODE
solution = solve_ivp(dh3_dx, t_span, [h3_0], method='RK45')
solution_linéarise = solve_ivp(dh3_dt_linéarise, t_span, [h3_0], method='RK45')
solution_point_2_nonlineaire = solve_ivp(dh3_dx_point_2_non_lineaire, t_span, [h3_0], method='RK45')
solution_point_2_lineaire = solve_ivp(dh3_dx_point_2lineaire, t_span, [h3_0], method='RK45')
solution_point_2_nonlineaire_2 = solve_ivp(dh3_dx_point_2_non_lineaire_2, t_span, [h3_0], method='RK45')
solution_point_2_lineaire_2 = solve_ivp(dh3_dx_point_2lineaire_2, t_span, [h3_0], method='RK45')

# Ouvrir le fichier en mode lecture
def read_file(name_file):
    with open(name_file, 'r') as file:
        # Lire toutes les lignes
        lines = file.readlines()

    # Parcourir les lignes, sauter la ligne d'en-tête et extraire les colonnes voulues
    t = []
    tank_level = []
    for line in lines[12:]:  # Sauter la première ligne (en-tête)
        # Séparer les colonnes par les espaces ou tabulations
        columns = line.split()

        # Extraire la première et la troisième colonne
        t.append(columns[0])  # Première colonne
        tank_level.append(columns[2])  # Troisième colonne


        # Afficher les résultats
        # print(f"t [s]: {t}, tank level [cm]: {tank_level}")
    t = [val.replace(',', '.') for val in t]
    tank_level = [val.replace(',', '.') for val in tank_level]
    t = np.array(t, dtype=float)
    tank_level = np.array(tank_level, dtype=float)
    return t , tank_level
t , tank_level = read_file('Labo/LINMA1510/open-loop-30.txt')
t2 , tank_level2 = read_file('Labo/LINMA1510/closed-loop-P3.txt')
t3 , tank_level3 = read_file('Labo/LINMA1510/closed-loop-P10.txt')



# Plotting the solution
plt.figure() 
plt.plot(t , tank_level)
plt.plot(solution.t, solution.y[0])
plt.plot(solution_linéarise.t, solution_linéarise.y[0])
print(t)
print(tank_level)
plt.axhline(y=np.max(solution_linéarise.y[0]), color='r', linestyle='--', label='Max (x={:.2f})'.format(np.max(solution.t)))
plt.legend(['Data(réalité)', 'Non linéaire', 'Linéaire' , ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Solutions of the ODEs")
plt.show()

plt.figure()
# plt.plot(solution_point_2_nonlineaire.t, solution_point_2_nonlineaire.y[0])
plt.plot(t2 , tank_level2)
plt.plot(solution_point_2_lineaire.t, solution_point_2_lineaire.y[0])

print(t)
print(tank_level)
plt.legend(['Data(réalité)', 'linéaire' ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Solutions of the ODEs (K_p = 3)")
plt.show()

plt.figure()
# plt.plot(solution_point_2_nonlineaire_2.t, solution_point_2_nonlineaire_2.y[0])
plt.plot(t3 , tank_level3)
plt.plot(solution_point_2_lineaire_2.t, solution_point_2_lineaire_2.y[0])

print(t)
print(tank_level)
plt.legend(['Data(réalité)', 'linéaire' ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Solutions of the ODEs (K_p = 10)")
plt.show()


