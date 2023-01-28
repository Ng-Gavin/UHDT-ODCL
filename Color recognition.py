import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans



# kmeans code 

kmeans=KMeans(n_clusters=5)
s=kmeans.fit(img)

labels=kmeans.labels_
print(labels)
labels=list(labels)

centroid=kmeans.cluster_centers_
print(centroid)

percent=[]
for i in range(len(centroid)):
  j=labels.count(i)
  j=j/(len(labels))
  percent.append(j)
print(percent)



kmeans=KMeans(n_clusters=4)
s=kmeans.fit(img)
labels=kmeans.labels_
centroid=kmeans.cluster_centers_
labels=list(labels)
percent=[]
for i in range(len(centroid)):
  j=labels.count(i)
  j=j/(len(labels))
  percent.append(j)
plt.pie(percent,colors=np.array(centroid/255),labels=np.arange(len(centroid)))
plt.show()