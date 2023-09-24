import pandas as pd

# Load the updated CSV file into a DataFrame
df_updated = pd.read_csv('updated_tweets.csv')

# Specify the user you want to search for
user_to_search = "ten_gop"

# Filter the DataFrame for the specific user and create a copy
filtered_tweets = df_updated[df_updated['user_key'] == user_to_search].copy()

# Convert the retweet_count column to numeric values
filtered_tweets['retweet_count'] = pd.to_numeric(filtered_tweets['retweet_count'], errors='coerce')

# Calculate the number of tweets and the total retweets for the user
num_filtered_tweets = filtered_tweets.shape[0]
total_filtered_retweets = filtered_tweets['retweet_count'].sum()

print(f"Number of tweets by {user_to_search}: {num_filtered_tweets}")
print(f"Total retweets for those tweets: {total_filtered_retweets}")
