import pandas as pd
import networkx as nx
import re

# Load the original dataset
df_original = pd.read_csv('english_tweets.csv')

def extract_original_tweeter(text):
    """Extract original tweeter from a retweet text using regex"""
    match = re.search(r'RT @([A-Za-z0-9_]+):', text)
    if match:
        return match.group(1)
    return None

# Filter out rows that are retweets
df_retweets_original = df_original[df_original['text'].str.startswith('RT')]

# Extract original tweeter from retweets
df_retweets_original['original_tweeter'] = df_retweets_original['text'].apply(extract_original_tweeter)

# Filter out rows where no original tweeter was identified
df_retweets_filtered = df_retweets_original.dropna(subset=['original_tweeter'])

# Initialize a new directed graph
G_retweets_original = nx.DiGraph()

# Add nodes for all users
G_retweets_original.add_nodes_from(df_original['user_key'].unique())

# Create edges based on retweets
for index, row in df_retweets_filtered.iterrows():
    retweeter = row['user_key']
    original_tweeter = row['original_tweeter']
    
    # If the edge already exists, increase the weight by retweet count
    if G_retweets_original.has_edge(retweeter, original_tweeter):
        G_retweets_original[retweeter][original_tweeter]['weight'] += row['retweet_count']
    else:
        G_retweets_original.add_edge(retweeter, original_tweeter, weight=row['retweet_count'])

# Information about the constructed graph
num_nodes_retweets_original = G_retweets_original.number_of_nodes()
num_edges_retweets_original = G_retweets_original.number_of_edges()

print(f"Number of Nodes: {num_nodes_retweets_original}")
print(f"Number of Edges: {num_edges_retweets_original}")