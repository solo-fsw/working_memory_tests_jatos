import os
import json


def list_jatos_results(directory):
  try:
    files = os.listdir(directory)
    return files
  except FileNotFoundError:
    return f"Directory {directory} not found."

def parse_txt_to_json(directory, file):
  try:
    file = os.path.join(directory, file)
    with open(file, 'r') as f:
      data = f.read()
    json_data = json.loads(data)
    json_file = file.replace('.txt', '.json')
    with open(json_file, 'w') as f:
      json.dump(json_data, f, indent=4)
    return f"File {json_file} created successfully.", json_data
  except FileNotFoundError:
    return f"File {file} not found."

def get_unique_keys(json_data):
  keys = set()
  for data in json_data:
    for key, value in data.items():
      keys.add(key)
      if isinstance(value, dict):
        keys.update(get_unique_keys(value))
  return keys


if __name__ == "__main__":
  directory = "JATOS results"
  files = list_jatos_results(directory)
  for file in files:
    parse_txt_to_json(directory, file)
    _, json_data = parse_txt_to_json(directory, file)
    keys = get_unique_keys(json_data)
  print("Files converted successfully.")
  print("Unique keys in JSON files:")
  print(keys)