import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/twitter_dataset.csv")

loc_counts = df["Location"].value_counts().head(10)
total_locs = df["Location"].count()
percentages = (loc_counts / total_locs * 100).round(2)

loc_df = pd.DataFrame({
    "location": loc_counts.index,
    "tweet": loc_counts.values,
    "percentage": percentages.values
})

print(loc_df)

plt.figure()
sns.barplot(x=loc_counts.values, y=loc_counts.index)
plt.title("Top 100 Locations")
plt.show()

lon_brands = df[df["Location"] == 'London, UK']["Brand"].value_counts().head(10)
lon_brands_df = pd.DataFrame({
    "brand": lon_brands.index,
    "tweets": lon_brands.values
})

print(lon_brands_df)