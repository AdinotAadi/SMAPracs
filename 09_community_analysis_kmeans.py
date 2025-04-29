import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.cluster import KMeans

df = pd.read_csv("/content/twitter_dataset.csv").head(20)
G = nx.Graph()

for brand in df["Brand"].dropna().unique():
    users = df[df["Brand"] == brand]["Username"].dropna().unique()
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            G.add_edge(users[i], users[j], brand=brand)

adj_mat = nx.to_pandas_adjacency(G)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(adj_mat)

labels = kmeans.labels_
for user, label in zip(adj_mat.index, labels):
    print(f"User: {user}, Cluster: {label}")

plt.figure()
nx.draw(G, with_labels=True, node_size=50, font_size=8, node_color=clusters)