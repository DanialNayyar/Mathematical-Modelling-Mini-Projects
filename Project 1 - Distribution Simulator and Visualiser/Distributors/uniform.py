import numpy as np


#PDF - Continuous data
# This is a continuous sample using a linear transformation

def uniform(a,b,n_samples): #continous stream of equally random values, between a and b. Theoretical mean = (a+b) /2
    U = np.random.rand(n_samples) # the probability denisty function of this is flat.

    X = U*(b-a) + a #scaled by (b-a), then shifted by a

    #print(f"U= {U}, a = {a}, b={b}, X = {X}")
    return X

samples = uniform(a=5,b=10, n_samples=100_000)

mean = np.mean(samples)

#print(mean)
