'''this module finds all numbers in text.'''

import re

text = """If 300 spartans were so brave, so 500 spartans could destroy more than 10k warriors of Darius,
       but 15k and even 20k."""
template = re.compile('\d+')
res = template.findall(text)
print(res)