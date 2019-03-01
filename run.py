from utils.myconfigparser import *
from urllib.request import urlopen
import pathlib
import os
import re, sys

CURSOR_UP_ONE = '\033[F'
ERASE_LINE = '\033[K'

parser = MyConfigParser()
parser.read("setup.cfg")
list_file = parser.get_url_file()
list_dir = parser.get_data_folder()

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
# print(os.path.abspath(os.path.curdir))
# out_file = open(os.path.curdir + "/output/html_out.txt", "w")

print("There are " + str(num_line) + " number of lines in the URL list.")
print("----------------------------------> scraping start")
# Try opening all the URL in the url list file
for x in range(0, num_line):
    html = urlopen(content[x])
    b = html.read()
    # print(b.decode("utf-8"))
    rtn = re.findall("//.*pdf", b.decode("utf-8"))
    if not rtn:
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
        print("Nothing returned in: " + content[x])
    else:
        out_file = open(os.path.curdir + "/output/pdf_list.txt", "a")
        for f in rtn:
            lk = "https:" + f
            sys.stdout.write(CURSOR_UP_ONE)
            sys.stdout.write(ERASE_LINE)
            print(lk)
            out_file.write(lk + "\n")
        out_file.close()
    # out_file.write(b.decode("utf-8"))