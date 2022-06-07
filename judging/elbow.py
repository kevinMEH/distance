from genericpath import exists
from plot import line_plot

folder = "./results/"

def elbow(ending, folder = folder):
    centroid_count = []
    records = []
    for i in range(21):
        path = folder + str(i) + ending
        if exists(path):
            with open(path) as file:
                file_records = []
                for line in file:
                    values = line.split(" ")
                    file_records.append(float(values[0]))

                if len(file_records) == 0:
                    continue;

                true_record = 999999
                for record in file_records:
                    if record < true_record:
                        true_record = record
                centroid_count.append(i)
                records.append(true_record)
    
    line_plot(centroid_count, records)
    