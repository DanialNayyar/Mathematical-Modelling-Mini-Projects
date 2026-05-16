import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm


def normal_with_pdf (n_samples, mu, sigma, bins = 30):
    plt.figure(figsize=(10,10))
    plt.hist(n_samples, bins = bins, density= True, alpha = 0.5, edgecolor = "black")


    x = np.linspace(min(n_samples), max(n_samples), 100)
    y = norm.pdf(x, mu, sigma)

    plt.plot(x, y, color = "red", linewidth = 2, label = "Theoretical PDF")

    plt.title(f"Normal (mu = {mu}, sigma = {sigma}, Empirical vs Theoretical)")
    plt.xlabel("Value")
    plt.ylabel("Probability Density Function")
    plt.legend()
    plt.grid(True, alpha = 0.2)
    plt.show()




def expo_with_pdf (n_samples, lambda_parameter, bins = 30):
    plt.figure(figsize=(10,10))
    plt.hist(n_samples, density= True, alpha = 0.5, edgecolor = "black")


    x = np.linspace(0, max(n_samples), 100)
    y = lambda_parameter * np.exp(-lambda_parameter *x)
    plt.plot(x, y, color = "red", linewidth = 2, label = "Theoretical PDF")


    plt.title(f"Exponential (lambda = {lambda_parameter}), Empirical vs Theoretical)")
    plt.xlabel("Value")
    plt.ylabel("Probability Density Function")
    plt.legend()
    plt.grid(True, alpha = 0.2)
    plt.show()


def uniform_with_pdf (n_samples, a,b, bins = 30):
    plt.figure(figsize=(10,10))
    plt.hist(n_samples, density= True, alpha = 0.5, edgecolor = "black")


    x = np.linspace(a,b, 100)
    y = np.ones_like(x) * (1/(b-a))
    plt.plot(x, y, color = "red", linewidth = 2, label = "Theoretical PDF")


    plt.title(f"Uniform ({a}, {b}), Empirical vs Theoretical)")
    plt.xlabel("Value")
    plt.ylabel("Probability Density Function")
    plt.legend()
    plt.grid(True, alpha = 0.2)
    plt.show()





def hist_continiuous(n_samples,bins = 30, title = "Continuous Distribution"):
    plt.figure(figsize=(10,10))
    plt.hist(n_samples, bins = bins, density = True, edgecolor = "black")
    plt.title(title)
    plt.xlabel("value")
    plt.ylabel("Estimated Probability Density Function (PDF)")
    plt.grid(True, alpha = 0.5)
    plt.show()
    




def bar_discrete(n_samples, title = "Discrete Distribution"):
    values, counts = np.unique(n_samples, return_counts = True)
    probs = counts /counts.sum()

    plt.figure(figsize=(10,10))
    plt.bar(values, probs, alpha = 0.7, edgecolor = "black")
    plt.title(title)
    plt.xlabel("value")
    plt.ylabel("Estimated Probability Density Function (PDF)")
    plt.grid(True, alpha = 0.5)
    plt.show()
    



def cdf_empirical(n_samples):
    samples_sorted = np.sort(n_samples)
    n = len(samples_sorted)

    cdf_values = np.arange(1,n+1)/n
    return samples_sorted, cdf_values


def cdf_plot_norm(n_samples, mu, sigma):
    x_emp, cdf_emp = cdf_empirical(n_samples)

    plt.figure(figsize=(10,10))
    plt.step(x_emp, cdf_emp,  label = "Empirical CDF")

    theo_x = np.linspace(min(n_samples), max(n_samples), 100)
    theo_cdf = norm.cdf(theo_x, loc = mu, scale = sigma)
    plt.plot(theo_x, theo_cdf, color = "red", linewidth = 2, label = "Theoretical CDF")
    

    plt.title(f"Normal (mu = {mu}, sigma = {sigma}) - Empirical vs Theoretical CDF")
    plt.xlabel("Value")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True, alpha = 0.2)
    plt.show()



def cdf_plot_expo(n_samples,lambda_parameter):
    x_emp, cdf_emp = cdf_empirical(n_samples)

    plt.figure(figsize=(10,10))
    plt.step(x_emp, cdf_emp,  label = "Empirical CDF")

    theo_x = np.linspace(0, max(n_samples), 100)
    theo_y = 1- np.exp(-lambda_parameter *theo_x)
    plt.plot(theo_x, theo_y, color = "red", linewidth = 2, label = "Theoretical CDF")
    

    plt.title(f"Exponential (lambda = {lambda_parameter})) - Empirical vs Theoretical CDF")
    plt.xlabel("Value")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True, alpha = 0.2)
    plt.show()



def cdf_plot_uniform (n_samples, a,b, ):
    x_emp, cdf_emp = cdf_empirical(n_samples)

    plt.figure(figsize=(10,10))
    plt.step(x_emp, cdf_emp,  label = "Empirical CDF")

    theo_x = np.linspace(min(n_samples), max(n_samples), 100)
    theo_cdf = np.clip((theo_x - a) / (b - a), 0, 1)
    plt.plot(theo_x, theo_cdf, color = "red", linewidth = 2, label = "Theoretical CDF")
    

    plt.title(f"Uniform {a}, {b}) - Empirical vs Theoretical CDF")
    plt.xlabel("Value")
    plt.ylabel("CDF")
    plt.legend()
    plt.grid(True, alpha = 0.2)
    plt.show()