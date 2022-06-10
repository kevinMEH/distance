from genericpath import exists
from calculate import filter_dist_with_points
from distance import squared_dist_array, squared_dist_p
from plot import line_plot

folder = "./results/"

def silhouette(ending, coords, folder = folder):
    centroid_count = []
    silhouette_scores = []
    
    for z in range(2, 21):
        path = folder + str(z) + ending
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
                    for i in range(0, len(values), 2):
                        centroids_list.append((float(values[i]), float(values[i + 1])))
                    file_centroids.append(centroids_list)
                    
                if len(file_records) == 0:
                    continue;
                    
                centroid_count.append(z)

                # Finding true record centroids
                true_record = 999999
                record_centroids = centroids_list[0]
                for i, record in enumerate(file_records):
                    if record < true_record:
                        true_record = record
                        record_centroids = file_centroids[i]
                
                # Score calculation
                # Arrays (# centroids) of arrays (# points) of distances
                dist_arrays = []
                for centroid in record_centroids:
                    dist_arrays.append(squared_dist_array(centroid, coords))
                _, filtered_points = filter_dist_with_points(coords, dist_arrays)

                point_dist_arrays = []
                for point in coords:
                    point_dist_arrays.append(squared_dist_array(point, record_centroids))

                # For each point, find closest and second closest
                #   For each point in closest, find distance to every
                #   other point in second closest
                true_total_score = 0
                for i, point_centroid_dist in enumerate(point_dist_arrays):
                    # Finding closest and second closest clusters
                    closest = 99999999
                    closest_index = 0
                    next_closest = 99999999
                    next_closest_index = 0
                    
                    for j, dist in enumerate(point_centroid_dist):
                        if dist < closest:
                            next_closest = closest
                            next_closest_index = closest_index
                            closest = dist
                            closest_index = j
                        elif dist < next_closest:
                            next_closest = dist
                            next_closest_index = j

                    this_point = coords[i]
                    avg_dist_to_closest = 0
                    avg_dist_to_second = 0
                    for cluster_point in filtered_points[closest_index]:
                        dist_to_point = squared_dist_p(this_point, cluster_point)
                        if dist_to_point == 0: continue
                        avg_dist_to_closest += dist_to_point
                    for next_cluster_point in filtered_points[next_closest_index]:
                        dist_to_next = squared_dist_p(this_point, next_cluster_point)
                        avg_dist_to_second += dist_to_next
                    avg_dist_to_closest /= (len(filtered_points[closest_index]) - 1)
                    avg_dist_to_second /= (len(filtered_points[next_closest_index]))
                    
                    true_total_score += (avg_dist_to_second - avg_dist_to_closest) / max(avg_dist_to_second, avg_dist_to_closest)
                silhouette_scores.append(true_total_score / len(point_dist_arrays))
    
    line_plot(centroid_count, silhouette_scores)
