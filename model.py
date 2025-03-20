from sklearn.cluster import KMeans 
import pandas as pd
import subprocess
df = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")
dfKmeans = df.drop(['PassengerId', 'Survived', 'Age_category_'], axis=1)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
dfKmeans['Cluster'] = kmeans.fit_predict(dfKmeans)

cluster_counts = dfKmeans['Cluster'].value_counts().sort_index()

with open("k.txt", "w") as f:
    for cluster, count in cluster_counts.items():
        f.write(f"Cluster {cluster}: {count} records\n")