import json

with open("dirty.json", "r") as read_file:
    data = json.load(read_file)

unis = []

for each in data["dirty_university"]:
    unis.append(each['institution'])

unis.sort()

with open("data_file.json", "r") as read_file:
    data1 = json.load(read_file)

data1['universities'] = unis

with open("data_file.json", "w") as write_file:
    json.dump(data1,write_file,indent=4)

print('Success!')