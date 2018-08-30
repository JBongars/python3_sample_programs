
# ================================================================================================
# Problem
# ================================================================================================
# Suppose you live in a city where the streets are arranged in a perfect grid and decide to
# go for a walk. At each intersection you choose your direction randomly with choices such as
# north, south, east and west (back tracking is permitted). Eventually, you get tired and
# decide to take a taxi if you are 7 or more blocks away or walk otherwise. What is the
# minimum number of steps you must take so that on average, you will take a cab back?
#
# Hint: using Python, you are able to simulate this senario tens of thousands of times in milliseconds
#
# ================================================================================================

import numpy # meat and potatoes
from random import random

ITERATIONS = 10000
PERCENTILE = 0.5000

randNegPos_old = lambda: numpy.random.choice([-1, 1]) # this is slower
randNegPos = lambda: ((random() >= 0.5000) * 2) - 1 # this is faster

def randomWalk(steps):
    position = 0
    for i in range(steps):
        position += randNegPos()
    return position

def monteCarlo(blocks):
    data = []
    steps = 1

    while True:
        for i in range(ITERATIONS):
            data.append(abs(randomWalk(steps)) > blocks)
        
        print("For steps %s, the average is %.4f" %(steps, numpy.average(data)))
        if numpy.average(data) > PERCENTILE:
            return steps
        else:
            data = []
            steps += 1

def go():
    while True:
        try:
            blocks = int(input("Please select the number of blocks you want to calculate (1 to 20): "))
            result = monteCarlo(7)
            print("Final solution: %d steps" %(result))
            input("Press any key to continue...")
            return
        except(NameError, ValueError):
            print("Value entered is invalid. Please try again...")



        
