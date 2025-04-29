import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv("/content/twitter_dataset.csv")
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Month"] = df["Timestamp"].dt.to_period("M")

vectorizer = CountVectorizer(stop_words="english", max_features=20)
X = vectorizer.fit_transform(df["Tweet"])
keywords = vectorizer.get_feature_names_out()

lda = LatentDirichletAllocation(n_components=5, random_state=42)
topic_dist = lda.fit(X)
df["Topic"] = topic_dist.transform(X).argmax(axis=1)

topic_labels = [
    " / ".join([keywords[i] for i in topic.argsort()[:-6:-1]])
    for topic in lda.components_
]

trend = df.groupby(["Month", "Topic"]).size().unstack(fill_value=0)
trend.columns = topic_labels

plt.figure(figsize=(10, 6))
trend.plot()
plt.show()