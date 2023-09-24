import pandas as pd

# Load the English tweets from the CSV file
df_english = pd.read_csv('english_tweets.csv')

# Filter the DataFrame to keep only tweets with retweet_count > 0
retweeted_tweets = df_english[df_english['retweet_count'] > 0]

# Save the filtered DataFrame
retweeted_tweets.to_csv('retweeted_english_tweets.csv', index=False)

# Verification output
print(f"Number of English tweets: {df_english.shape[0]}")
print(f"Number of Retweeted English tweets: {retweeted_tweets.shape[0]}")