#clean the data replace the missing values with mean and median
import pandas as pd
from linearalgebra.configurations.conf import Config

def clean_data(file_path):
    #read the data
    data = pd.read_excel(file_path)
    #replace the zero values in insulin column with null values
    data['Insulin']=data['Insulin'].replace(0, pd.NA)
    #replace the missing values in insulin column with mean
    data['Insulin']=data['Insulin'].fillna(data['Insulin'].mean(), 
                                           inplace=True)
    return data['Insulin']


if __name__ == "__main__":
    file_path = Config.cleandata_path
    cleaned_data = clean_data(file_path)
    print(cleaned_data.head())