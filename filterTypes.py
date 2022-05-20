import json


with open('test.json') as json_file:
    map = json.load(json_file)


for key, value in map.items() :
    print (key)