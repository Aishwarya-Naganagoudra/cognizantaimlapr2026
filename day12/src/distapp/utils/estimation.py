#create estimation.py for sales_data using sales_amount column
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
from distapp.configurations.config import Config
#point estimation for sales_amount and purchase_amount columns
def estimation():
    config = Config()
    data = pd.read_csv(config.estimation_path)
    sales_amount = data['sales_amount']
    
    # Calculate mean and standard deviation
    mean_sales = sales_amount.mean()
    std_dev_sales = sales_amount.std()
    
    # calculate mean and standard deviation for purchase_amount
    purchase_amount = data['purchase_amount']
    mean_purchase = purchase_amount.mean()
    std_dev_purchase = purchase_amount.std()

    return mean_sales, std_dev_sales, mean_purchase, std_dev_purchase

def plot_estimation(sales_date, sales_amount, mean_sales, std_dev_sales):
    
    # Plot histogram for sales_amount
    plt.figure(figsize=(10, 6))
    #plot x axis sales_date and y axis sales_amount
    #plot normal distribution curve
    x = sales_date
    y = sales_amount
    plt.plot(x, y, label='Normal Distribution', color='red')
    #plot the mean and standard deviation
    plt.axhline(mean_sales, color='blue', linestyle='--', label='Mean')
    plt.axhline(mean_sales + std_dev_sales, color='green', linestyle='--', label='Mean + 1 Std Dev')
    plt.axhline(mean_sales - std_dev_sales, color='orange', linestyle='--', label='Mean - 1 Std Dev')
    plt.title('Distribution of Sales Amount')
    plt.xlabel('sales_date')
    plt.ylabel('sales_amount')
    plt.grid(axis='y', alpha=0.75)
    plt.legend()
    plt.show()

def interval_estimation():
    config = Config()
    data = pd.read_csv(config.estimation_path)
    sales_amount = data['sales_amount']    
    # Calculate mean and standard deviation
    mean_sales = sales_amount.mean()
    min_sales = sales_amount.min()
    max_sales = sales_amount.max()        
    return mean_sales, min_sales, max_sales

if __name__ == "__main__":
    mean_sales, std_dev_sales, mean_purchase, std_dev_purchase = estimation()
    print(f"Sales Amount - Mean: {mean_sales}, Standard Deviation: {std_dev_sales}")
    print(f"Purchase Amount - Mean: {mean_purchase}, Standard Deviation: {std_dev_purchase}")
    df = pd.read_csv(Config().estimation_path)
    x=pd.to_datetime(df['date_of_sales'])
    y=df['sales_amount']
    plot_estimation(x,y, mean_sales, std_dev_sales)

    #interval estimation
    mean_sales, min_sales, max_sales = interval_estimation()

    print(f"Sales Amount - Mean: {mean_sales}, Min: {min_sales}, Max: {max_sales}")