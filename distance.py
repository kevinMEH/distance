from math import sqrt

def dist(ox, oy, tx, ty):
	return sqrt((ox - tx) ** 2 + (oy - ty) ** 2)

def squared_dist(ox, oy, tx, ty):
	return (ox - tx) ** 2 + (oy - ty) ** 2

def total_squared_dist(point, coords):
	(ox, oy) = point
	result = 0
	for ( x, y ) in coords:
		result += squared_dist(ox, oy, x, y)
	return result

def dist_array(point, coords):
	distances = []
	(ox, oy) = point
	for ( x, y ) in coords:
		distances.append(dist(ox, oy, x, y))
	return distances

def squared_dist_array(point, coords):
	distances = []
	(ox, oy) = point
	for ( x, y ) in coords:
		distances.append(squared_dist(ox, oy, x, y))
	return distances

def closest_point(point, coords):
	(ox, oy) = point
	closest = coords[0]
	closest_squared_dist = sq_dist(ox, oy, coords[0][0], coords[0][1])

	for ( x, y ) in coords:
		sq_dist = sq_dist(ox, oy, x, y)
		if sq_dist < closest_squared_dist:
			closest_squared_dist = sq_dist
			closest = (x, y)

	return closest
