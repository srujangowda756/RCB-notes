import re

text = 'srujan991@gmail.com'

pattern = r"[a-z0-9]+@+[a-z.-]+.com"

emails = re.findall(pattern, text, re.IGNORECASE)

print(list(set(emails)))  # removes duplicates