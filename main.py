from algorithms.step_v2 import step_v2
from algorithms.centroid import kmeans
from judging.elbow import elbow
from judging.silhouette import silhouette
# from judging.silhouette_inc import silhouette

path = "./coordinates.csv"
folder = "./results/"
step_ending = "_cluster_step_records.txt"
kmeans_ending = "_cluster_centroids_records.txt"
# ending = "_bcn.csv"

def main():
    coords = import_coords(path)
    for clusters in range(2, 15):
        for _ in range(15):
            kmeans(str(clusters) + "_" + kmeans_ending, coords, clusters, plot = False)
    elbow(kmeans_ending)

def import_coords(file_name):
    coords = []
    with open(file_name) as file:
        for line in file:
            raw_coords = line.split(",")
            coords.append((float(raw_coords[0]), float(raw_coords[1])))
    return coords

main()
