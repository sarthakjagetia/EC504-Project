# EC504-Project

PROJECT NAME: Image Foreground/Background Segmentation using Network Flow

TEAM NAME: DaVincii
 
TEAM MEMBERS: 
Aastha Anand (aastha24@bu.edu) 

Archana Bajaj (bajaj@bu.edu) 

Rashmi Agrawal (rashmi23@bu.edu) 

Sarthak Jagetia (sarthakj@bu.edu) 

Yijian Liu (yijliu@bu.edu) 

BRIEF DESCRIPTION:
In computer vision, image segmentation is the process of partitioning a digital image into multiple segments (sets of pixels, also known as super-pixels). The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images.

Segmentation is generally treated as a clustering problem, where the pixels are clustered into two groups (foreground or background). We will be using network flow as a method to solve the segmentation problem efficiently in the case of two segments. We will set up the flow network for the segmentation problem and then find the minimum capacity cut for this graph after which we will have an optimal algorithm in our model of foreground/background segmentation.

For the implementation of our algorithm, we will label each pixel in an image belonging to either the foreground of the scene or the background. This can be done with the help of any clustering algorithm based on the color (e.g., RGB values) of the pixels. We plan to use k-means clustering algorithm for our project.

Covering the optional requirements for the project, we plan to do add the following two parts:
Extend the image segmentation beyond two segments to k segments.
Develop an interactive GUI through which the user can select a part of the image he/she wishes to segment

APPLICATIONS OF THE PROJECT:
Some practical examples of image segmentation include:-
Recognition tasks: face recognition, fingerprint recognition, iris recognition
Medical Imaging: surgery planning, measure tissue volumes, locate tumors
Content-based image retrieval
Object detection: Locate objects in satellite images (roads,forests,crops)

REFERENCES:
Siddheswar Ray and Rose H. Turi: Determination of number of Clusters in K-means Clustering and Application in Color Image Segmentation.
Foreground Detection: https://en.wikipedia.org/wiki/Foreground_detection
Dorit S. Hochbaum: An Efficient Algorithm for Image Segmentation, Markov Random Fields and Related Problems.
Caroline Pantofaru and Martial Hebert: A Comparison of Image Segmentation Algorithms  
Ying Yin: Binary Image Segmentation Using Graph Cuts  
Yuri Boykov: Graph Cuts and Efficient N-D Image Segmentation  


SCHEDULE:
          
Task
Deadline
Implement the binary segmentation 
04/10/17
Make improvements(interactive application)
04/30/17
Prepare report and presentation
05/05/17
