#!/usr/bin/env python2.7

from operator import itemgetter 
import sys

recipesreviewmap = {}

for line in sys.stdin:
    line = line.strip()
    recipes, count = line.split("\n")
    try:
        count = int(count)
        recipesreviewmap[recipes] = recipesreviewmap.get(recipes, 0) + count
    except ValueError:
        pass

sort_recipesreviewmap = sorted(recipesreviewmap.items(), key=itemgetter(0))

for recipes, countreviews in sort_recipesreviewmap:
    print ('%s\t%s' % (recipes, countreviews))