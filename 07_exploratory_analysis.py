import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/twitter_dataset.csv")

print(df.head())

print(df.dtypes)

print(df.isnull().sum())

print(df.describe())

print(df.shape)