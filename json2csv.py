import csv, json, sys

input = open(sys.argv[1])
data = json.load(input)
input.close()

output = csv.writer(sys.stdout)

output.writerow(data[0].keys()[0])  # header row

for row in data:
    output.writerow(row.values()[0])
