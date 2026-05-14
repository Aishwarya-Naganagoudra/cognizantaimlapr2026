#create min max normalization function for angola population data
import pandas as pd
from linearalgebra.configurations.conf import Config
def min_max_normalization(file_path):
    df = pd.read_excel(file_path)
    #select year column and apply min max normalization
    year = df.iloc[:, 0]  # Assuming the year column is the first column
    min_year = year.min()
    max_year = year.max()
    normalized_year = (year - min_year) / (max_year - min_year)
    df['Year'] = normalized_year
    #select population column and apply min max normalization
    population = df.iloc[:, 1]  # Assuming the population column is the second column
    min_population = population.min()
    max_population = population.max()   
    normalized_population = (population - min_population) / (max_population - min_population)
    df['Population'] = normalized_population
    df.drop(df.columns[0:2], axis=1, inplace=True)  # Drop any additional columns
    normalized_file_path = file_path.replace('.xlsx', '_normalized.xlsx')
    df.to_excel(normalized_file_path, index=False)
    print(f"Normalized data saved to {normalized_file_path}")


if __name__ == "__main__":
    file_path = Config.population_path
    min_max_normalization(file_path)