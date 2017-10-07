import csv
def csv_read():
	
	with open('Balance.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)

