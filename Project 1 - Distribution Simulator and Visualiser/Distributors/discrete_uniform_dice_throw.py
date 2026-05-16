import numpy as np


def dice_throw(n_throws): # Discrete Uniform distributon - equal probability to each value in a finite set

    throws = np.random.randint(1,7, size = n_throws)

    return(throws)    
