# JSON
# - JavaScript Object Notation
# - Text Based Format
# - JSON format is preferred over XML for its simplicity and flexibility

# Serialization
# - Process of encoding JSON is referred to Serialization

# Deserialization
# - Reverse process of Serialization
# - Decoding data that is stored in JSON Format

# In build paclkage json

import json
import traceback
import requests

try:
    json_inp_str = '{"ID": 6, "Address": "551 Alvarado St", "City": "San Francisco", "State": "CA 94114", "Country": "USA", "Name": "Richvalley", "Employees": 20}'
    json_out_str = ""
    json_inp_dict = dict({"ID": 6, "Address": "551 Alvarado St", "City": "San Francisco",
                          "State": "CA 94114", "Country": "USA", "Name": "Richvalley", "Employees": 20})
    json_out_dict = {}

    json_inp_file = "../assets/sample.json"
    json_out_file = "../assets/output/parse-json-output.json"
    # json_inp_file = "d:/Practise/Python/learn-python/assets/sample.json"
    # json_out_file = "d:/Practise/Python/learn-python/assets/output/parse-json-output.json"

    # dump() serializes the JSON data and writes to a file-like object
    with open(json_out_file, "w") as fp_json_out_file:
        json.dump(json_inp_str, fp_json_out_file)

    # dumps() returns a Python str object
    json_out_str = json.dumps(json_inp_dict)

    with open(json_inp_file, "r") as fp_json_inp_file:
        json_out_dict = json.load(fp_json_inp_file)

    json_out_str = json.loads(json_inp_str)

    URL = "https://jsonplaceholder.typicode.com/todos"
    vResponse = requests.get(URL)  # HTTP GET
    vJSONData = json.loads(vResponse.text)
    print(vJSONData)

    with open(json_out_file, 'w') as fp_json_out_file:
        json.dump(vResponse.json(), fp_json_out_file)

except Exception as e:
    traceback.print_exc()
else:
    print(f"No exceptions occurred")
