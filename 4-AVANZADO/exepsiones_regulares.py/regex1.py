import re

text = """The quick brown fox jumps over the lazy dog"""

x = re.search("^The.*dog$", text)
print (type(x))
if x:
  print("SI")
else:
  print("NO")