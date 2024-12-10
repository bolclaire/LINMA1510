import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


import numpy as np

import numpy as np

def read_file(name_file):
    with open(name_file, 'r') as file:
        # Lire toutes les lignes du fichier
        lines = file.readlines()

    # Initialiser les listes pour stocker les données
    t = []
    tank_level1 = []
    tank_level2 = []
    tank_level3 = []

    # Parcourir les lignes utiles (à partir de la 13ème, car 12 lignes d'en-tête)
    for line in lines[12:]:
        # Supprimer les espaces ou caractères inutiles
        line = line.strip()

        # Remplacer les tabulations par des espaces pour unifier le séparateur
        line = line.replace('\t', ',')

        # Séparer les colonnes par la virgule
        columns = line.split(',')
        np.set_printoptions(threshold=np.inf)  # Supprime la limite d'affichage
        print(columns)
        # Vérifier qu'il y a suffisamment de colonnes pour éviter une erreur d'indice
        if len(columns) < 6:
            print(f"Ligne ignorée (pas assez de colonnes) : {line}")
            continue

        try:
            # Extraire les colonnes nécessaires
            t.append((columns[0] +","+ columns[1]).replace(',', '.'))
            tank_level1.append((columns[6] +","+ columns[7]).replace(',', '.'))
            tank_level2.append((columns[8]+","+columns[9]).replace(',', '.'))
            tank_level3.append((columns[10]+","+columns[11]).replace(',', '.'))
        except Exception as e:
            print(f"Erreur de traitement sur la ligne : {line}\n{e}")
            continue
    # Convertir les listes en tableaux numpy avec des valeurs flottantes
    try:
        t = np.array(t, dtype=float)
        tank_level1 = np.array(tank_level1, dtype=float)
        tank_level2 = np.array(tank_level2, dtype=float)
        tank_level3 = np.array(tank_level3, dtype=float)

    except ValueError as e:
        print(f"Erreur de conversion en float : {e}")
        raise
    return t, tank_level1, tank_level2, tank_level3


t , tank_level1 , tank_level2 , tank_level3 = read_file('Labo3\Equilibrium_flow1.txt')
plt.figure() 
plt.plot(t , tank_level1)
plt.plot(t , tank_level2)
plt.plot(t , tank_level3)
plt.legend(['Tank1', 'Tank2', 'Tank3' , ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Height of the tanks (Equilibirum)")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('Labo3\plot1.png')
t , tank_level1 , tank_level2 , tank_level3 = read_file('Labo3\Equilibrium_flow2b.txt')
plt.figure() 
plt.plot(t , tank_level1)
plt.plot(t , tank_level2)
plt.plot(t , tank_level3)
plt.legend(['Tank1', 'Tank2', 'Tank3' , ])
plt.xlabel('t[sec]')
plt.ylabel('h_3[cm]')
plt.title("Height of the tanks (Gramian)")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig('Labo3\plot2.png')






