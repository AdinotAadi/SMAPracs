import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/twitter_dataset.csv")
df = df.dropna(subset=["Tweet", "Sentiment"])
df["Sentiment"] = df['Sentiment'].str.lower()

print(df.head())

plt.figure()
sns.countplot(data=df, x='Sentiment')

print(f"Positive Tweets:\n {df[df['Sentiment'] == 'positive']['Tweet'].head()}")
print(f"Neutral Tweets:\n {df[df['Sentiment'] == 'neutral']['Tweet'].head()}")
print(f"Negative Tweets:\n {df[df['Sentiment'] == 'negative']['Tweet'].head()}")

sentiments = ['positive', 'neutral', 'negative']

for sentiment in sentiments:
    text = " ".join(df[df["Sentiment"] == sentiment]["Tweet"])
    wc = WordCloud(background_color="white", stopwords="English").generate(text)
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.title(f"Wordcloud for {sentiment } sentiment:")
    plt.show()