"""
Modelling and Visualisation in Physics
Checkpoint 2: SIRS
Class to produce a 2 dimensional lattice of live and dead cells
via the Game of Life model.
Author: Larisa Dorman-Gajic
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import math 


class Game_of_Life(object):
    def __init__(self, size, state):
        self.size = size
        self.state = state
        self.build()

    def build(self):

        if self.state == "random":
            self.lattice = np.random.choice(a=[0,1], size=self.size)

        if self.state == "oscillator":
            self.lattice = np.zeros(self.size)
            self.lattice[25:28,25:26] = self.oscillator()

        if self.state == "glider":
            self.lattice = np.zeros(self.size)
            self.lattice[1:4, 1:4] = self.glider()

    def pbc(self, indices):

        return(indices[0]%self.size[0], indices[1]%self.size[1])


    def oscillator(self):
        
        return np.ones((3,1))

    def glider(self):

        a = np.array([0,1,0])
        b = np.array([0,0,1])
        c = np.ones((1,3))
        return np.block([[a], [b], [c]])

    def neighbours(self, indices):

        n, m = indices
        north = self.lattice[self.pbc((n+1, m))]
        north_east = self.lattice[self.pbc((n+1,m+1))]
        east = self.lattice[self.pbc((n,m+1))]
        south_east = self.lattice[self.pbc((n-1,m+1))]
        south = self.lattice[self.pbc((n-1,m))]
        south_west = self.lattice[self.pbc((n-1,m-1))]
        west = self.lattice[self.pbc((n,m-1))]
        north_west = self.lattice[self.pbc((n+1,m-1))]
        neighbours =  north + north_east + east + south_east + south + south_west + west + north_west
        return neighbours

    def parallel_update(self):
        lattice_update = np.zeros(self.size)
        for n in range(self.size[0]):
            for m in range(self.size[1]):
                if self.lattice[n,m] == 1 and self.neighbours((n, m)) == 2 or self.neighbours((n, m)) == 3:
                    lattice_update[n,m] = 1
                elif self.lattice[n,m] == 0 and self.neighbours((n,m)) == 3:
                    lattice_update[n,m] = 1

        self.lattice = lattice_update

    def end(self, alive):
        for i in range(len(alive)-5):
            if alive[i] == alive[i + 1] and alive[i] == alive[i + 2] and alive[i] == alive[i + 3] and alive[i] == alive[i + 4]:
                return i

    def centre_mass(self):
        sum_x = []
        for n in range(5, self.size[0]-5):
            for m in range(5, self.size[1]-5):
                if self.lattice[n,m] == 1:
                    sum_x.append(n)    
        com_x = (np.sum(sum_x)/len(sum_x))
        return com_x




   
    def run(self, iterations, it_per_frame):
        """
        method running the data into FuncAnimation
        """
        self.it_per_frame = it_per_frame
        self.figure = plt.figure()
        self.image = plt.imshow(self.lattice, animated=True)
        self.animation = animation.FuncAnimation(self.figure, self.animate, repeat=False, frames=iterations, interval=100, blit=True)
        plt.show()

    def animate(self, *args):
        """
        a loop to but data into animation
        """
        self.parallel_update()
        self.image.set_array(self.lattice)
        return self.image,


    

