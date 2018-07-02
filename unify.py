import sys
import basicutil

if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " file1 file2"
    exit(1)

fileorig = sys.argv[1]
file = sys.argv[2]

refdates, refvalues = basicutil.read_from_file (fileorig)
dates, values = basicutil.read_from_file (file)

previd = 0
for d in refdates:
    if d in dates:
        previd = dates.index(d)
        print d, " , ", values[previd]
    else:
        previd = previd + 1
        if (previd == len(values)):
            previd = len(values) - 1
        print d, " , ", values[previd]

