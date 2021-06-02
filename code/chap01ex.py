"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2
import gzip

def readFemResp():
    dctFile = '2002FemResp.dct'
    datFile = '2002FemResp.dat.gz'
    nrows = None

    dct = thinkstats2.ReadStataDct(dctFile)
    df = dct.ReadFixedWidth(datFile, compression='gzip', nrows=nrows)
    return df

def crossVal(resp):
    dctFile = '2002FemPreg.dct'
    datFile = '2002FemPreg.dat.gz'
    nrows = None
    dct = thinkstats2.ReadStataDct(dctFile)
    preg = dct.ReadFixedWidth(datFile, compression='gzip', nrows=nrows)

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = readFemResp()
    
    print(resp.pregnum.value_counts())

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
