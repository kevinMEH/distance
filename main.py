from algorithms.step_v2 import step_v2
from algorithms.centroid import kmeans
from judging.elbow import elbow
from judging.silhouette import silhouette

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"
folder = "./results/"
kmeans_ending = "_cluster_centroids_records.txt"
step_ending = "_cluster_step_records.txt"

def main():
    coords = import_coords(path)
    silhouette(coords)
    return
    elbow()
    clusters = 11
    while True:
        for _ in range(7):
            kmeans(folder + str(clusters) + kmeans_ending, coords, clusters)
        clusters = clusters + 1

def import_coords(file_name):
    coords = []
    with open(file_name) as file:
        for line in file:
            raw_coords = line.split(",")
            coords.append((float(raw_coords[0]), float(raw_coords[1])))
    return coords

main()
