import csv
import json
import hashlib

# File paths
csvFilePath = r'HNGi9 CSV FILE - Sheet1.csv'
jsonFilePath = r'sheet1.json'

def main():

    make_json(csvFilePath=r'HNGi9 CSV FILE - Sheet1.csv', jsonFilePath=r'sheet1.json')
    result = encode(jsonFilePath)
    print(result)

# Generate a compatible CHIP-0007 json from csv provided
def make_json(csvFilePath, jsonFilePath):

    data = {}

    # open csv reader
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)

        # convert into dictionary
        for rows in csvReader:
            key = rows['Series Number']
            data[key] = rows

    # write to json
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        
 

# Calculate the sha256 of the json file

def encode(json_file):

    json_file = 'sheet1.json'

    result = hashlib.sha256(json_file.encode())
    print(result.hexdigest())

# Append to each line of csv(as a filename.output.csv)

if __name__ == "__main__":
    main()
