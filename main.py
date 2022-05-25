from algorithms.step_v2 import step_v2

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"
file_path = "./result.txt"

def main():
    coords = import_coords(path)
    while True:
        step_v2(file_path, coords, 2, 96, 4, 1.33)

def import_coords(file_name):
    coords = []
    with open(file_name) as file:
        for line in file:
            raw_coords = line.split(",")
            coords.append((float(raw_coords[0]), float(raw_coords[1])))
    return coords

main()
