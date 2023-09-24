import pandas as pd
import langid

# Load the updated CSV file into a DataFrame
df_updated = pd.read_csv('updated_tweets.csv')

# Set langid to just use English and a few other common languages for speed
langid.set_languages(['en', 'es', 'fr', 'de', 'it', 'pt'])

def is_english(text):
    # Ensure the text is a string
    if not isinstance(text, str):
        return False
    lang, _ = langid.classify(text)
    return lang == 'en'


# Filter the DataFrame for English tweets
df_english = df_updated[df_updated['text'].apply(is_english)]

# Save the filtered DataFrame
df_english.to_csv('english_tweets.csv', index=False)


# Print the number of rows in the original and filtered DataFrames
print(f"Original number of tweets: {df_updated.shape[0]}")
print(f"Number of English tweets: {df_english.shape[0]}")

# Randomly sample 5 tweets from the filtered DataFrame
sample_tweets = df_english['text'].sample(5)
print("\nSampled English tweets:")
print(sample_tweets)
