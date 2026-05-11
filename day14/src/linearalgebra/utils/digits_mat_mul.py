#create matrix multiplication using w*x+b for neural network digits csv file
import numpy as np
import pandas as pd
from linearalgebra.configurations.conf import Config

def mat_mul(w,x,b):
    return np.dot(w,x)+b

if __name__ == "__main__":
    file_path = Config.digits_path
    #load digits csv file
    df = pd.read_csv(file_path)
    #define x as the first 64 columns of the dataframe
    x = df.iloc[1:5, 1:65].values
    print("x shape: ", x.shape)
    #define w as a random matrix of shape (64,4)
    w = np.random.rand(64,4)
    print("w shape: ", w.shape)
    #print("x: ", x)
    #print("w: ", w)
    #define b as a random scalar
    b = np.random.rand(1)
    mat_mul_result = mat_mul(w,x,b)
    print("mat_mul_result shape: ", mat_mul_result)
 

