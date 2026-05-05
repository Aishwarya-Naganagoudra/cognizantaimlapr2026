#create uniform distribution for datacenter_vm_load_last_24_hours.csv
import pandas as pd
import numpy as np
from scipy.stats import uniform
from distapp.configurations.config import Config
from matplotlib import pyplot as plt
def create_uniform_distribution(data, column_name):
    # Get the minimum and maximum values of the column
    min_value = data[column_name].min()
    max_value = data[column_name].max()
    
    # Create a uniform distribution with the same range as the data
    uniform_dist = uniform(loc=min_value, scale=max_value - min_value)
    
    return uniform_dist

def draw_uniform_distrribution(uniform_dist, size=1000):
    # Draw a histogram of the uniform distribution
    plt.hist(uniform_dist.rvs(size=size), bins=30, density=True, alpha=0.6, color='g') 
    # Plot the PDF of the uniform distribution
    # x = np.linspace(uniform_dist.ppf(0.01), uniform_dist.ppf(0.99), 100)
    x = np.linspace(uniform_dist.kwds['loc'], uniform_dist.kwds['loc'] + uniform_dist.kwds['scale'], 100)
    plt.plot(x, uniform_dist.pdf(x), 'r-', lw=2)
    plt.title('Uniform Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()

if __name__ == "__main__":

    uniform_path = Config().uniform_path
    # Load the dataset
    data = pd.read_csv(uniform_path)
    
    # Create a uniform distribution for the 'load' column
    uniform_dist = create_uniform_distribution(data, 'load_spread')
    
    # Print the parameters of the uniform distribution
    print(f"Uniform Distribution Parameters: loc={uniform_dist.kwds['loc']}, scale={uniform_dist.kwds['scale']}")

    # Draw the uniform distribution
    draw_uniform_distrribution(uniform_dist)