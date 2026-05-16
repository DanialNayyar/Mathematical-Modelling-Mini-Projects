import numpy as np

def expo_distro(lambda_param, n_samples):
    
    U = np.random.rand(n_samples)

    X = - ((np.log(1-U) )/ (lambda_param))

    return X

samples = (expo_distro(5,100_000))