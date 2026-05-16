import numpy as np



def coin_flip(n_flips): #Bernoulli Distribution (PMF - discrete)
    coin_flips = np.random.randint(0,2, size = n_flips)

    return(coin_flips)
