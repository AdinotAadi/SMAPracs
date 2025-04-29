import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv("/content/twitter_dataset.csv")
tweets = df["Tweet"].dropna()

vectorizer = CountVectorizer(stop_words="english", max_features=20)
X = vectorizer.fit_transform(tweets)

keywords = vectorizer.get_feature_names_out()
print(f"Keywords: {keywords}")

lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X)

for i, topic in enumerate(lda.components_):
    print(f"Topic {i+1}: {[keywords[i] for i in topic.argsort()[:-6:-1]]}")