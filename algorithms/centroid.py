from calculate import *
from time import sleep

from plot import scatter_plot

def kmeans(file_path, coords, clusters, plot = False):
    centroids = []
    for _ in range(clusters):
        point = random_point(coords)
        while point in centroids:
            point = random_point(coords)
        centroids.append(point)
    
    record, filtered_dists, filtered_points = calc_scores_with_filtered(coords, centroids)
    points_shifted = 9999
    
    print("Initial: " + str(record) + " " + str(centroids))

    while points_shifted != 0:
        # Finding centroids of clusters. Assigning new points
        for i in range(len(centroids)):
            x, y = average_xy(filtered_points[i])
            centroids[i] = (x, y)
        
        # Calculating
        prev_filtered_arrays = filtered_dists
        record, filtered_dists, filtered_points = calc_scores_with_filtered(coords, centroids)
        # Calculating how many points shifted clusters
        points_shifted = abs_diffs_lengths(prev_filtered_arrays, filtered_dists)
    
        print(record, centroids, points_shifted)
    
    if plot:
        scatter_plot(filtered_points, centroids, record)

    file = open(file_path, "a")
    file.write(str(record) + " " + str(centroids) + "\n")
    print(record, centroids)
    print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️")

    file.close()
    sleep(0.25)


def average_xy(filtered):
    if len(filtered) == 0: return (0, 0)
    sum_x = 0
    sum_y = 0
    for x, y in filtered:
        sum_x += x
        sum_y += y
    return (sum_x / len(filtered), sum_y / len(filtered))

def abs_diffs_lengths(arrays1, arrays2):
    result = 0
    for i in range(len(arrays1)):
        result += abs(len(arrays1[i]) - len(arrays2[i]))
    return result