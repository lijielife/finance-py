################################################################################
# Copyright (C)  2010 Ray M. Salem
# http://code.google.com/p/finance-py/
# Distributed under the GPL license Version 3.0 ( See accompanying file
# License_ or copy at http://code.google.com/p/finance-py/LICENSE)
################################################################################

from numpy import *
from scipy import *
# Eponential Moving average
# in - input, out-output, length
def ema(input,length):
    if __debug__ and input.__len__() == 0:
      print "moving_average:ema -> input length is equal to 0"

    N = input.__len__();
    output = zeros(N);
    output[0] = input[0];
    sum = input[0];

    sf1 = 2.0/ (length+1.0);
    sf2 = 1.0-sf1;
    indxO = 1;
    for indxI in arange(1,N):
        sum = input[indxI] *sf1 + sum * sf2;
        output[indxO] = sum;
        indxO = indxO +1;
    return output

# Simple Moving average
def sma(input, length):
    weights = ones(length) / length
    output = convolve(input, weights, mode='full')[:len(input)]
    return output;

# moving avergage, allows for a specification of the type
def ma(input, length, type):
    if(type == "sma"):
         return sma(input, length);
    elif(type == "ema"):
         return ema(input, length);
    else:
         print ("incorrect moving average type specififed")


