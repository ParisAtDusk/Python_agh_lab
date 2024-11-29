
def replace_words(text, repl):
    for old_word, new_word in repl.items():
        text = text.replace(old_word, new_word)
    return text

input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in ante leo. Morbi scelerisque feugiat felis, eu interdum massa sodales. "
print(replace_words(input_text, {"Lorem": "AGH", "elit": "wiet"}))

