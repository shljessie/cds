from sklearn import preprocessing
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

data = pd.read_csv("final_sub_pol.csv")
plt.scatter(data['subjectivity'], data['polarity'])
plt.xlabel('Subjectivity')
plt.ylabel('Polarity')
# plt.show()

x = data.copy()
kmeans = KMeans(2)
kmeans.fit(x)

clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)

plt.scatter(clusters['subjectivity'], clusters['polarity'],
            c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('Subjectivity')
plt.ylabel('Polarity')
# plt.show()

x_scaled = preprocessing.scale(x)

# wcss = []
# for i in range(1, 30):
#     kmeans = KMeans(i)
#     kmeans.fit(x_scaled)
#     wcss.append(kmeans.inertia_)

# plt.plot(range(1, 30), wcss)
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()

kmeans_new = KMeans(4)
kmeans_new.fit(x_scaled)
cluster_new = x.copy()
cluster_new['cluster_pred'] = kmeans_new.fit_predict(x_scaled)

plt.scatter(cluster_new['subjectivity'], cluster_new['polarity'],
            c=cluster_new['cluster_pred'], cmap='rainbow')
plt.xlabel('Subjectivity')
plt.ylabel('Polarity')
plt.show()
