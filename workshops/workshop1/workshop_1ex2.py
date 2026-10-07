# Maximizing quadratic utility
import numpy as np


def util(c, A, B, C):
    u = -A * (c - B) ** 2 + C
    return u


def find_max_cons(candidates, A, B, C):
    """_summary_

    Parameters
    ----------
    candidates : list or array-like
        Sequence of candidate consumption levels to evaluate
    A, B, C : float
        Parameters of the utility function.

    Returns
    ----------
    u_max
        Maximized utility
    cons_max
        Consumption at which utility is maximized
    """

    # Initiliaze u_max to negative infinity
    u_max = -np.inf

    #Loop through all candidate consumption levels and compute the assosciated utility
    #use enumerate or range(len)
    #for i in range(len(candidates)):
    for i, candidate in enumerate(candidates):
        utility = util(candidate, A, B, C)
        # use candidate to go through one value of the array at a time
        if utility > u_max:
            u_max = utility
            cons_max = candidate
    return u_max, cons_max 

candidates = np.linspace(0, 4, 51)
A = 1
B = 2
C = 10

u_max, cons_max = find_max_cons(candidates, A, B, C)

print(u_max, cons_max)



#Repeat the excersize using vectorized NumPy operations
#Vectorized numpy means array

cons = np.linspace(0,4,51)
A,B,C = 1,2,10

utilities = util(cons, A, B, C)

idx = np.argmax(utilities)
u_max = utilities[idx]
cons_max = cons[idx]

print(idx, u_max, cons_max)
