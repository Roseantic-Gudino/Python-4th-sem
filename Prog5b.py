import re

phone_regex= re.compile('\+\d{12}')
email_regex= re.compile('[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-z|a-z]{2,}')
with open('Fileforprogram5b.txt', 'r') as f:
    for line in  f:
        matches=phone_regex.findall(line)
        for match in matches:
            print(match)

        matches=email_regex.findall(line)
        for match in matches:
            print(match)
