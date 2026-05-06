#create exponential distribution from angola_population.csv dataset
import pandas as pd
import numpy as np
from scipy.stats import expon
from distapp.configurations.config import Config
import matplotlib.pyplot as plt
def create_exponential_distribution():
    config = Config()
    #load dataset
    df = pd.read_csv(config.exponential_path)
    #range of years
    t=np.arange(df['year'].min(), df['year'].max()+1, 1)
    #get population column
    population = df['population'].values
    #fit exponential distribution to data
    loc, scale = expon.fit(population)
    #generate random numbers from exponential distribution
    random_numbers = expon.rvs(loc=loc, scale=scale, size=100)
    return random_numbers,t,population

def draw_exponential_distribution(random_numbers,t,population):
    plt.figure(figsize=(10, 6))    
   
    #plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='g')
    plt.plot(t, population, marker='o', linestyle='-', color='b')
    plt.title('Exponential Population Growth in Angola')
    plt.xlabel('year')
    plt.ylabel('Density')
    plt.show()

if __name__ == "__main__":
    random_numbers, t, population = create_exponential_distribution()
    draw_exponential_distribution(random_numbers,t,population)