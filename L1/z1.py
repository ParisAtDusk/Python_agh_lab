import os
import re
import random as rd

def count_files(directory):
    items = os.listdir(directory)
    file_count = sum(1 for item in items if os.path.isfile(os.path.join(directory, item)))
    print(f"The number of files in '{directory}' is: {file_count}")


def list_files_recursive(directory):

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
    
        if os.path.isfile(path):
            print(path)

        elif os.path.isdir(path):
            list_files_recursive(path)

def remove_words(text, to_rem):
    for word in to_rem:
        text = text.replace(word, "")
    return text

def replace_words(text, repl):
    for old_word, new_word in repl.items():
        text = text.replace(old_word, new_word)
    return text

def remove_words_regex(text, to_rem):
    pattern = r'\b(' + '|'.join(re.escape(word) for word in to_rem) + r')\b'
    return re.sub(pattern, '', text)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_numbers_bubble = bubble_sort(numbers[:])
print("Bubble Sort result:", sorted_numbers_bubble)


input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in ante leo. Morbi scelerisque feugiat felis, eu interdum massa sodales. "

replacement_dict = {"Lorem": "AGH", "elit": "wiet"}

print(remove_words_regex(input_text,{"Lorem"}))
print(replace_words(input_text, replacement_dict))

print(remove_words(input_text,{"Lorem", "elit"}))

list_files_recursive("/home/kita/Documents")

count_files("/dev")
