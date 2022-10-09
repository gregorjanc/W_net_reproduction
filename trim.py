import csv

rows = []

file = "losses_17_58_57"

with open(f'{file}.csv') as csvfile:
	read = csv.reader(csvfile)
	for i, row in enumerate(read):
		if i % 10000 == 0 or i == 0:
			rows.append(row)


with open(f'{file}_lite.csv', 'w', newline="") as csvfile:
    write = csv.writer(csvfile)
    write.writerows(rows)
