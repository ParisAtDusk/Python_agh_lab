import re

def replace_words_regex(text, repl_dict):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in repl_dict.keys()) + r')\b')
    return pattern.sub(lambda x: repl_dict[x.group()], text)

input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur in ante leo. Morbi scelerisque feugiat felis, eu interdum massa sodales. "

print(replace_words_regex(input_text, {"Lorem": "AGH", "elit": "wiet"}))

