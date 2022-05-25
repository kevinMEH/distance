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
