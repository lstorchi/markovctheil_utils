import re
import sys
import datetime
import calendar

if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " dates file"
    exit(1)

datesfile = sys.argv[1]
file = sys.argv[2]

rat2num = {"AAA": 1, "Aaa":1, "AA": 2, "Aa":2, "AA-": 2, "AA+": 2, \
           "Aa1":2, "Aa2":2, "Aa3":2, "A+":3, "A":3,  "A-":3, \
           "A1":3, "A2":3, "A3":3, "BBB+":4, "BBB":4, "BBB-":4, \
           "Baa1":4, "Baa2":4, "Baa3":4, "BB+":5, "BB":5, "BB-":5, \
           "Ba1":5, "Ba2":5, "Ba3":5, "B+":6, "B":6, "B-":6, "B1":6, \
           "B2":6, "B3":6, "CCC+":7, "CCC":7, "CCC-":7, "CC":7, "C":7, \
           "Caa1":7, "Caa2":7, "Caa3":7, "Ca":7,"C-":8, "SD":8, "D":8, "RD":8}

rat2num_moodys = {"AAA": 1, "Aaa":1, "AA": 2, "Aa":2, "AA-": 2, "AA+": 2, \
           "Aa1":2, "Aa2":2, "Aa3":2, "A+":3, "A":3,  "A-":3, \
           "A1":3, "A2":3, "A3":3, "BBB+":4, "BBB":4, "BBB-":4, \
           "Baa1":4, "Baa2":4, "Baa3":4, "BB+":5, "BB":5, "BB-":5, \
           "Ba1":5, "Ba2":5, "Ba3":5, "B+":6, "B":6, "B-":6, "B1":6, \
           "B2":6, "B3":6, "CCC+":7, "CCC":7, "CCC-":7, "CC":7, "C":8, \
           "Caa1":7, "Caa2":7, "Caa3":7, "Ca":7,"C-":8, "SD":8, "D":8, "RD":8}


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
    ratings.append(rating.replace(" ", ""))

fp.close()

previd = 0
for d in refdates:
    if d in dates:
        previd = dates.index(d)
        #print d, " , ", rat2num_moodys[ratings[previd]]
        print d, " , ", rat2num[ratings[previd]]
    else:
        previd = previd + 1
        if (previd == len(ratings)):
            previd = len(ratings) - 1
        #print d, " , ", rat2num_moodys[ratings[previd]]
        print d, " , ", rat2num[ratings[previd]]
