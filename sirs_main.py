import numpy as np
import random
import math
from SIRS import SIRS
import matplotlib.pyplot as plt

def main():

    size_input = int(input("size of lattice? "))
    p_1 = float(input("probability of getting infected? "))
    p_2 = float(input("probability of recovery? "))
    p_3 = float(input("probability of becoming susceptible ?"))
    simulate = str(input("simulate? (Y/N) "))
    iterations = int(input("number of iterations? "))
    size = (size_input, size_input)

    if simulate == "Y":
        game = SIRS(size, p_1, p_2, p_3)
        game.run(iterations, 10000)


main()