import re

match = re.search("abc", "aabca")
print(match.group())  # abc is found in text
match = re.search("xyz", "aabca")
print(match is None)  # no match

