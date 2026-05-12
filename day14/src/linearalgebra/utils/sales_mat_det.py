#create matrix determinant for sales data
import numpy as np
from linearalgebra.configurations.conf import Config
import pandas as pd
def sales_matrix_determinant():
    df=pd.read_csv(Config.sales_path)
    #input data manufacturing cost, adv cost, influencer cost, discount cost, profit
    #convert discount percent to discount cost
    df['discount_cost']=df['sales_price']*df['discount_percent']/100
    x_data=df[['manufacturing_cost','advertisement_cost','influencer_cost','discount_cost']].values
    y_data=df['sales_price'].values
    #display x and y data
    print("X data:")
    print(x_data)
    print("Y data:")
    print(y_data)
    #compute the x correlation matrix
    x_correlation_matrix=np.corrcoef(x_data, rowvar=False)
    print("X correlation matrix:")
    print(x_correlation_matrix)
    # 2. Feature-to-sales correlation
    sales_corr = np.corrcoef(x_data, y_data, rowvar=False)[-1, :-1]
    print("\nFeature-to-sales correlation:")
    print(sales_corr) 

    print(x_correlation_matrix)
    #calculate the determinant of the x correlation matrix
    determinant=np.linalg.det(x_correlation_matrix)
    print("Determinant of the X correlation matrix:")
    print(determinant)

    if determinant<0.01:
        print("Warning: The determinant is very small, indicating potential multicollinearity among features.")
    else:
        print("The determinant is sufficiently large, suggesting that the features are not highly collinear.")

if __name__=="__main__":
    sales_matrix_determinant()
