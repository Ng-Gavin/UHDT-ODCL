
import cv2
from sklearn.cluster import KMeans
img = cv2.imread("test2.png") 
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = img.reshape((img.shape[1]*img.shape[0],3))

# import the modules
import os
from os import listdir
 
# get the path/directory
folder_dir = "C:/Users/RIJUSHREE/Desktop/Gfg images"
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".png")):
        print(images)


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



kmeans=KMeans(n_clusters=7)
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
