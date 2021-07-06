import json
with open("shape_data.json", "w") as write_file:
    json.dump('sphere', write_file)
with open("size_data.json", "w") as write_file:
    json.dump(35, write_file)
with open("defects_data.json", "w") as write_file:
    json.dump(True,'Replacement, insertion', write_file)
with open("elements_data.json", "w") as write_file:
    json.dump('Pd, Ag', write_file)
