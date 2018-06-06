import commands
import sys
import os

curDir = os.path.dirname(__file__)
file_path = sys.argv[1]
file = os.path.abspath(os.path.join(curDir, file_path))
bash_command = 'p4pktgen ' + file + ' -au -rss -d'
error, output = commands.getstatusoutput(bash_command)
filename = os.path.splitext(file)[0]
f = open(filename + '.pkt','w+')


for line in output.splitlines():
        if 'INFO: table_add' in line:
                l = line.replace('INFO: table_add ','')
                # print 'writing: '+ l
                f.write(l)
                f.write('\n')
        if 'INFO: packet' in line:
                l = line.split(") ",1)[1]
                f.write(l)
                f.write('\n')
f.close()
