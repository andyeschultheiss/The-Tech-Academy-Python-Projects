import matplotlib.pyplot as plt 
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    random_state=42
)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print(scaled_features[:5])
print(true_labels[:5])
