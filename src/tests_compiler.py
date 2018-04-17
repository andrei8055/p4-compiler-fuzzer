import sys
import subprocess
import os
import re
import shutil

curDir = os.path.dirname(__file__)
inputPath = os.path.join(curDir, "../input")
outputPath = os.path.join(curDir, "../output")
errorsPath = os.path.join(outputPath, "errors")

files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
currentTest = None if not files else sorted(files)[0]

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
        shutil.copyfile(tmpFile, errorFile)
        f = open(errorLogFile, "w")
        f.write(e.output)
        f.close()
        # TODO: insert in database
        print "Test " + currentTest + " failed"

    os.remove(tmpFile)

    files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
    currentTest = None if not files else sorted(files)[0]
