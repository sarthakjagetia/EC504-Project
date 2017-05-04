#We will need a comment here depending on your server. It is basically telling the server where your python.exe is in order to interpret the language. The server is too lazy to do it itself.

import cgitb
import cgi

cgitb.enable() #This will show any errors on your webpage

inputs = cgi.FieldStorage() #REMEMBER: We do not have inputs, simply a button to run the program. In order to get inputs, give each one a name and call it by inputs['insert_name']

print("Content-type: text/html") #We are using HTML, so we need to tell the server

print("<title> firstpage</title>")
print("Whatever you would like to print goes here, preferably in between tags to make it look nice")
'''	
import numpy as np
 
def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
 
def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu])
 
def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)
'''