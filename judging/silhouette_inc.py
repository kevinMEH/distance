# NOTE: This algorithm is incorrect.

from genericpath import exists
from calculate import filter_dist_any
from distance import squared_dist_array, squared_dist_p
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
                
                dist_arrays = []
                for centroid in record_centroids:
                    dist_arrays.append(squared_dist_array(centroid, coords))
                filtered_dists = filter_dist_any(dist_arrays)
                
                # Calculating A and B
                closest_dists = []
                next_closest_dists = []
                for point_index, point in enumerate(coords):
                    first_record = 9999999
                    first_record_centroid_index = 0
                    second_record = 9999999

                    for z, dist_array in enumerate(dist_arrays):
                        squared_dist = dist_array[point_index]
                        if squared_dist < first_record:
                            second_record = first_record
                            first_record = squared_dist
                            first_record_centroid_index = z
                        elif squared_dist < second_record:
                            second_record = squared_dist

                    first_record_centroid = record_centroids[first_record_centroid_index]
                    # Hack to calculate mean of all other points in cluster:
                    # Centroid is already mean, multiply by num of points,
                    # subtract self, divide by num of points - 1.
                    
                    num_points_assoc_centroid = len(filtered_dists[first_record_centroid_index])
                    cent_x, cent_y = first_record_centroid
                    cent_x = cent_x * num_points_assoc_centroid
                    cent_y = cent_y * num_points_assoc_centroid
                    cent_x = cent_x - point[0]
                    cent_y = cent_y - point[1]
                    cent_x = cent_x / (num_points_assoc_centroid - 1)
                    cent_y = cent_y / (num_points_assoc_centroid - 1)
                    closest_dists.append(squared_dist_p(point, (cent_x, cent_y)))
                    next_closest_dists.append(second_record)

                total_point_score = 0
                for j in range(len(closest_dists)):
                    first_record = closest_dists[j]
                    second_record = next_closest_dists[j]
                    total_point_score += (second_record - first_record) / max(second_record, first_record)
                silhouette_scores.append(total_point_score / len(closest_dists))
    
    line_plot(centroid_count, silhouette_scores)
