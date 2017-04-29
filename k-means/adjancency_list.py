from __future__ import division
import numpy as np
import cv2
import sys
from sklearn.cluster import KMeans
from scipy.spatial import distance

def adjancencylist(imageFile,k):
    img = cv2.imread(imageFile)
    newimg = img.reshape(-1,3)
    #newimg = np.reshape(img,(-1,3))
    kmeans = KMeans(init='k-means++', n_clusters=k, n_init=100)
    kmeans.fit_predict(newimg)
    error = kmeans.inertia_
    centroids = kmeans.cluster_centers_
    #print centroids
    labels = kmeans.labels_
    adjancencyList = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
			adjancency = []
			dist_sum = 0
			for k in range(0,len(centroids)):
				dist = distance.euclidean(img[i][j],centroids[k])
				dist_sum += dist
				adjancency.append(dist)
			for w in range(0,len(adjancency)):
				norm_dist = int(round(adjancency[w]/dist_sum*10))
				adjancency[w] = norm_dist
			adjancencyList.append(str(adjancency).translate(None, '[],'))
    return adjancencyList,len(adjancencyList)

def getData(imageFile,k):
	f = open('adjancency_list.txt', 'w')	
	#print imageFile
	#print k
	data,dataSize = adjancencylist(imageFile,k)
	for i in range(0,dataSize):
		f.write(str(data[i])+"\n")
	f.close()
	print "The size of data is:", dataSize


if __name__ == '__main__':
	#args = sys.argv
	#getData(args[1],int(args[2]))
        getData("rgb.thumbnail",2)
    	#img = cv2.imread("rgb.thumbnail")
	#print img
	
