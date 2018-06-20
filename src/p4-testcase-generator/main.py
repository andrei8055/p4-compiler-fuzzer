import os
import argparse
import signal
from datetime import datetime

from bmv2_random_program_generator import bmv2_random_program_generator
from ebpf_random_program_generator import ebpf_random_program_generator
from common import common
from randomizer import randomizer

def signaled(signum, frame):
	print "Test generation failed (generation time too long)"

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
	parser.add_argument(
		'-t',
		'--target',
		dest='target',
		type=str,
		default='bmv2',
		help='The target for the code generation: bmv2/ebpf')
	parser.add_argument(
		'--seed',
		dest='seed',
		type=str,
		default='',
		help='The seed for the randomizer')
	args = parser.parse_args()

	filename = args.filename.strip()
	console = True if args.show == "True" or args.show == "true" else False
	target = args.target
	seed = args.seed

	# print the program to file
	file = open(filename, "w+")

	seed = int(seed) if seed != "" else randomizer.generateRandomSeed()
	#seed = 2470199104
	randomizer.setSeed(seed)
	print "Seed: " + str(seed)

	generator = bmv2_random_program_generator() if target == "bmv2" else ebpf_random_program_generator()
	dt1 = datetime.now()
	signal.signal(signal.SIGALRM, signaled)
	signal.alarm(15)
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