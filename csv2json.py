import csv
import json

def csv2json(*readurl,*writeurl):
	csvfile = open(readurl, 'r')
	jsonfile = open(writeurl, 'w')

	fieldnames = ("Subject Discipline","Topic Name","Keyword","Hint")
	reader = csv.DictReader(csvfile, fieldnames)

	topics = {}
	print(reader)

	for row in reader:
		print(row)
		if row["Topic Name"] not in topics:
			topic_name = row["Topic Name"]
			#create a new object
			topics[topic_name] = []
		obj = {

				"Keyword":row["Keyword"],
				"Hint":row["Hint"],
				"Subject Discipline":row["Subject Discipline"]
				
		}
		topics[row["Topic Name"]].append(obj)

	jsonfile.write(str(topics))
