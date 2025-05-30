# Financial News Sentiment Analysis

This project analyzes financial news headlines to extract insights about publication trends, publisher activity, and key topics using natural language processing (NLP) and data visualization techniques.

## Project Structure

```
.
├── .gitignore
├── README.md
├── requirments.txt
├── data/
│   ├── raw_analyst_ratings.csv
│   ├── raw_analyst_ratings.csv.zip
│   ├── raw_analyst_ratings.parquet
│   ├── yfinance_data.zip
│   └── yfinance_data/
│       ├── AAPL_historical_data.csv
│       ├── AMZN_historical_data.csv
│       ├── GOOG_historical_data.csv
│       ├── META_historical_data.csv
│       ├── MSFT_historical_data.csv
│       ├── NVDA_historical_data.csv
│       └── TSLA_historical_data.csv
└── src/
    ├── notebooks/
    │   └── news_eda.ipynb
    ├── scripts/
    └── tests/
```

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/estif-lul/financial-sentiment-analysis
   cd financial-sentiment-analysis
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirments.txt
   ```

3. **Download NLTK Data:**
   The notebook will attempt to download required NLTK data (`punkt_tab`, `stopwords`) automatically. If you encounter issues, run:
   ```python
   import nltk
   nltk.download('punkt_tab')
   nltk.download('stopwords')
   ```

4. **Data Preparation:**
   - Ensure the `data/raw_analyst_ratings.parquet` file is present. If not, extract it from the provided CSV or ZIP files in the `data/` directory.

## Usage

### Exploratory Data Analysis

The main analysis is performed in [src/notebooks/news_eda.ipynb](src/notebooks/news_eda.ipynb). The notebook covers:

- **Loading and preprocessing data:** Reads the Parquet file and parses dates.
- **Headline statistics:** Calculates mean, median, standard deviation, skewness, and kurtosis of headline lengths.
- **Temporal analysis:** Examines yearly, monthly, and hourly trends in news publication.
- **Publisher analysis:** Identifies top publishers by article count.
- **Keyword and topic extraction:**
  - Most common words in headlines (after stopword removal).
  - Top bigram keywords using TF-IDF.
  - Topic modeling with Latent Dirichlet Allocation (LDA).
- **Visualization:** Plots daily publication trends and other relevant charts.

#### To run the notebook:

1. Open [src/notebooks/news_eda.ipynb](src/notebooks/news_eda.ipynb) in Jupyter or VS Code.
2. Execute cells sequentially to reproduce the analysis and visualizations.

### Example: Plotting Daily News Publication Trend

The following code (from the notebook) plots the number of articles published per day:

```python
# Count articles published per day
daily_news_count = news_df.groupby('date').size().reset_index(name='num_articles')

# Plot publication frequency over time
plt.figure(figsize=(12,6))
plt.plot(daily_news_count['date'], daily_news_count['num_articles'], label='Articles per Day')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.title('Daily Financial News Publication Trend')
plt.legend()
plt.show()
```

## Data Sources

- **raw_analyst_ratings.parquet:** Contains financial news headlines, URLs, publishers, dates, and associated stock tickers.
- **yfinance_data/**: Contains historical stock data for selected tickers.

## Dependencies

See [requirments.txt](requirments.txt) for the full list. Key libraries include:

- pandas
- numpy
- matplotlib
- scipy
- nltk
- scikit-learn
- tqdm
- seaborn

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.


## Acknowledgments

- [NLTK](https://www.nltk.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)
- [Benzinga](https://www.benzinga.com/) (for news data)