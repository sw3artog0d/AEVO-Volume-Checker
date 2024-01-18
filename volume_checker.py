import csv

total_volume = 0

with open('Your csv file') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        total_volume += (float(row[3]) * float(row[4]))
    print(round(total_volume / 2, 2))