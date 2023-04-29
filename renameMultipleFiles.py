import os
path = "C:\\xampp\\htdocs\\sign\\img"
i = 64
for filename in os.listdir(path):
  i = i + 1
  os.rename(os.path.join(path, filename), os.path.join(path,str(chr(i)) + '.jpg'))