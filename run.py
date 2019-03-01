from utils.myconfigparser import *
from urllib.request import urlopen
import pathlib
import os

parser = MyConfigParser()
parser.read("setup.cfg")
list_file = parser.get_url_file()
list_dir = parser.get_data_folder()

print(list_dir)
print(list_file)

p = pathlib.Path(list_dir + '/' +list_file)

# Test if the path exist
if (p.exists()):
    print("The path exists.")

# Open all the
with p.open('r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

num_line = len(content)

# Open an output file
print(os.path.abspath(os.path.curdir))
out_file = open(os.path.curdir + "/output/html_out.txt", "w")

print("There are " + str(num_line) + " number of lines in the URL list.")

for x in range(1, 2):
    print(content[x])
    html = urlopen(content[x])
    b = html.read()
    out_file.write(b.decode("utf-8"))