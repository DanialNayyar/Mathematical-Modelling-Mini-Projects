import numpy as np


def normal_distro(mean_mu, sigma, n_samples):
    n_samples = n_samples// 2
    U1 = np.random.rand(n_samples)
    U2 = np.random.rand(n_samples)
    R = np.sqrt(-2*np.log(U1))
    theta = np.pi*2*U2
    Z1 = R*np.cos(theta)
    Z2 = R * np.sin(theta)
    
    Z = np.concatenate([Z1, Z2])
    
    X = mean_mu + sigma*Z

    return X

print(normal_distro(1,1,100_000))