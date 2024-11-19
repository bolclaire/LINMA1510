import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def read_file(name_file):
    with open(name_file, 'r') as file:
        # Lire toutes les lignes
        lines = file.readlines()

    # Parcourir les lignes, sauter la ligne d'en-tête et extraire les colonnes voulues
    t = []
    tank_level = []
    for line in lines[12:]:  # Sauter la première ligne (en-tête)
        # Séparer les colonnes par les espaces ou tabulations
        columns = line.split(',')
        # Extraire la première et la troisième colonne
        t.append(columns[0])  # Première colonne
        tank_level.append(columns[1])  # Troisième colonne
        

        # Afficher les résultats
        # print(f"t [s]: {t}, tank level [cm]: {tank_level}")
    t = [val.replace(',', '.') for val in t]
    tank_level = [val.replace(',', '.') for val in tank_level]
    t = np.array(t, dtype=float)
    tank_level = np.array(tank_level, dtype=float)
    return t , tank_level
t , tank_level = read_file('Labo/LINMA1510/Labo2/Controle_P_sum.txt')
t1 , tank_level1 = read_file('Labo/LINMA1510/Labo2/Controle_P.txt')

t2 , tank_level2 = read_file('Labo/LINMA1510/Labo2/Controle_PI_sum.txt')
t3 , tank_level3 = read_file('Labo/LINMA1510/Labo2/Controle_PI.txt')

t4 , tank_level4 = read_file('Labo/LINMA1510/Labo2/Controle_PID_sum.txt')
t5, tank_level5 = read_file('Labo/LINMA1510/Labo2/Controle_PID.txt')

# Plotting the solution
plt.figure() 
plt.plot(t , tank_level)
plt.plot(t1 , tank_level1)
plt.legend(['Sum', 'Non linéaire', 'Linéaire' , ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Solutions of the ODEs")
plt.grid(True)
plt.tight_layout()
# plt.show()


plt.figure() 
plt.plot(t2 , tank_level2)
plt.plot(t3 , tank_level3)

plt.legend(['Sum', 'Non linéaire', 'Linéaire' , ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Solutions of the ODEs")
plt.grid(True)
plt.tight_layout()
# plt.show()

plt.figure()
plt.plot(t4 , tank_level4)
plt.plot(t5 , tank_level5)

plt.legend(['Sum', 'Non linéaire', 'Linéaire' , ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Solutions of the ODEs")
plt.grid(True)
plt.tight_layout()
# plt.show()

plt.figure()
plt.plot(t , tank_level)
plt.plot(t2 , tank_level2)
plt.plot(t4 , tank_level4)

plt.legend(['Output Controller P', 'Output Controller PI', 'Output Controller PID' , ])
plt.xlabel('Times [sec]')
plt.ylabel('h[cm]')
plt.title("Output of the Controllers")
plt.grid(True)
plt.tight_layout()
plt.show()