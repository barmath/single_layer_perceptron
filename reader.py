import csv

class CSV_reader:
	def read_csv(name_of_file):
		if name_of_file is None or len(name_of_file) == 0:
			return []

		converted = []

		with open(name_of_file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter = ',')
			for row in csv_reader:
				converted.append(row)
	
		return converted
