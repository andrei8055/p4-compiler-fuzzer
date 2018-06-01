import argparse
import subprocess
import os
import re
import shutil
import mysql.connector

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
	args = parser.parse_args()

	currentTest = args.number.strip()
	input = args.input.strip()
	output = args.output.strip()
	errorsPath = args.errors.strip()

	cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
	cursor = cnx.cursor()
	add_bug = "INSERT INTO bugs (`test`, `error`, `file`, `seed`, `known`) VALUES (%s, %s, %s, %s, %s)"

	try:
		result = subprocess.check_output(["/usr/local/bin/p4c-bm2-ss --Wdisable " + input + " -o " + output + " > /dev/null"],
										 stderr=subprocess.STDOUT, shell=True)
		print "Test " + currentTest + " passed"
	except subprocess.CalledProcessError as e:
		errorFile = os.path.abspath(os.path.join(errorsPath, currentTest + ".p4"))
		errorLogFile = os.path.abspath(os.path.join(errorsPath, currentTest + ".err"))
		seed_line = open(input).readline().rstrip()
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


if __name__ == '__main__':
	main()