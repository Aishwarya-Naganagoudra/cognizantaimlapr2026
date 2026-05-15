#generate matrix with 5 customers and 5 products, with random ratings from 1 to 5
import numpy as np

def generate_random_ratings(num_customers=5, num_products=5, 
                            min_rating=1, max_rating=10):
    ratings = np.random.randint(min_rating, max_rating + 1, 
                                size=(num_customers, num_products))
    return ratings

def sentiment_analysis(ratings_matrix):
    # Simple sentiment analysis: average rating for each product
    #find number of rows and columns
    #complexity is O(n*m) where n is number of customers and m is number of products
    num_customers, num_products = ratings_matrix.shape
    for customer in range(num_customers):
        for product in range(num_products):
            rating = ratings_matrix[customer, product]
            if rating > 5:
                print(f"Customer {customer} has a positive sentiment towards Product {product} with a rating of {rating}.")
            elif rating == 5:
                print(f"Customer {customer} has a neutral sentiment towards Product {product} with a rating of {rating}.")
            else:
                print(f"Customer {customer} has a negative sentiment towards Product {product} with a rating of {rating}.")
if __name__ == "__main__":
    ratings_matrix = generate_random_ratings()
    print("Ratings Matrix:")
    print(ratings_matrix)