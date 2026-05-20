#create skpipe file for pizza data using linearregression
import pandas as pd
from sklearn.pipeline import Pipeline
from kafkamessageapp.configurations.conf import KafkaConfig
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
def create_pipeline(pizza_data):
    print("pipeie ready")
    # Define the features and target variable
    X = pizza_data.drop("pizza_rate", axis=1)
    Y = pizza_data["pizza_rate"]
    # Create a pipeline with imputation and linear regression
    #defining imputer is manual step replace it by pipeline
    #simple_inmputer = SimpleImputer(strategy="mean")
    # trainig and testing data
    xtrain, xtest, ytrain, ytest = train_test_split(X, Y,
                         test_size=0.3, 
                         random_state=42                         
                         )
    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler()),
        ("regressor", LinearRegression())
    ])
    pipeline.fit(xtrain, ytrain)
    print("Pipeline created and trained successfully")
    #create the predictions

    predictions = pipeline.predict(xtest)
    print("Y predictions:", xtest["pizza_size"].values[:5], predictions[:5])
    
    #evaluate the model    
    mse = mean_squared_error(ytest, predictions)  
   
    print(f"Mean Squared Error: {mse}")

    #plot the results
    plt.scatter(xtest["pizza_size"], ytest, color="blue", label="Actual")
    plt.scatter(xtest["pizza_size"], predictions, color="red", label="Predicted")
    #plot the line of best fit
    plt.plot(xtest["pizza_size"], predictions, color="green", label="Line of Best Fit")
    plt.xlabel("Pizza Size")
    plt.ylabel("Pizza Rate")
    plt.title("Actual vs Predicted Pizza Rate")
    plt.legend()
    plt.show()
    
    


    

if __name__ == "__main__":
    pizza_data = pd.read_csv(KafkaConfig.pizza_path)
    create_pipeline(pizza_data)
    
