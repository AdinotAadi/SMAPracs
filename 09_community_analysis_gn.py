import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import girvan_newman

df = pd.read_csv("/content/twitter_dataset.csv").head(20)

G = nx.Graph()

for brand in df["Brand"].dropna().unique():
    users = df[df["Brand"] == brand]["Username"].dropna().unique()
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            G.add_edge(users[i], users[j], brand=brand)

communities = next(girvan_newman(G))
i = 1
for community in communities:
    print(f"Community [{i}]: {community}")
    i = i + 1

plt.figure()
nx.draw(G, with_labels=True, node_size=50, font_size=8)
plt.show()