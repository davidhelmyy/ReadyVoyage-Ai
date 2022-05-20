
import json


with open('test.json') as json_file:
    map = json.load(json_file)

places=map["results"]
with open("filter.json", "w") as outfile:
    json.dump(places, outfile)


    
