from math import sqrt

def dist(ox, oy, tx, ty):
	return sqrt((ox - tx) ** 2 + (oy - ty) ** 2)

def squared_dist(ox, oy, tx, ty):
	return (ox - tx) ** 2 + (oy - ty) ** 2

def squared_dist_p(point1, point2):
    return squared_dist(point1[0], point1[1], point2[0], point2[1])

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

def closest_point(origin, coords):
	closest = coords[0]
	closest_squared_dist = squared_dist_p(origin, closest)

	for point in coords:
		sq_dist = squared_dist_p(origin, point)
		if sq_dist < closest_squared_dist:
			closest_squared_dist = sq_dist
			closest = point

	return closest

def closest_not(origin, coords, not_this):
    closest = coords[0]
    if closest == not_this:
        closest = coords[1]
    closest_squared_dist = squared_dist_p(origin, closest)
    
    for point in coords:
        if point == not_this:
            continue
        sq_dist = squared_dist_p(origin, point)
        if sq_dist < closest_squared_dist:
            closest_squared_dist = sq_dist
            closest = point
    
    return closest
