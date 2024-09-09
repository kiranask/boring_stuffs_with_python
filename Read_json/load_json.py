import json
# Open and read the Json File

with open('data_1.json') as file:
    data = json.load(file)

print(data)