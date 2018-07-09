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

    date = re.sub('[^ a-zA-Z0-9+\-]', '', sline[3])
    rating = re.sub('[^ a-zA-Z0-9+\-]', '', sline[1])

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
    #print d1, d2
    delta = d2 - d1
    for j in range(delta.days):
         print d1 + datetime.timedelta(j), " , ", ratings[i - 1]

d = 26
m = 6
y = 2018

fd = datetime.date(y, m, d)
sd = dates[len(dates) - 1]
fr = ratings[len(dates) - 1]
delta = fd - sd
for j in range(delta.days):
    print sd + datetime.timedelta(j), " , ", fr
print fd, " , ", fr
