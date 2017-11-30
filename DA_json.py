# encoding = -utf-8-
import json

json_file = open('json_obj.json', 'r')
## loads : read from strings
## load  : read from file
data = json.load(json_file)
print(str(data))

print(type(data))
print(data['diet'])

json_dumps = json.dumps(data)
print(json_dumps)

json_dump = json.dump(data, open('data.json', 'w'))
print(str(json_dump))

print(str(json.load(open('data.json'))))










