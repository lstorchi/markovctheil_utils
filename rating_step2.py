import re
import sys
import datetime
import calendar

if len(sys.argv) != 2:
    print "usage: ", sys.argv[0], " filename "
    exit(1)

file = sys.argv[1]

nametonum = dict((v,k) for k,v in enumerate(calendar.month_abbr))

fp = open(file)

dates = []
ratings = []

for line in fp:
    sline = line.split(";")

    if len(sline) != 4:
        print "Error in file format"
        exit(1)

    date = re.sub('[^ a-zA-Z0-9]', '', sline[3])
    rating = re.sub('[^ a-zA-Z0-9]', '', sline[1])

    sdate = date.split()

    m = nametonum[sdate[0]]
    d = int(sdate[1])
    y = int(sdate[2])
    da = datetime.date(y, m, d)

    dates.append(da)
    ratings.append(rating)

    #print da, sdate, rating

fp.close()

for i in range(1, len(dates)):
    d1 = dates[i - 1]
    d2 = dates[i]
    delta = d2 - d1
    #print delta.days
    for j in range(-1 * delta.days):
        print d1 - datetime.timedelta(j), " , ", ratings[i - 1]
