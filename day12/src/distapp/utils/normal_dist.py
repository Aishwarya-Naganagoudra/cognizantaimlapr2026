#create normal distribution for trainees score data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from distapp.configurations.config import Config
def calculate_normal_distribution():
    config = Config()
    data = pd.read_csv(config.csv_path)
    scores = data['Score']
    mean = np.mean(scores)
    std_dev = np.std(scores)
    x = np.linspace(min(scores), max(scores), 1000)
    pdf = norm.pdf(x, mean, std_dev)
    return x, pdf, mean, std_dev

def plot_normal_distribution(x, pdf, mean, std_dev):
    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, color='blue', label='Normal Distribution')
    plt.title(f'Normal Distribution of Trainees Scores\nMean: {mean:.2f}, Std Dev: {std_dev:.2f}')
    plt.xlabel('Scores')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    x, pdf, mean, std_dev = calculate_normal_distribution()
    plot_normal_distribution(x, pdf, mean, std_dev)
