import csv


def csv_write(fieldnames,data):
	with open('Balance.csv', 'a') as outfile:
		writer = csv.DictWriter(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,fieldnames=fieldnames)
		#writer.writeheader()
		for row in data:
			writer.writerow(row)


    
 
