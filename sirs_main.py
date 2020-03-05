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

    size_input = int(sys.argv[1])
    simulate = sys.argv[2]
    size = (size_input, size_input)

    if simulate == "Y":
        p_1 = float(sys.argv[3])
        p_2 = float(sys.argv[4])
        p_3 = float(sys.argv[5])
        p_i = 0.0
        game = SIRS(size, simulate, p_1, p_2, p_3, p_i)
        game.run(10000, 10000)

    elif simulate == "N":
        p_1_range = np.arange(0.0, 1.0, 0.025)
        p_2 = 0.5
        p_3_range = np.arange(0.0, 1.0, 0.025)
        p_i = 0.0
        i_avg_matrix = []
        i_var_matrix = []
        for n in range(len(p_1_range)):
            p_1 = p_1_range[n]
            print(p_1)
            i_avg_list = []
            i_var_list = []
            for m in range(len(p_3_range)):
                p_3 = p_3_range[m]
                print(p_3)
                game = SIRS(size, simulate, p_1, p_2, p_3, p_i)
                infected = []
                for i in range(1100):
                    for j in range(size[0]*size[1]):
                        game.update()
                    if i > 100:
                        infected_sites = game.infected_sites()
                        infected.append(infected_sites)
                
                infected_avg = np.mean(infected)/(size[0]*size[1])
                i_avg_list.append(infected_avg)
                infected_variance = np.var(infected)/(size[0]*size[1])
                i_var_list.append(infected_variance)
            i_avg_matrix.append(i_avg_list)
            i_var_matrix.append(i_var_list)

        #plt.imshow(i_matrix, cmap = 'hot', interpolation = 'nearest', extent = [0,1,1,0])
        #plt.show()


            np.savetxt("phase.txt", np.matrix(i_avg_matrix))
            np.savetxt("waves.txt", np.matrix(i_var_matrix))
            
                    
    elif simulate == "strip":
        p_1_range = np.arange(0.2, 0.51, 0.01)
        p_2 = 0.5
        p_3 = 0.5
        p_i = 0.0
        i_var_list = []
        errors = []
        for n in range(len(p_1_range)):
            p_1 = p_1_range[n]
            print(p_1)       
            game = SIRS(size, simulate, p_1, p_2, p_3, p_i)
            infected = [] 
            for i in range(10100):
                for j in range(size[0]*size[1]):
                    game.update()
                if i > 100:
                    infected.append(game.infected_sites())                                                   
            infected_variance = np.var(infected)/(size[0]*size[1])
            i_var_list.append(infected_variance)
            errors.append(game.bootstrap(infected))
            print(i_var_list)

        with open("p_3_var.txt", "w+") as f:
            f.writelines(map("{}, {}, {}\n".format, p_1_range, i_var_list, errors))

    elif simulate == "immunity":
        p_1 = 0.5
        p_2 = 0.5
        p_3 = 0.5
        p_i_range = np.arange(0.0, 0.51, 0.01)
        i_avg_matrix= []
        errors = []
        for r in range(5):
            i_avg_list = []
            for n in range(len(p_i_range)):
                p_i = p_i_range[n]
                print(p_i)
                infected = []
                game = SIRS(size, simulate, p_1, p_2, p_3, p_i)
                for i in range(1100):
                    for j in range(size[0]*size[1]):
                        game.update()
                    if i > 100:
                        infected.append(game.infected_sites()) 
                infected_avg = np.mean(infected)/(size[0]*size[1])
                i_avg_list.append(infected_avg)
            i_avg_matrix.append(i_avg_list)
            print(i_avg_matrix)
        for vals in np.transpose(i_avg_matrix):
            errors.append(np.std(vals)/math.sqrt(len(vals)))
        infected_final = np.mean(i_avg_matrix, axis=0)
        print(infected_final)

        with open("immunity.txt", "w+") as f:
            f.writelines(map("{}, {}, {}\n".format, p_i_range, infected_final, errors))



main()