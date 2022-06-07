from genericpath import exists
from distance import squared_dist_array
from plot import line_plot

folder = "./results/"

def silhouette(ending, coords, folder = folder):
    centroid_count = []
    silhouette_scores = []
    
    for i in range(2, 21):
        path = folder + str(i) + ending
        if exists(path):
            with open(path) as file:
                file_records = []
                file_centroids = []
                for line in file:
                    values = line.split(" ")
                    file_records.append(float(values[0]))
                    values = "".join(values[1 : ])
                    values = values.strip()
                    values = values[1 : len(values) - 1]
                    values = values.split("(")
                    values = "".join(values)
                    values = values.split(")")
                    values = "".join(values)
                    values = values.split(",")
                    centroids_list = []
                    for j in range(0, len(values), 2):
                        centroids_list.append((float(values[j]), float(values[j + 1])))
                    file_centroids.append(centroids_list)
                    
                if len(file_records) == 0:
                    continue;
                    
                centroid_count.append(i)

                # Finding true record centroids
                true_record = 999999
                record_centroids = centroids_list[0]
                for j, record in enumerate(file_records):
                    if record < true_record:
                        true_record = record
                        record_centroids = file_centroids[j]
                
                # Calculating A and B
                # Arrays (# centroids) of arrays (# points) of distances
                dist_arrays = []
                for centroid in record_centroids:
                    dist_arrays.append(squared_dist_array(centroid, coords))
                # Best distances - We want second best
                closest_dists = []
                next_closest_dists = []
                # For each point
                for j in range(len(dist_arrays[0])):
                    first_record = 9999999
                    second_record = 9999999
                    # For each centroid dist array
                    for distance_array in dist_arrays:
                        dist = distance_array[j]
                        if dist < first_record:
                            first_record = dist
                    closest_dists.append(first_record)
                    for distance_array in dist_arrays:
                        dist = distance_array[j]
                        if dist < second_record and dist != first_record:
                            second_record = dist
                    next_closest_dists.append(second_record)
                
                total_point_score = 0
                for j in range(len(closest_dists)):
                    first_record = closest_dists[j]
                    second_record = next_closest_dists[j]
                    total_point_score += (second_record - first_record) / second_record
                silhouette_scores.append(total_point_score / len(closest_dists))
    
    line_plot(centroid_count, silhouette_scores)
