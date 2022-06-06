from algorithms.step_v2 import step_v2
from algorithms.centroid import kmeans

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"
folder = "./results/"
kmeans_ending = "_cluster_centroids_records.txt"
step_ending = "_cluster_step_records.txt"

def main():
    clusters = 7
    while True:
        coords = import_coords(path)
        for _ in range(7):
            kmeans(folder + str(clusters) + kmeans_ending, coords, clusters)
        clusters = clusters + 2

def import_coords(file_name):
    coords = []
    with open(file_name) as file:
        for line in file:
            raw_coords = line.split(",")
            coords.append((float(raw_coords[0]), float(raw_coords[1])))
    return coords

main()
