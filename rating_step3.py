import sys
import basicutil

if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " dates file"
    exit(1)

dates = sys.argv[1]
file = sys.argv[2]


previd = 0
for d in refdates:
    if d in dates:
        previd = dates.index(d)
        print d, " , ", values[previd]
    else:
        previd = previd + 1
        print d, " , ", values[previd]

