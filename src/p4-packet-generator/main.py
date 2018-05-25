import commands
import sys

file = sys.argv[1]
bash_command = 'p4pktgen ' + file + ' -au -rss -d'
error, output = commands.getstatusoutput(bash_command)
filename = file.split('.')[0]
f = open('packets/' + filename + '.pkt','w')


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
