import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('D:\\GCOEN SEM 6\\PS-2 LAB\\ps-2 vs folder\\mtcars.csv') # Double backslashes for file path in Windows

X = df[['mpg', 'hp']]

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

df['Cluster'] = kmeans.labels_

plt.figure(figsize=(8, 6))

plt.scatter(X['mpg'], X['hp'], c=df['Cluster'], cmap='viridis') # Corrected scatter plot arguments

plt.xlabel('mpg')
plt.ylabel('hp')
plt.title('Clustering of mtcars dataset based on mpg and hp by K-means')
plt.colorbar(label='Cluster')

plt.show()


# Clustering algorithms are unsupervised learning techniques used to group similar data points into clusters based on their 
# inherent patterns or similarities. These algorithms partition the data into subsets, or clusters, where data points 
# within the same cluster are more similar to each other than to those in other clusters. Key concepts include distance 
# metrics to quantify similarity between data points, cluster centroids representing the center of each cluster, and 
# optimization criteria to iteratively refine cluster assignments. Common clustering algorithms include K-means, 
# hierarchical clustering, DBSCAN, and Gaussian mixture models, each with its strengths and weaknesses suitable for 
# different data types and structures. Clustering is widely used in various domains such as customer segmentation, 
# image segmentation, anomaly detection, and pattern recognition, providing valuable insights into underlying data 
# structures and facilitating data-driven decision-making.
