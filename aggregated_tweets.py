import pandas as pd

# Load the dataset
df = pd.read_csv('final_retweeted_english_tweets.csv')

# Group by 'user_key' and sum the retweet counts
user_retweet_counts = df.groupby('user_key')['retweet_count'].sum()

# Convert the Series to a DataFrame
df_aggregated = user_retweet_counts.reset_index()

# Rename columns for clarity
df_aggregated.columns = ['user_key', 'total_retweets']

# Save the aggregated data to a new CSV (optional)
df_aggregated.to_csv('aggregated_retweet_counts.csv', index=False)
