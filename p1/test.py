import os
from datasets import loadTextData
# Provide the absolute path to the sentiment.all file
sentiment_file_path = 'p1/data/sentiment.all'

# Check if the sentiment.all file exists
if not os.path.exists(sentiment_file_path):
    raise FileNotFoundError(f"File '{sentiment_file_path}' does not exist.")

# Load the text data using the absolute path
Xall, Yall, words, meta = loadTextData(sentiment_file_path)