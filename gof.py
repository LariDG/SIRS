"""
Modelling and Visulaisation in Physics
Checkpoint 2: SIRS
Main for Game of Life.
To run the simulation from the class as well as plotting a histogram
of time till the game of life equilibrates and a plot of the glider velocity.
Author: Larisa Dorman-Gajic
"""
import numpy as np
import random
import math
from game_of_life import Game_of_Life
import matplotlib.pyplot as plt

def main():


    size_input = int(input("size of lattice? "))
    state = str(input("initialise with random, oscillator or glider? "))
    simulate = str(input("simulate? (Y/N) "))
    iterations = int(input("number of iterations? "))
    size = (size_input, size_input)
    

    if simulate == "Y":
        game = Game_of_Life(size, state)
        game.run(iterations, 1)

    else:
        if state == "random":
            time_to_stop = []
            for i in range(150):
                print(i)
                alive = []
                game = Game_of_Life(size, state)
                inEquilibrium = False
                while not inEquilibrium:
                    game.parallel_update()
                    l_after = np.sum(game.lattice)
                    alive.append(l_after)
                    if len(alive) > 4:
                        if alive[-1] == alive[-2] and alive[-2] == alive[-3] and alive[-3] == alive[-4]:
                            time_to_stop.append(len(alive)-4)
                            inEquilibrium = True
                print(time_to_stop[i])                    

            
            plt.hist(time_to_stop, np.arange(0,3500,50))
            plt.show()

        if state == "glider":
            file_handle = open("Glider_velocity.dat", "w+")
            x_t = []
            time = []
            game = Game_of_Life(size, state)
            for t in range(1000):
                com_x = game.centre_mass()
                if  7  < com_x < size_input - 7 and t % 10 == 0 :
                    print(com_x, t)
                    x_t.append(com_x)
                    time.append(t)
                game.parallel_update()

            for i in range(len(time)):
                file_handle.write(str(time[i]) + " " + str(x_t[i]) + "\n")
            file_handle.close()

            plt.title("velocity of glider")
            plt.xlabel("Time")
            plt.ylabel("Centre of Mass (x(t))")
            plt.plot(time, x_t)
            plt.show()                    
main()