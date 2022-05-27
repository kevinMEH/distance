from functools import reduce
import random
from distance import *

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
    if len(dist_arrays) == 0:
        print("Error: dist_array length 0. (filter_dist_any)")
        return

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

def calc_scores_with_filtered(coords, points):
    dist_arrays = []
    for point in points:
        dist_arrays.append(squared_dist_array(point, coords))
    filtered_dists, filtered_points = filter_dist_with_points(coords, dist_arrays)
    score = 0
    for dists in filtered_dists:
        score += total(dists)
    return (score, filtered_dists, filtered_points)

def filter_dist_with_points(coords, dist_arrays):
    if len(dist_arrays) == 0:
        print("Error: dist_arrays length 0. (filter_dist_with_points)")
        return

    filtered_dists = [ [] for _ in range(len(dist_arrays)) ]
    filtered_points = [ [] for _ in range(len(dist_arrays)) ]
    for point_index in range(len(dist_arrays[0])):
        record = 9999999
        record_dist_index = 0
        for j, array in enumerate(dist_arrays):
            dist = array[point_index]
            if dist < record:
                record = dist
                record_dist_index = j
        filtered_dists[record_dist_index].append(record)
        filtered_points[record_dist_index].append(coords[point_index])
    
    return filtered_dists, filtered_points

def total(array):
    if len(array) == 0: return 0
    return reduce(lambda a, b: a + b, array)

def random_point(coords):
    return random.choice(coords)
