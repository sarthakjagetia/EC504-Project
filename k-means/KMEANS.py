# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:45:32 2017

@author: sarjag
"""

from __future__ import division
import numpy as np
import cv2
from sklearn.cluster import KMeans
from scipy.spatial import distance

def getLikelihood(imageFile):
    img = cv2.imread(imageFile)
    newimg = img.reshape(-1,3)
    kmeans = KMeans(init='k-means++', n_clusters=2, n_init=100)
    kmeans.fit_predict(newimg)
    error = kmeans.inertia_
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    likelihoodList = []
    segmentedimage = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            a = distance.euclidean(img[i][j],centroids[0])
            b = distance.euclidean(img[i][j],centroids[1])
            likelihood = a/(a+b)
        if (likelihood > 0.5):
            segmentedimage[i][j]=1;
            likelihoodList.append(int(round(likelihood*10)))
    return likelihoodList,len(likelihoodList)

def getData(imageFile):
	f = open('data.txt', 'w')	
	dataList,dataSize = getLikelihood(imageFile)
	for data in range(0,dataSize):
		f.write(str(dataList[data])+"\n")
	f.close()
	print (dataSize)
 
getData("lena.jpg")
