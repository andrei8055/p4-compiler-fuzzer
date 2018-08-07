import sys
import subprocess
import os
import re
import mysql.connector

from datetime import datetime

cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
cursor = cnx.cursor()

curDir = os.path.dirname(__file__)
inputPath = os.path.abspath(os.path.join(curDir, "../../input"))

files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
sortedFiles = sorted(files)

lastNo = 0 if not sortedFiles else int(sortedFiles[-1])

maxNo = 1000 if len(sys.argv) < 2 or not sys.argv[1].isdigit() else int(sys.argv[1])

curNo = lastNo

while curNo < maxNo:
    curNo += 1
    filename = str(curNo).zfill(10)
    filepath = os.path.abspath(os.path.join(curDir, "../../input/" + filename + ".p4"))
    print "Generating test " + filename

    dt1 = datetime.now()
    subprocess.call([sys.executable, os.path.abspath(curDir + "/../p4-testcase-generator/main.py"), "-t netfpga", "-f " + filepath, "-s false"])
    print "test"
    dt2 = datetime.now()
    diff = dt2 - dt1

    input_obj = open(filepath)

    unique_tokens_line = input_obj.readline().rstrip()
    unique_tokens_match = re.search('//unique_tokens: ([0-9]+)', unique_tokens_line)
    unique_tokens = unique_tokens_match.group(1) if unique_tokens_match is not None else 0

    tokens_line = input_obj.readline().rstrip()
    tokens_match = re.search('//tokens: ([0-9]+)', tokens_line)
    tokens = tokens_match.group(1) if tokens_match is not None else 0

    size_line = input_obj.readline().rstrip()
    size_match = re.search('//size: ([0-9]+)', size_line)
    size = size_match.group(1) if size_match is not None else 0

    seed_line = input_obj.readline().rstrip()
    seed_match = re.search('//seed: ([0-9]+)', seed_line)
    seed = seed_match.group(1) if seed_match is not None else 0

    data = (filename, seed, unique_tokens, tokens, size, diff.total_seconds())
    cursor.execute("INSERT INTO tests (`test`, `seed`, `unique_tokens`, `tokens`, `f_size`, `generate_time`) VALUES (%s, %s, %s, %s, %s, %s)", data)
    cnx.commit()
    print "Test " + filename + " generated"
