import re

def remove_words_regex(text, to_rem):
    pattern = r'\b(' + '|'.join(re.escape(word) for word in to_rem) + r')\b'
    return re.sub(pattern, '', text)

input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in ante leo. Morbi scelerisque feugiat felis, eu interdum massa sodales. "
print(remove_words_regex(input_text,{"Lorem", "elit"}))

