import os
import argparse
from datetime import datetime

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
	#seed = 2470199104
	randomizer.setSeed(seed)
	print "Seed: " + str(seed)

	generator = bmv2_random_program_generator()
	dt1 = datetime.now()
	code = generator.generate()
	dt2 = datetime.now()

	code = "//unique_tokens: " + str(len(common.tokens.keys())) + "\n" + "//tokens: " + str(common.get_total_tokens()) + "\n" + "//size: " + str(len(code.encode('utf-8'))) + "\n" + code

	print "Unique tokens: " + str(len(common.tokens.keys()))
	print "Tokens: " + str(common.get_total_tokens())
	print "Size: " + str(len(code.encode('utf-8')))

	diff = dt2 - dt1

	print "Time: " + str(diff.total_seconds())

	common.output(code, console, file)

if __name__ == '__main__':
	main()