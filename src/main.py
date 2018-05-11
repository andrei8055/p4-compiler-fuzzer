import sys
import os

from bmv2_random_program_generator import bmv2_random_program_generator
from common import common

filename = ""
console = False

if len(sys.argv) > 1:
	filename = sys.argv[1]
	if sys.argv[2] == "false":
		console = False
	else:
		console = True
else:
	sys.exit("Error! Missing argument 1 - output filename")

# print the program to file
curdir = os.path.dirname(__file__)
file_path = os.path.join(curdir, filename)
file = open(file_path, "w")

generator = bmv2_random_program_generator()
code = generator.generate()
common.output(code, console, file)