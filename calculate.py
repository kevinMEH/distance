import random
from math import sqrt
from distance import squared_dist, dist

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"

def test():
	coords = import_coords(path)
	coords = coords[0:14]
	
	random1 = coords[3]
	random2 = coords[7]

	distance1 = dist_array(random1, coords)
	distance2 = dist_array(random2, coords)

	sq_dist1 = map(lambda x: x ** x, distance1)
	sq_dist2 = map(lambda x: x ** x, distance2)

	print(distance1)
	print(distance2)

	print(sq_dist1)
	print(sq_dist2)

def main():
	coords = import_coords(path)

	random1 = (0, 0)
	random2 = (0, 0)
	
	while random1 == random2:
		random1 = random_point(coords)
		random2 = random_point(coords)
	
	distance1 = squared_dist_array(random1, coords)
	distance2 = squared_dist_array(random2, coords)
	
	print(squared_dist)

def random_point(coords):
	return random.choice(coords)

def import_coords(file_name):
	coords = []
	with open(file_name) as file:
		for line in file:
			raw_coords = line.split(",")
			coords.append((float(raw_coords[0]), float(raw_coords[1])))
	return coords

test()
# main()
