import random
from numpy import dot
from numpy import linalg as LA


def find_position_in_range(position, t_range):
    for index, value in enumerate(t_range):
        position -= float(value)
        if position <= 0:
            return index
    return 0

TRANSITION = [
    [0, 0.5, 2.0/5],
    [1.0/5, 0.5, 3.0/5],
    [4.0/5, 0, 0]
]
TRANSITION_START = [1, 0, 0]
LOG = []
M = random.random()

#Defines start position by random, comment next line if you want to use direct setting of start position
LOG.append(find_position_in_range(M, TRANSITION_START))
ITERATION_COUNT = 20

for i in range(1, ITERATION_COUNT):
    M = random.random()
    LOG.append(find_position_in_range(M, dot(TRANSITION_START, LA.matrix_power(TRANSITION, i))))
print LOG
