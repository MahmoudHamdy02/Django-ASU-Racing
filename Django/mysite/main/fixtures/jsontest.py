import json

with open('data.json') as f:
	data = json.load(f)


for person in data:
	if person['fields']['name'] != None and person['fields']['phone'] != None and person['fields']['email'] != None:
		print(person['fields'])

