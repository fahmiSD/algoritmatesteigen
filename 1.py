import re

txt = "NEGIE1"

def reverse_preserve_number(text):
    match = re.search(r'([A-Z]+)(\d*)$', text)
    if match:
        letters_to_reverse = match.group(1) 
        part_after_letters = match.group(2)
        return letters_to_reverse[::-1] + part_after_letters
    else:
        return text[::-1]

print(reverse_preserve_number(txt))