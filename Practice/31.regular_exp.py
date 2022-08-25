import re
m = ['isalnum','isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'ISALNUM', 'ISALPHA', 'ISDIGIT', 'ISLOWER', 'ISSPACE', 'ISTITLE', 'ISUPPER']
pattern = re.compile("is")
short_listed = [word for word in m if pattern.match(word)]
print(short_listed)