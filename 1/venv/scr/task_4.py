from scipy.cluster import *
names, data = get_data()
centroids = vq.kmeans(numpy.array(data), 5, iter=200)[0]