import sys
import subprocess
import os
import re


curDir = os.path.dirname(__file__)
inputPath = os.path.abspath(os.path.join(curDir, "../../input"))
outputPath = os.path.abspath(os.path.join(curDir, "../../output"))
errorsPath = os.path.abspath(os.path.join(outputPath, "errors"))

files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
currentTest = None if len(files) < 2 else sorted(files)[0]

while currentTest:
    currentFile = os.path.abspath(os.path.join(inputPath, currentTest + ".p4"))
    tmpFile = os.path.abspath(os.path.join(inputPath, currentTest + ".tmp"))
    os.rename(currentFile, tmpFile)
    outFile = os.path.abspath(os.path.join(outputPath, currentTest + ".json"))

    output = subprocess.call([sys.executable, os.path.abspath(curDir + "/../p4-testcase-tester/main.py"), "-n " + currentTest, "-i " + tmpFile, "-o" + outFile, "-e " + errorsPath])

    os.remove(tmpFile)

    files = [os.path.splitext(f)[0] for f in os.listdir(inputPath) if re.match(r'[0-9]{10}\.p4', f)]
    currentTest = None if len(files) < 2 else sorted(files)[0]
