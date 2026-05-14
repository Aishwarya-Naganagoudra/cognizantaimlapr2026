#apply robust scalar to the ceo salary data

import pandas as pd
from sklearn.preprocessing import RobustScaler
from linearalgebra.configurations.conf import Config

def robust_scalar_ceo_salary(file_path):
    #read the ceo salary data
    df = pd.read_csv(file_path)
    
    #select the salary column
    salary = df['salary_usd'].values.reshape(-1, 1)
    
    #apply robust scalar to the salary column
    scaler = RobustScaler()
    salary_scaled = scaler.fit_transform(salary)
    
    #add the scaled salary back to the dataframe
    df['Salary_Scaled'] = salary_scaled
    
    return df

if __name__ == "__main__":
    file_path = Config.ceo_salary_path
    df_scaled = robust_scalar_ceo_salary(file_path)
    print(df_scaled.head())