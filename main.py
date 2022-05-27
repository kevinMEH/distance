from algorithms.step_v2 import step_v2
from algorithms.centroid import kmeans

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"
file_path = "./results/2_cluster_centroids_records.txt"

def main():
    coords = import_coords(path)
    while True:
        kmeans(file_path, coords, 2)
        # step_v2(file_path, coords, 3, 64, 3, 1.33)

def import_coords(file_name):
    coords = []
    with open(file_name) as file:
        for line in file:
            raw_coords = line.split(",")
            coords.append((float(raw_coords[0]), float(raw_coords[1])))
    return coords

main()
