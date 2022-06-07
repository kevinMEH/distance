from calculate import random_point, total
from distance import *
from time import sleep

def step_v1(coords, t_limit, div_factor, file_path):
    # Find through steps method
    point1 = (0, 0)
    point2 = (0, 0)

    while point1 == point2:
        point1 = random_point(coords)
        point2 = random_point(coords)

    step_x = 0.05650488226427158 * 1.667
    step_y = 0.05288401249558794 * 1.667

    record = calc_score(coords, point1, point2)[0]
    limit = t_limit
    
    count = 0

    while True:
        new_scores = []
        # TOP
        new_scores.append(calc_score(coords, (point1[0], point1[1] + step_y), point2))
        # BOTTOM
        new_scores.append(calc_score(coords, (point1[0], point1[1] - step_y), point2))
        # LEFT
        new_scores.append(calc_score(coords, (point1[0] - step_x, point1[1]), point2))
        # RIGHT
        new_scores.append(calc_score(coords, (point1[0] + step_x, point1[1]), point2))

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
            step_x /= div_factor
            step_y /= div_factor
        
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
    
    file = open(file_path, "a")

    file.write(str(record) + " " + str(point1) + " " + str(point2) + " " + str(count) + "\n")
    print(record, point1, point2, count)
    print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️")
    
    file.close()

def calc_score(coords, point1, point2):
    distances1 = squared_dist_array(point1, coords)
    distances2 = squared_dist_array(point2, coords)
    (filtered1, filtered2) = filter_dist(distances1, distances2)
    return (total(filtered1) + total(filtered2), point1, point2)

def filter_dist(array1, array2):
    result_1 = []
    result_2 = []
    for i in range(0, len(array1)):
        if array1[i] < array2[i]:
            result_1.append(array1[i])
        else:
            result_2.append(array2[i])
    return (result_1, result_2)