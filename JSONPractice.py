import json

size_file = open("size_data.json", "r")
json_sizes = json.load(size_file)
size_file.close()

json_sizes["particle1"] = 35
print(json_sizes)

size_file = open("size_data.json", "w")
json.dump(json_sizes, size_file)
size_file.close()