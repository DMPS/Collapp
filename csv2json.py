import csv
import json

csvfile = open('CollaborateCSV.csv', 'r')
jsonfile = open('collab.json', 'w')

fieldnames = ("Subject Discipline","Topic Name","Keyword","Hint")
reader = csv.DictReader(csvfile, fieldnames)
topics = {}

for row in reader:
	if topics[row["Topic Name"]] = None:
		topic_name = row["Topic Name"]
		#create a new object
		topics[topic_name] = '"' + topic_name + '"' +":[]"	
	obj = {

			"Keyword":row["Keyword"],
			"Hint":row["Hint"],
			"Subject Discipline":row["Subject Discipline"]
			
	}
	topics[row["Topic Name"]].push(obj)
jsonfile.write(topics)
