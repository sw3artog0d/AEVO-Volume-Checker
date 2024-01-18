import csv

value_per_trade = []


with open('Your csv file') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if i == 0:
            i += 1
            continue
        value_per_trade.append(round(float(row[3]) * float(row[4]), 4))
total_value = 0

for i in range(len(value_per_trade)):
    total_value += value_per_trade[i]
print(round(total_value / 2, 4))