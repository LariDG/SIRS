"""
Modelling and Visulaisation in Physics
Checkpoint 2: SIRS
Main for SIRS model.
To run the simulation from the class as well as plotting a phase diagram 
based on the changing probabailities of S --> I and R --> S.
Author: Larisa Dorman-Gajic
"""
import numpy as np
import random
import math
from SIRS import SIRS
import matplotlib.pyplot as plt
import sys

def main():

    size_input = sys.argv[1]
    simulate = sys.argv[2]
    size = (50, 50)

    if simulate == "Y":
        p_1 = 0.8
        p_2 = 0.1
        p_3 = 0.01
        game = SIRS(size, p_1, p_2, p_3)
        game.run(10000, 10000)

    if simulate == "N":
        p_1_range = np.arange(0, 1, 0.025)
        p_2 = 0.5
        p_3_range = np.arange(0, 1, 0.025)
        i_matrix = []
        i_matrix.append([0.0]*len(p_3_range), [0.0]*len(p_3_range), [0.0]*len(p_3_range), [0.0]*len(p_3_range))
        for n in range(4, len(p_1_range)):
            p_1 = p_1_range[n]
            print(p_1)
            i_avg_list = [0.0, 0.0, 0.0, 0.0]
            for m in range(4, len(p_3_range)):
                p_3 = p_3_range[m]
                print(p_3)
                game = SIRS(size, p_1, p_2, p_3)
                infected = []
                for i in range(1100):
                    for j in range(size[0]*size[1]):
                        game.update()
                    if i > 100:
                        infected_sites = game.infected_sites()
                        print(infected_sites)
                        infected.append(infected_sites)
                infected_avg = np.mean(infected)/(size[0]*size[1])
                i_avg_list.append(infected_avg)
            i_matrix.append(i_avg_list)
        print(i_matrix)

        plt.imshow(i_matrix, cmap = 'hot', interpolation = 'nearest', extent = [0,1,1,0])
        plt.show()

        numpy_matrix = np.matrix(i_matrix)
        np.savetxt("phase.txt", numpy_matrix)
            

        
        


                        



main()