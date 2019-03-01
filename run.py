from utils.myconfigparser import *

parser = MyConfigParser()
parser.read("setup.cfg")
print(parser.get_URL_file())
print(parser.get_data_folder())


