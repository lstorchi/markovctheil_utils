import datetime
import calendar

def read_from_file (filename):
    dates = []
    values = []

    nametonum = dict((v,k) for k,v in enumerate(calendar.month_abbr))

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
        
        d = int(datasplit[1])
        m = nametonum[datasplit[0]]
        y = int(sline[1])

        da = datetime.date(y, m, d)

        data = float(sline[2])
    
        dates.append(da)
        values.append(data)
    
    fp.close()

    return dates, values

