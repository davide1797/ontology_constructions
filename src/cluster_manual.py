import pandas as pd
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA 
import plotly.express as px
from collections import defaultdict
import os

def get_papers(file):
    df = pd.read_csv(file, header=None)
    df.columns = ['Name', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']

    names = df['Name'].values
    # For clustering
    types_raw = df['f1'].values
    numerical = df[['f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']].values.astype(float)
    combined = np.column_stack((types_raw, numerical))

    # For visualization
    df_encoded = pd.get_dummies(df[['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']], columns=['f1'])
    features_for_visualization = df_encoded.values  # shape: (46, 9)

    return names, combined, features_for_visualization

def custom_distance(x, y):
    diff = 0
    if x[0] != y[0]:
        diff += 1
    diff += np.sum(np.abs(x[1:].astype(float) - y[1:].astype(float)))

    return diff

if __name__ == "__main__":
    file = os.getcwd() + "\src\data\papers_manual.csv"
    names, df, features_visualization = get_papers(file)
   
    distance_matrix = squareform(pdist(df, metric=custom_distance))
    
    k_range = range(2, len(df) // 2 + 1)
    scores = []

    for k in k_range:
        model = AgglomerativeClustering(
            n_clusters=k,
            metric='precomputed',  # important for custom distances
            linkage='average'      # must be compatible with precomputed metric
        )
        labels = model.fit_predict(distance_matrix)

        # Silhouette score using the same precomputed distances
        score = silhouette_score(distance_matrix, labels, metric='precomputed')
        scores.append(score)
        print(f"k={k}, silhouette={score:.4f}")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(k_range, scores, 'bo-')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Silhouette Score")
    plt.title("Elbow Method using Silhouette Score (Agglomerative + Custom Distance)")
    plt.grid(True)
    plt.xticks(list(k_range))
    plt.show()

    # Optionally, pick the best k
    best_k = k_range[np.argmax(scores)]
    print(f"Optimal number of clusters: {best_k}")
    
    model = AgglomerativeClustering(
        n_clusters=best_k,
        metric='precomputed',  # important for custom distances
        linkage='average'      # must be compatible with precomputed metric
    )
    labels = model.fit_predict(distance_matrix)

    clusters = defaultdict(list)

    for idx, label in enumerate(labels):
        clusters[label].append(idx)

    for cluster in clusters:
        print(cluster, [names[i] for i in clusters[cluster]])

    pca = PCA(n_components=3)
    X_3d = pca.fit_transform(features_visualization)

    df_plot = pd.DataFrame(X_3d, columns=["PC1", "PC2", "PC3"])
    df_plot["Cluster"] = labels
    df_plot["Name"] = names

    fig = px.scatter_3d(
        df_plot, x="PC1", y="PC2", z="PC3", 
        color="Cluster", text="Name", hover_name="Name",
        title="3D PCA Projection with Clusters"
    )
    fig.update_traces(marker=dict(size=2), textposition="top center")
    fig.show()