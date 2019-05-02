import numpy.linalg
import numpy.random
import scipy.stats
import scipy.io
import argparse
import numpy
import math
import sys
import os

import os.path

if __name__ == "__main__" :

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-m","--mat-filename", help="MAtlab matrix filename", \
            type=str, required=True, dest="matfilename")
    
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    args = parser.parse_args()

    filename = args.matfilename
    
    errmsg = []
    
    if not (os.path.isfile(filename)):
        print "File " + filename + " does not exist"
        exit(1)
    
    m = scipy.io.loadmat(filename)
    
    print len(m.keys())

    for name in m.iterkeys():
        if (isinstance( m[name],(numpy.ndarray))):
            if (len(m[name].shape) == 2):
                print name
                print m[name].shape[0], " , ", m[name].shape[1]

                for i in range(m[name].shape[0]):
                    for j in range(m[name].shape[1]-1):
                        sys.stdout.write( str(m[name][i, j]) + " , ")
                    sys.stdout.write( str(m[name][i, -1]) + "\n")

