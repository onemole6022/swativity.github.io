import os
import json

data = []

def create_json_entry(path):
    # Split the file path
    parts = path.split(os.sep)
    # Extract the tag (e.g., "Cloth", "Jewellery")
    tag = parts[-2]
    # Extract the file name without extension (e.g., "IMG-1545")
    file_name = os.path.splitext(parts[-1])[0]
    # Split the file name to get title and subtitle (e.g., "IMG", "1545")
    # try:
    #     title, subtitle = file_name.split('_')
    # except:
    title = ""
    subtitle = ""

    # Create dictionary entry
    return {
        "filepath": path,
        "tag": tag,
        "title": title,
        "subtitle": subtitle
    }

 
def list_files_recursive(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            filepath = full_path
            data.append(create_json_entry(filepath))

    with open("file_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
 
# Specify the directory path you want to start from
directory = 'assets/img/portfolio'
list_files_recursive(directory)