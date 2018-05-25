import sys
import subprocess
import os
import re
import shutil
import mysql.connector


curDir = os.path.dirname(__file__)
inputPath = os.path.join(curDir, "../input")
outputPath = os.path.join(curDir, "../output")
errorsPath = os.path.join(outputPath, "errors")

cnx = mysql.connector.connect(user="p4-compiler-fuzzer", password="p4-compiler-fuzzer", host="localhost", database="fuzzer")
cursor = cnx.cursor()

add_bug = "INSERT INTO bugs (`test`, `error`, `file`, `seed`, `known`) VALUES (%s, %s, %s, %s, %s)"

files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
currentTest = None if len(files) < 2 else sorted(files)[0]

while currentTest:
    currentFile = os.path.join(inputPath, currentTest + ".p4")
    tmpFile = os.path.join(inputPath, currentTest + ".tmp")
    os.rename(currentFile, tmpFile)
    outFile = os.path.join(outputPath, currentTest + ".json")

    try:
        result = subprocess.check_output(["/usr/local/bin/p4c-bm2-ss " + tmpFile + " -o " + outFile + " > /dev/null"],
                                         stderr=subprocess.STDOUT, shell=True)
        print "Test " + currentTest + " passed"
    except subprocess.CalledProcessError as e:
        errorFile = os.path.join(errorsPath, currentTest + ".p4")
        errorLogFile = os.path.join(errorsPath, currentTest + ".err")
        seed_line = open(tmpFile).readline().rstrip()
        seed_match = re.search('//seed: ([0-9]+)', seed_line)
        seed = seed_match.group(1) if seed_match is not None else 0
        shutil.copyfile(tmpFile, errorFile)
        f = open(errorLogFile, "w")
        f.write(e.output)
        f.close()

        data_bug = (currentTest, e.output, errorFile, seed, 0)
        cursor.execute(add_bug, data_bug)
        cnx.commit()

        print "Test " + currentTest + " failed"

    os.remove(tmpFile)

    files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
    currentTest = None if len(files) < 2 else sorted(files)[0]
