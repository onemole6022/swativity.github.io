import os
import json

data = []

def create_json_entry(path):
    # Split the file path
    parts = path.split(os.sep)
    # Extract the tag (e.g., "Cloth", "Jewellery")
    tag = parts[-2]
    # Extract the file name and extension (e.g., "IMG-1545" and ".JPG")
    file_name, file_ext = os.path.splitext(parts[-1])
    
    # Construct the placeholder file path by inserting 'Placeholder ' before the file name
    placeholder_file = f"Placeholder {file_name}{file_ext}"
    placeholder_path = os.path.join(os.sep.join(parts[:-1]), placeholder_file)

    # Split the file name to get title and subtitle (e.g., "IMG", "1545")
    title = ""
    subtitle = ""

    # Create dictionary entry
    return {
        "filepath": path,
        "placeholder": placeholder_path,  # Add the placeholder key with the same file extension
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
            # Skip files that contain "Placeholder" in the file name
            if "Placeholder" not in os.path.basename(filepath):
                data.append(create_json_entry(filepath))

    with open("file_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
 
# Specify the directory path you want to start from
directory = 'assets/img/portfolio'
list_files_recursive(directory)
