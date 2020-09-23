import numpy as np
import tensorflow as tf
from create_embedding import list_of_poems
from poetry_analysis import poems

num_points = 100
dimensions = 2


def create_poem_dict():  # associates each poem to its index in the list of poems
    poem_dict = {}
    for poem in list_of_poems:
        poem_dict[list_of_poems.index(poem)] = poem
    return poem_dict


poem_dictionary = create_poem_dict()

points = np.array(list_of_poems)  # need array for processing rather than a list


def input_fn():  # maps our poems to a tensor for the algorithm
    return tf.compat.v1.train.limit_epochs(
        tf.convert_to_tensor(points, dtype=tf.float32), num_epochs=1)


num_clusters = 5
kmeans = tf.compat.v1.estimator.experimental.KMeans(
    num_clusters=num_clusters, use_mini_batch=False)  # initializes the k means clustering

# train
num_iterations = 10

for _ in range(num_iterations):
    kmeans.train(input_fn)
    cluster_centers = kmeans.cluster_centers()
    previous_centers = cluster_centers

# map the input points to their clusters
cluster_indices = list(kmeans.predict_cluster_index(input_fn))

cluster_0 = []
cluster_1 = []
cluster_2 = []
cluster_3 = []
cluster_4 = []
for i, point in enumerate(points):  # loop prints out every poem in each cluster
    if cluster_indices[i] == 0:
        cluster_0.append(" ".join(poems[i]))
    elif cluster_indices[i] == 1:
        cluster_1.append(" ".join(poems[i]))
    elif cluster_indices[i] == 2:
        cluster_2.append(" ".join(poems[i]))
    elif cluster_indices[i] == 3:
        cluster_3.append(" ".join(poems[i]))
    elif cluster_indices[i] == 4:
        cluster_4.append(" ".join(poems[i]))


print("Cluster 0: ", cluster_0)
print("Cluster 1: ", cluster_1)
print("Cluster 2: ", cluster_2)
print("Cluster 3: ", cluster_3)
print("Cluster 4: ", cluster_4)

with open("cluster0.txt", "w") as f:  # writes each cluster to a text file
    for lst in cluster_0:
        f.write(f"{lst}\n\n")

with open("cluster1.txt", "w") as f:
    for lst in cluster_1:
        f.write(f"{lst}\n\n")

with open("cluster2.txt", "w") as f:
    for lst in cluster_2:
        f.write(f"{lst}\n\n")

with open("cluster3.txt", "w") as f:
    for lst in cluster_3:
        f.write(f"{lst}\n\n")

with open("cluster4.txt", "w") as f:
    for lst in cluster_4:
        f.write(f"{lst}\n\n")
