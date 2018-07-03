import re
import sys
import datetime
import calendar

if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " dates file"
    exit(1)

datesfile = sys.argv[1]
file = sys.argv[2]

nametonum = dict((v,k) for k,v in enumerate(calendar.month_abbr))

refdates = []
fp = open(datesfile)
for line in fp:
    date = re.sub('[^ a-zA-Z0-9]', '', line)

    sdate = date.split()

    m = nametonum[sdate[0]]
    d = int(sdate[1])
    y = int(sdate[2])
    da = datetime.date(y, m, d)

    refdates.append(da)

fp.close()

fp = open(file)

dates = []
ratings = []

for line in fp:
    sline = line.split(",")

    date = sline[0]
    rating =  re.sub('[^ a-zA-Z0-9]', '', sline[1])

    sdate = date.split("-")

    d = int(sdate[2])
    m = int(sdate[1])
    y = int(sdate[0])
    da = datetime.date(y, m, d)

    dates.append(da)
    ratings.append(rating)

fp.close()

previd = 0
for d in refdates:
    if d in dates:
        previd = dates.index(d)
        print d, " , ", ratings[previd]
    else:
        previd = previd + 1
        if (previd == len(ratings)):
            previd = len(ratings) - 1
        print d, " , ", ratings[previd]

