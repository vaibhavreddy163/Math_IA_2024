import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('tweets.csv')

# List of columns to drop
columns_to_drop = [
    'user_id', 'created_at', 'created_str', 'retweeted', 'tweet_id', 
    'source', 'expanded_urls', 'posted', 'mentions', 
    'retweeted_status_id', 'in_reply_to_status_id'
]

# Drop the columns
df = df.drop(columns=columns_to_drop)

# Save the modified data to a new CSV file
df.to_csv('updated_tweets.csv', index=False)

print("Data manipulation complete!")
