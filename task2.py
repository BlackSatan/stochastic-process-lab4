import random
from numpy import dot
from numpy import linalg as LA


def find_position_in_range(position, t_range):
    for index, value in enumerate(t_range):
        position -= float(value)
        if position < 0:
            return index
    return 2

TRANSITION = [
    [0, 1, 2.0/5],
    [1.0/5, 0, 3.0/5],
    [4.0/5, 0, 0]
]
TRANSITION_START = []
for i in range(0, 3):
    rest = 1 - sum(TRANSITION_START)
    if rest < 2:
        rest *= random.random()
    TRANSITION_START.append(rest)
LOG = []
M = random.random()

#Defines start position by random, comment next line if you want to use direct setting of start position
LOG.append(find_position_in_range(M, TRANSITION_START))
ITERATION_COUNT = 20

for i in range(1, ITERATION_COUNT):
    M = random.random()
    LOG.append(find_position_in_range(M, dot(TRANSITION_START, LA.matrix_power(TRANSITION, i))))
print LOG
