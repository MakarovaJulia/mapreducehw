#!/usr/bin/env python2.7
import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(",")
    if len(columns) == 28: 
        try:
            countReviews = int(columns[16])
            print ("%s\n%s" % (columns[3],countReviews))
        except ValueError:
            pass