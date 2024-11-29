import os

def list_files_recursive(directory):

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
    
        if os.path.isfile(path):
            print(path)

        elif os.path.isdir(path):
            list_files_recursive(path)

list_files_recursive("/home")
