import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/twitter_dataset.csv")
df["Sentiment"] = df["Sentiment"].str.lower()
df["Engagement"] = df["Like_count"] + df["Retweet_count"]
df["Text_length"] = df["Tweet"].str.len()
engagement_by_length = df.groupby(pd.cut(df["Text_length"], bins=5), observed=False)["Engagement"].mean()

plt.figure()
sns.barplot(x=engagement_by_length.index, y=engagement_by_length.values)
plt.show()

top_users = df.groupby("Username")["Engagement"].sum().nlargest(10).reset_index()
plt.figure()
sns.barplot(x="Engagement", y="Username", data=top_users)
plt.show()

top_tweets = df.nlargest(10, "Engagement")[["Username", "Tweet", "Engagement"]]
print(top_tweets.head())