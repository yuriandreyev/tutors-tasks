import re

text = 'horse 300 power. 380 volt'
template = re.compile(' 3\d0 ')
res = template.findall(text)

print(res)
