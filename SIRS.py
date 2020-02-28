import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import math 


class SIRS(object):
    def __init__(self, size, p_1, p_2, p_3):
        """
        initialising the SIRS model

        :param size: size of 2d lattice as tuple
        :param p_1: probability of S ---> I
        :param p_2: probability of I ---> R
        :param p_3: probability of R ---> S
        """
        self.size = size
        self.p_1 = p_1
        self.p_2 = p_2
        self.p_3 = p_3
        self.build()

    def build(self):
        self.lattice = np.random.choice(a=[-1,0,1], size=self.size)

    def pbc(self, indices):

        return(indices[0]%self.size[0], indices[1]%self.size[1])  

    def s_update(self, indices):

        n, m = indices
        north = self.lattice[self.pbc((n+1, m))]
        east = self.lattice[self.pbc((n, m+1))]
        south = self.lattice[self.pbc((n-1, m))]
        west = self.lattice[self.pbc((n, m-1))]
        neighbours = [north, south, east, west]
        if 0 in neighbours:
            r = np.random.rand() 
            if r <= self.p_1:
                self.lattice[indices] = 0

    def i_update(self, indices):
        if np.random.rand() <= self.p_2:
            self.lattice[indices] = -1

    def r_update(self, indices):
        if np.random.rand() <= self.p_3:
            self.lattice[indices] = 1

    def update(self):
        indices = (np.random.randint(0, self.size[0]), np.random.randint(0, self.size[1]))
        if self.lattice[indices] == 1:
            self.s_update(indices)
        elif self.lattice[indices] == 0:
            self.i_update(indices)
        elif self.lattice[indices] == -1:
            self.r_update(indices)

    def infected_sites(self):
        infected_sites = 0
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.lattice[i, j] == 0:
                    infected_sites += 1
                else:
                    infected_sites += 0
        return infected_sites

    
   
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
        for i in range(self.it_per_frame):
            self.update()
        self.image.set_array(self.lattice)
        return self.image,




