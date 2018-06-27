import sys
import basicutil

if len(sys.argv) != 2:
    print "usage: ", sys.argv[0], " file1 "
    exit(1)

file = sys.argv[1]

dates, values = basicutil.read_from_file (file)

for i in range(len(dates)):
    print dates[i], " , ", values[i], " , 0"

