#create poisson distribution for cybersecurity dataset has frequency of cyber attacks per day
import pandas as pd
from scipy.stats import poisson
import matplotlib.pyplot as plt
from distapp.configurations.config import Config

def create_poisson_distribution():
    # Load configuration
    config = Config()
    
    # Load the dataset
    df = pd.read_csv(config.poisson_path)
    
    # Assuming the dataset has a column 'cyber_attacks_per_day'
    data = df['attack_frequency'].values
    
    # Calculate the mean (lambda) for the Poisson distribution
    lambda_ = data.mean()
    
    #separate date and time from the dataset and extract the hour from the time column
    df['time'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['time'].dt.hour
    max_hour = df['hour'].max()

    x = range(0, max_hour)
    
    # Calculate the Poisson PMF for each x value
    pmf = poisson.pmf(x, lambda_)
    
    # Plot the Poisson distribution
    plt.bar(x, pmf, color='blue', alpha=0.7)
    plt.title('Poisson Distribution of Cyber Attacks per Day')
    plt.xlabel('Hourly Cyber Attacks')
    plt.ylabel('Probability')
    plt.xticks(x)
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    create_poisson_distribution()
