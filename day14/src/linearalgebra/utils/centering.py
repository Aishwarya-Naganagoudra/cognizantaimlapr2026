#create data centering for trainee score dataset
from scipy.stats import norm
import pandas as pd
from sklearn.preprocessing import StandardScaler
from linearalgebra.configurations.conf import Config
import matplotlib.pyplot as plt
import numpy as np
def center_data(file_path):
    #read the dataset
    df = pd.read_csv(file_path)
    #compute the center
    #calculate the mean of the score column
    mean_score = df['score'].mean()
    #x_centered = x - mean_score
    #center the data
    df['score_centered'] = df['score'] - mean_score
    return df

def calculate_normal_distribution(file_path):
    data = pd.read_csv(file_path)
    scores = data['score']
    mean = np.mean(scores)
    std_dev = np.std(scores)
    x = np.linspace(min(scores), max(scores), 1000)
    pdf = norm.pdf(x, mean, std_dev)
    return x, pdf, mean, std_dev

def create_plot(x, pdf,centered_df):
   #normalized distribution of the centered scores
    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf, color='blue', label='Normal Distribution')
    #plot histogram of scores
    scores = centered_df['score']
    mean = scores.mean()
    std_dev = scores.std()
    plt.bar(scores, norm.pdf(scores, mean, std_dev), color='orange', alpha=0.5, label='Trainees Scores')
    plt.title(f'Normal Distribution of Trainees Scores\nMean: {mean:.2f}, Std Dev: {std_dev:.2f}')
    plt.xlabel('Scores')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    file_path = Config.score_path
    centered_df = center_data(file_path)
    print(centered_df.head())
    x, pdf, mean, std_dev = calculate_normal_distribution(file_path)
    print(f'Mean: {mean}, Standard Deviation: {std_dev}')
    create_plot(x, pdf,centered_df)

