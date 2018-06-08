import argparse
import subprocess
import os
import re
import shutil
import mysql.connector

from datetime import datetime

def main():
	parser = argparse.ArgumentParser(description="P4 Fuzzer Testcase Tester")
	parser.add_argument(
		'-n',
		'--number',
		dest='number',
		type=str,
		default='',
		help='<Required> The testcase number',
		required=True)
	parser.add_argument(
		'-i',
		'--input',
		dest='input',
		type=str,
		default='',
		help='<Required> The filename to be tested',
		required=True)
	parser.add_argument(
		'-o',
		'--output',
		dest='output',
		type=str,
		default='',
		help='<Required> The filename to be compiled',
		required=True)
	parser.add_argument(
		'-e',
		'--errors',
		dest='errors',
		type=str,
		default='',
		help='<Required> Path for the errors folder',
		required=True)
	parser.add_argument(
		'-t',
		'--target',
		dest='target',
		type=str,
		default='bmv2',
		help='The target for the code generation: bmv2/ebpf')
	args = parser.parse_args()

	currentTest = args.number.strip()
	input = args.input.strip()
	output = args.output.strip()
	errorsPath = args.errors.strip()
	target = args.target

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()
	add_bug = "INSERT INTO bugs (`test`, `error`, `file`, `seed`, `known`) VALUES (%s, %s, %s, %s, %s)"

	input_obj = open(input)

	unique_tokens_line = input_obj.readline().rstrip()
	unique_tokens_match = re.search('//unique_tokens: ([0-9]+)', unique_tokens_line)
	unique_tokens = unique_tokens_match.group(1) if unique_tokens_match is not None else 0

	tokens_line = input_obj.readline().rstrip()
	tokens_match = re.search('//tokens: ([0-9]+)', tokens_line)
	tokens = tokens_match.group(1) if tokens_match is not None else 0

	size_line = input_obj.readline().rstrip()
	size_match = re.search('//size: ([0-9]+)', size_line)
	size = size_match.group(1) if size_match is not None else 0

	dt1 = datetime.now()
	try:
		if target == "bmv2":
			result = subprocess.check_output(["/usr/local/bin/p4c-bm2-ss --Wdisable " + input + " -o " + output + " > /dev/null"],
										 stderr=subprocess.STDOUT, shell=True)
		else:
			result = subprocess.check_output(["/usr/local/bin/p4c-ebpf --Wdisable " + input + " -o " + output + " > /dev/null"],
										 stderr=subprocess.STDOUT, shell=True)
		print "Test " + currentTest + " passed"
	except subprocess.CalledProcessError as e:
		errorFile = os.path.abspath(os.path.join(errorsPath, currentTest + ".p4"))
		errorLogFile = os.path.abspath(os.path.join(errorsPath, currentTest + ".err"))

		seed_line = input_obj.readline().rstrip()
		seed_match = re.search('//seed: ([0-9]+)', seed_line)
		seed = seed_match.group(1) if seed_match is not None else 0

		shutil.copyfile(input, errorFile)
		f = open(errorLogFile, "w")
		f.write(e.output)
		f.close()

		data_bug = (currentTest, e.output, errorFile, seed, 0)
		cursor.execute(add_bug, data_bug)
		cnx.commit()

		print "Test " + currentTest + " failed"
	finally:
		dt2 = datetime.now()
		diff = dt2 - dt1
		print "Unique tokens: " + str(unique_tokens)
		print "Tokens: " + str(tokens)
		print "Size: " + str(size)
		print "Time: " + str(diff.total_seconds())
		cursor.execute("UPDATE tests SET `compile_time`=" + str(diff.total_seconds()) + " WHERE `test` LIKE '" + currentTest + "'")
		cnx.commit()



if __name__ == '__main__':
	main()