import os
import argparse

from bmv2_random_program_generator import bmv2_random_program_generator
from common import common
from randomizer import randomizer

def main():
	parser = argparse.ArgumentParser(description="P4 Fuzzer Testcase Generator")
	parser.add_argument(
		'-f',
		'--filename',
		dest='filename',
		type=str,
		default='',
		help='<Required> The filename to be generated',
		required=True)
	parser.add_argument(
		'-s',
		'--show',
		dest='show',
		type=str,
		default='False',
		help='Show the generated program in console: True/False')
	args = parser.parse_args()

	filename = args.filename.strip()
	console = True if args.show == "True" or args.show == "true" else False

	# print the program to file
	file = open(filename, "w")

	seed = randomizer.generateRandomSeed()
	#seed = 4473699869
	randomizer.setSeed(seed)

	generator = bmv2_random_program_generator()
	code = generator.generate()
	common.output(code, console, file)

if __name__ == '__main__':
	main()