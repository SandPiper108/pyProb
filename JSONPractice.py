import json

def read(fileName): #Func to read in the new file, opens new dictionary if empty
    new_file = open(fileName, "r")
    json_object = json.load(new_file)
    new_file.close()
    try:
        return json_object
    except JSONDecodeError:
        return {}

def write(fileName, objName): #Func to change new file, req defining obj below
    new_file = open(fileName, "w")
    json.dump(objName, new_file, indent=4)
    new_file.close()

def main():
    a = "size_data.json"
    size_data = read(a)
    size_data["particle1"] = 35
    size_data["particle2"] = 56
    write("size_data.json", size_data)
    print(size_data)

if __name__ == "__main__":
    main()