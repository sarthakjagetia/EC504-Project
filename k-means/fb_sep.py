#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 10:46:58 2017

@author: yijliu
"""
from matplotlib import pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import cv2
import numpy as np

class Segment:
    def __init__(self,segments=5):
        #define number of segments, with default 5
        self.segments=segments

    def kmeans(self,image):
        image=cv2.GaussianBlur(image,(7,7),0)
        vectorized=image.reshape(-1,3)
        #print(vectorized.shape)
        vectorized=np.float32(vectorized) 
        criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        flags = cv2.KMEANS_RANDOM_CENTERS
        ret,label,center=cv2.kmeans(vectorized,self.segments,None,criteria,10, flags)
        #print(label.shape)
        #print(center.shape)
        res = center[label.flatten()]
        #print(res.shape)
        A = vectorized[label.ravel()==0]
        B = vectorized[label.ravel()==1]

        segmented_image = res.reshape((image.shape))
        return A, B, center, res, label.reshape((image.shape[0],image.shape[1])), segmented_image.astype(np.uint8) 


    def extractComponent(self,image,label_image,label):
        component=np.zeros(image.shape,np.uint8)
        component[label_image==label]=image[label_image==label]
        return component

if __name__=="__main__":
    import argparse
    import sys
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    ap.add_argument("-n", "--segments", required = False, type = int,
        help = "# of clusters")
    args = vars(ap.parse_args())

    image=cv2.imread(args["image"])
    if len(sys.argv)==3:
        
        seg = Segment()
        center, res, label, result = seg.kmeans(image)
    else:
        seg=Segment(args["segments"])
        A,B, center, res, label,result=seg.kmeans(image)
    ##cv2.imshow("segmented",result)
    #cv2.imwrite('plot.jpg', )
    fig = pylab.figure()
    ax = Axes3D(fig)  
    cv2.imwrite('messi_k2.jpg', result)    
    
    ax.scatter(A[:,0],A[:,1], A[:,2],c ='b')
    ax.scatter(B[:,0],B[:,1], B[:,2],c ='r')
    ax.scatter(center[:,0],center[:,1],center[:,2],s = 80,c = 'y', marker = '.')
    #pyplot.xlabel('Height'),plt.ylabel('Weight')
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('myfig.jpg')
    

        
    
    #result_2 = seg.extractComponent(image,label,2)
    #cv2.imshow("extracted",result)
    #cv2.imwrite('messi_2.png', result)
    #cv2.waitKey(0)