import sys

def read_from_file (filename):
    dates = []
    values = []

    fp = open(filename)
    fp.readline()
    for l in fp:
        line = l.replace("\"", "")
        sline = line.split(",")
        
        if len(sline) < 7:
            print "Error in file format ", len(sline)
            print sline
            print l
            exit(1)
    
        datasplit = sline[0].split()
        if len(datasplit) != 2:
            print "Error in file format "
            print l
            print datasplit
            exit(1)
        
        day = int(datasplit[1])
        month = datasplit[0]
    
        year = int(sline[1])
        data = float(sline[2])
    
        dates.append(str(day)+"_"+month+"_"+str(year))
        values.append(data)
    
    fp.close()

    return dates, values

#####################################################################


if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " file1 file2"
    exit(1)

fileorig = sys.argv[1]
file = sys.argv[2]

refdates, refvalues = read_from_file (fileorig)
dates, values = read_from_file (file)

previd = 0
for d in refdates:
    if d in dates:
        previd = dates.index(d)
        print d, values[previd]
    else:
        print d, values[previd]

