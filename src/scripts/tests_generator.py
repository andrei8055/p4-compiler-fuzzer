import sys
import subprocess
import os
import re

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
    subprocess.call([sys.executable, os.path.abspath(curDir + "/../p4-testcase-generator/main.py"), "-f " + filepath, "-s false"])
    print "Test " + filename + " generated"
