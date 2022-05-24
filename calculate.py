from functools import reduce
import random
from statistics import stdev
from time import sleep
from distance import *

path = "/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv"
path = "./coordinates.csv"

file_path = "./result.txt"

def main():
    coords = import_coords(path)
    t_limit = 200
    while True:
        file = open(file_path, "a")
    
        # Find through steps method
        point1 = (0, 0)
        point2 = (0, 0)

        while point1 == point2:
            point1 = random_point(coords)
            point2 = random_point(coords)

        step_x = stdev(map(lambda coord: coord[0], coords)) * 1.667
        step_y = stdev(map(lambda coord: coord[1], coords)) * 1.667

        record = calc_score(coords, point1, point2)[0]
        limit = t_limit
        
        count = 0

        while True:
            new_scores = []
            # TOP
            new_point = closest_not((point1[0], point1[1] + step_y), coords, point1)
            new_scores.append(calc_score(coords, new_point, point2))
            # BOTTOM
            new_point = closest_not((point1[0], point1[1] - step_y), coords, point1)
            new_scores.append(calc_score(coords, new_point, point2))
            # LEFT
            new_point = closest_not((point1[0] - step_x, point1[1]), coords, point1)
            new_scores.append(calc_score(coords, new_point, point2))
            # RIGHT
            new_point = closest_not((point1[0] + step_x, point1[1]), coords, point1)
            new_scores.append(calc_score(coords, new_point, point2))

            for (score, new_point1, _) in new_scores:
                # If new record: Note new record, reset limit
                # If same record: Decrease limit by one.
                # If smaller record: Ignore
                if score < record:
                    record = score
                    point1 = new_point1
                    limit = t_limit
                    print(record, point1, point2)
                else:
                    limit = limit - 1

            
            if limit < t_limit - 1 and count < t_limit:
                count = count + 1
                step_x /= 1.03
                step_y /= 1.03
            
            if count == t_limit:
                limit = t_limit
                count = 9999
            
            # If there hasn't been a new record in multiple moves,
            # we've reached the end.
            if limit <= 0:
                break
            
            # Swap point1 and point2
            temp = point1
            point1 = point2
            point2 = temp
        
        file.write(str(record) + " " + str(point1) + " " + str(point2) + " " + str(count) + "\n")
        print(record, point1, point2, count)
        print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️")
        
        file.close()
        sleep(0.25)

def test():
    coords = import_coords(path)
    coords = coords[0:14]

    random1 = coords[3]
    random2 = coords[7]

    distance1 = dist_array(random1, coords)
    distance2 = dist_array(random2, coords)

    sq_dist1 = map(lambda x: x * x, distance1)
    sq_dist2 = map(lambda x: x * x, distance2)
    
    (filtered1, filtered2) = filter_dist(sq_dist1, sq_dist2)
    
    print(total(filtered1) + total(filtered2));

def calc_score(coords, point1, point2):
    distances1 = squared_dist_array(point1, coords)
    distances2 = squared_dist_array(point2, coords)
    (filtered1, filtered2) = filter_dist(distances1, distances2)
    return (total(filtered1) + total(filtered2), point1, point2)

def total(array):
    if len(array) == 0: return 0
    return reduce(lambda a, b: a + b, array)

def filter_dist(array1, array2):
    result_1 = []
    result_2 = []
    for i in range(0, len(array1)):
        if array1[i] < array2[i]:
            result_1.append(array1[i])
        else:
            result_2.append(array2[i])
    return (result_1, result_2)

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
