from functools import reduce
import random
from time import sleep
from distance import *

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"
file_path = "./result.txt"

def main():
    coords = import_coords(path)
    div_factor = 1.15
    step_v2(coords, 2, 256, 4, div_factor)

def step_v2(coords, clusters, count_limit, limit_limit, div_factor):
    file = open(file_path, "a")
    
    # Point generation. Any number of points.
    points = []
    for _ in range(clusters):
        point = random_point(coords)
        while point in points:
            point = random_point(coords)
        points.append(point)
    
    # Default steps based on standard deviation
    step_x = 0.05650488226427158 * 2
    step_y = 0.05288401249558794 * 2
    
    record = calc_scores_any(coords, points)
    limit = limit_limit
    count = 0
    
    sqrt2div2 = sqrt(2) / 2
    
    while True:
        new_record = False
        # For each point, step and generate new points.
        # Calculate scores for new points.
        # Have a local record: Tracks highest of the new points
        # If local_record beats record: update the record,
        # reset limit, update point.
        # Record can update up to cluster times per while True
        for i, point in enumerate(points):
            dia_x = sqrt2div2 * step_x
            dia_y = sqrt2div2 * step_y
            new_scores = []
            new_points = [ *points ]
            # TOP LEFT
            stepped_point = (point[0] - dia_x, point[1] + dia_y)
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # TOP
            stepped_point = (point[0], point[1] + step_y)
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # TOP RIGHT
            stepped_point = (point[0] + dia_x, point[1] + dia_y)
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # LEFT
            stepped_point = (point[0] - step_x, point[1])
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # RIGHT
            stepped_point = (point[0] + step_x, point[1])
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # BOTTOM LEFT
            stepped_point = (point[0] - dia_x, point[1] - dia_y)
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # BOTTOM
            new_points[i] = stepped_point
            stepped_point = (point[0], point[1] - step_y)
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            # BOTTOM RIGHT
            stepped_point = (point[0] + dia_x, point[1] - dia_y)
            new_points[i] = stepped_point
            new_scores.append((calc_scores_any(coords, new_points), stepped_point))
            
            local_record = 99999
            local_record_point = new_scores[0][1]
            
            for score, new_point in new_scores:
                if score < local_record:
                    local_record = score
                    local_record_point = new_point
            
            if local_record < record:
                record = local_record
                points[i] = local_record_point
                new_record = True
                print(record, points)
            
        # If no new record updates: Decrease limit by 1.
        if not new_record:
            print(count, limit)
            limit = limit - 1
        else:
            limit = limit_limit
        
        if limit < limit_limit and count < count_limit:
            count = count + 1
            step_x /= div_factor
            step_y /= div_factor
        
        if count >= count_limit and limit <= 0:
            break
    
    
    file.write(str(record) + " " + str(points) + "\n")
    print(record, points)
    print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️")
    
    file.close()
    sleep(0.25)


def calc_scores_any(coords, points):
    dist_arrays = []
    for point in points:
        dist_arrays.append(squared_dist_array(point, coords))
    filtered_dists = filter_dist_any(dist_arrays)
    score = 0
    for dists in filtered_dists:
        score += total(dists)
    return score

def filter_dist_any(dist_arrays):
    if len(dist_arrays) == 0: return

    results = [ [] for _ in range(len(dist_arrays)) ]
    for i in range(len(dist_arrays[0])):
        record = 9999999
        record_index = 0
        for j, array in enumerate(dist_arrays):
            dist = array[i]
            if dist < record:
                record = dist
                record_index = j
        results[record_index].append(record)
    
    return results

def total(array):
    if len(array) == 0: return 0
    return reduce(lambda a, b: a + b, array)

def random_point(coords):
    return random.choice(coords)

def import_coords(file_name):
    coords = []
    with open(file_name) as file:
        for line in file:
            raw_coords = line.split(",")
            coords.append((float(raw_coords[0]), float(raw_coords[1])))
    return coords


main()
# test()
