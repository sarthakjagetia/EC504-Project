def kmeans_Likelihood(in_image, k):
    image = cv2.imread(in_image)
    kmeans = KMeans(init='k-means++', n_clusters=2)
    kmeans.predict(image)
    centroids = kmeans.cluster_
    labels = kmeans.labels_
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(0, centroids):
                dist = distance.euclidean(image[i][j], centroids[k])
                dist_sum += dist
                likelihood.append(dist)
            for w in range(0, len(likelihood)):
                norm_dist = int(round(likelihood[w] / dist_sum * 10))
                likelihood[w] = norm_dist
            likelihood_List.append(str(likelihood).translate(None, '[],'))
    return likelihood_List
