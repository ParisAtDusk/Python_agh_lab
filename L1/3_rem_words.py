def remove_words(text, to_rem):
    for word in to_rem:
        text = text.replace(word, "")
    return text

input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in ante leo. Morbi scelerisque feugiat felis, eu interdum massa sodales. "
print(remove_words(input_text,{"Lorem", "elit"}))
