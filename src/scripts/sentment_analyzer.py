import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity  # Returns value from -1 (negative) to 1 (positive)

    
if __name__ == "__main__":
    try:
        # Load the news parquet file
        news_df = pd.read_parquet('data/raw_analyst_ratings.parquet')
    except FileNotFoundError:
        print("File not found. Please ensure the path is correct and the file exists.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the parquet file: {e}")
        exit(1)


    # Apply sentiment analysis
    news_df['sentiment'] = news_df['headline'].apply(get_sentiment)

    news_df.sort_values(by='date', inplace=True)
    # Save the processed DataFrame to a new CSV file
    news_df[['headline', 'url', 'publisher', 'date', 'stock', 'sentiment']].to_csv(
        'data/processed_analyst_ratings.csv', index=False)

    print(news_df[['headline', 'sentiment']].head())