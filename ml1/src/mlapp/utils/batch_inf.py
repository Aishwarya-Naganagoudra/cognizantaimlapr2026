#batch inferences using reviews.csv and transformer model
import pandas as pd
from transformers import pipeline
from mlapp.configurations.conf import Config

def batch_inference(reviews_csv):
    # Load the reviews from the CSV file
    reviews_df = pd.read_csv(reviews_csv)
    
    # Initialize the sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis", 
                                  model="distilbert-base-uncased-finetuned-sst-2-english" )
    
    # Perform batch inference on the reviews
    results = sentiment_pipeline(reviews_df['review_text'].tolist())
    
    # Add the results to the DataFrame
    reviews_df['sentiment'] = [result['label'] for result in results]
    #confidence scores
    reviews_df["confidence_score"] = [round(r["score"], 4) for r in results]
    return reviews_df

if __name__ == "__main__":
    reviews_csv = Config.REVIEW_PATH  # Path to your reviews CSV file
    results_df = batch_inference(reviews_csv)
    print(results_df.head())