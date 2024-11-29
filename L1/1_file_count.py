import os

def count_files(directory):
    items = os.listdir(directory)
    file_count = sum(1 for it in items if os.path.isfile(os.path.join(directory, it)))
    print(f"The number of files in '{directory}' is: {file_count}")

count_files("/usr/bin") # On my machine outputs: 3246

