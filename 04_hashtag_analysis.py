import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("/content/twitter_dataset.csv")

hashtags = df['Hashtags'].dropna().str.split(", ").sum()
counter = Counter(hashtags)
common = counter.most_common(10)
labels, count = zip(*common)

print("Hashtag\t\t\t\tCount")
for label, count in zip(labels, count):
    print(f"{label}: \t\t {count}")

plt.barh(labels, count)
plt.show()