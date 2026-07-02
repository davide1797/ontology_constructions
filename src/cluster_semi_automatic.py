import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import umap.umap_ as umap
import matplotlib.pyplot as plt
#odfpy

# 1. Load dataset
file_path = os.getcwd() + "\src\data\papers_semi-automatic.ods"
df = pd.read_excel(file_path, engine="odf")

# 2. Combine text columns into a single string per row
df['Combined'] = "Manual: " + df['Manual'] + "; Automatic: " + df['Automatic']

# 3. Get semantic embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")  # small and fast model

embeddings = model.encode(df['Combined'].tolist(), show_progress_bar=True)

# 4. Find best k (3–5) using silhouette score
best_k, best_score, best_labels = None, -1, None
for k in range(3, 6):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(embeddings)
    score = silhouette_score(embeddings, labels)
    if score > best_score:
        best_k, best_score, best_labels = k, score, labels

df['Cluster'] = best_labels
print(f"Chosen number of clusters: {best_k} (silhouette score: {best_score:.3f})")

# 5. Dimensionality reduction for visualization
umap_model = umap.UMAP(random_state=42)
embeddings_2d = umap_model.fit_transform(embeddings)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    embeddings_2d[:, 0],
    embeddings_2d[:, 1],
    c=df['Cluster'],
    cmap="tab10",
    s=80,
    edgecolors="k",
    alpha=0.8,
)

# Add row labels as text
for i, label in enumerate(df.iloc[:, 0]):  # first column of df
    plt.text(
        embeddings_2d[i, 0],
        embeddings_2d[i, 1],
        str(label),
        fontsize=8,
        alpha=0.7,
        ha='center',
        va='center'
    )
    
plt.title(f"2D Semantic Clustering (k={best_k})", fontsize=14)
plt.xlabel("UMAP Dimension 1")
plt.ylabel("UMAP Dimension 2")
plt.grid(alpha=0.3)

# Add legend
handles, labels = scatter.legend_elements()
plt.legend(handles, [f"Cluster {i}" for i in range(best_k)], title="Clusters")
plt.tight_layout()
plt.show()
