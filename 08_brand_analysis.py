import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/twitter_dataset.csv")
brand_counts = df["Brand"].value_counts().head(100)
brand_engagement = df.groupby("Brand")[["Like_count", "Retweet_count"]].mean().loc[brand_counts.index]

plt.figure()
sns.barplot(x=brand_counts.values, y=brand_counts.index)
plt.show()

plt.figure()
sns.lineplot(x=brand_engagement.index, y=brand_engagement["Like_count"])
plt.show()

plt.figure()
sns.lineplot(x=brand_engagement.index, y = brand_engagement["Retweet_count"])
plt.show()