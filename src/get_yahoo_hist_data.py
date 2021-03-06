################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file 
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

################################################################################
# Author - Ray Salem
# Description
# Creation date
# History
################################################################################

#!/usr/bin/env python
from matplotlib.finance import quotes_historical_yahoo
import sys
from datetime import date,timedelta


################################################################################
# Get historical data
################################################################################
def get(symbol, daysBack, fileWrite):
    if __debug__ and resolution != 1 :
      print "get_yahoo_hist_data:get - Does not support resolution other then 1"
    date1 = date.today() - timedelta(days=daysBack)
    # end
    date2 = date.today()

    quotes = quotes_historical_yahoo(
        symbol, date1, date2)


    if(fileWrite == 1):
        f = open(symbol + ".csv", 'w')
        for line in quotes:
            for val in line:
                f.write(str(val))
                f.write(',')
            f.write('\n')
        f.close()
################################################################################

if (sys.argv.__len__() ==1):
    print "Version 0.0.1"
    print "Must provide symbol and days going back.  for example: yhoo 1000"
    print "Output format is data, open, close, high, low, volume"  
    exit()
else:
    symbol   = sys.argv[1]
    daysBack = int(sys.argv[2])




get(symbol, daysBack, 0)
